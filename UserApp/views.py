from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from  UserApp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from AdminApp.models import *
from django.db.models.aggregates import Sum
import stripe
from django.conf import settings
# Create your views here.
def users(request):
    data=Category.objects.all()
    data1=Product.objects.all()
    return render(request,'users.html',{'data':data,'data1':data1})


def products(request):
    data=Product.objects.all()
    return render(request,'products.html',{'data':data,})
def contact(request):
    return render(request,'contact.html')
def discontact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']
        data=Contact(Name=name,
                     email=email,
                     phone=phone,
                     Subject=subject,
                     Message=message)
        data.save()
        return redirect('feedback')
def about(request):
    return render(request,'about.html')

def viewfruit(request,id):
    data=Product.objects.filter(id=id)
    return render(request,'viewfruit.html',{'data':data})

def fruits(request):
    data=Category.objects.filter(categoryname='Fruits').all()
    data1=Product.objects.filter(productcategory='Fruits').all()
    return render(request,'fruits.html',{'data':data,'data1':data1})
def vegetables(request):
    data=Category.objects.filter(categoryname='Vegetables').all()
    data1=Product.objects.filter(productcategory='Vegetables').all()
    return render(request,'vegetables.html',{'data':data,'data1':data1})
def dryfruits(request):
    data=Category.objects.filter(categoryname='Dry Fruits').all()
    data1=Product.objects.filter(productcategory='Dry Fruits').all()
    return render(request,'dryfruits.html',{'data':data,'data1':data1})
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def disregister(request):
    if request.method=='POST':
        
        username=request.POST['name']
        email=request.POST['email']
        
        password=request.POST['password']
        
        phone=request.POST['phone']
        data=Register(Name=username,
                     email=email,
                     password=password,
                     phone=phone
                     )
        data.save()
    return redirect('login')
def publicdata(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        if Register.objects.filter(email=email,password=password).exists():
            data = Register.objects.filter(email=email,password=password).values('Name','id','phone').first()
           
            request.session['u_id'] = data['id']
            request.session['username_u'] = data['Name']
            request.session['phone_u'] = data['phone']
            request.session['u_mail'] = email
            
            request.session['password_u'] = password
            return redirect('users') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('users')
def userlogout(request):
    del request.session['u_mail']
    
    del request.session['u_id']
    
    
    del request.session['username_u']
    del request.session['password_u']
    del request.session['phone_u']
    return redirect('users')
def feedback(request):
    
    return render(request,'feedback.html')



def cart(request):
    u=request.session.get('u_id')
    data=Cart.objects.filter(userid=u,status=0)
    s=Cart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'cart.html',{'data':data,'s':s})

def cartdata(request,id):
    if request.method=="POST":
        userid=request.session.get('u_id')
        quantity=request.POST['quantity']
        total=request.POST['total']
        
        data=Cart(userid=Register.objects.get(id=userid),
                  productid=Product.objects.get(id=id),
                  quantity=quantity,
                  total=total,
                  )
        data.save()
        return redirect('cart')

def removecart(request,id):
    Cart.objects.filter(id=id).delete()
    return redirect('cart')
def checkout(request):
    u=request.session.get('u_id')
    data=Cart.objects.filter(userid=u,status=0)
    
    s=Cart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    
    return render(request,'checkout.html',{'data':data,'s':s})

stripe.api_key = settings.STRIPE_SECRET_KEY
def checkoutdata1(request):
    if request.method == "POST":
        userid = request.session.get('u_id')
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        country = request.POST['country']
        address = request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        city = request.POST['city']
        zip = request.POST['zip']
        order=Cart.objects.filter(userid=userid, status=0)
        #product = Product.objects.get(id=product_id)
        totalamount=0
        for i in order:
            totalamount+=i.total
            data=Checkout(userid=Register.objects.get(id=userid),
                     cartid=Cart.objects.get(id=i.id),
                      firstname=firstname,
                        lastname=lastname,
                        address=address,
                        city=city,
                        district=district,
                                    
                        state=state,
                        country=country,
                        zip=zip,)
            data.save()
            Cart.objects.filter(id=i.id).update(status=1)
            #print(i.total)
        
        session = stripe.checkout.Session.create(
         payment_method_types = ['card'],
         line_items=[{
                'price_data':{
                    'currency': 'inr',
                    'product_data':{
                        'name': 'product.name',
                     },
                   'unit_amount':int(totalamount)*100,
                   
               },
                 'quantity':1,
        }],
        mode='payment',
        success_url = "http://127.0.0.1:8000/history",
        cancel_url = "http://127.0.0.1:8000/cancel",
        #client_reference_id=product_id,
    )
    return redirect(session.url, code=303)
    #for i in order:
        #data=Checkout(userid=Register.objects.get(id=userid),
        #              cartid=Cart.objects.get(id=i.id),
        #               firstname=firstname,
        #                 lastname=lastname,
        #                 address=address,
        #                 city=city,
        #                 district=district,
                                    
        #                 state=state,
        #                 country=country,
        #                 zip=zip,)
        # data.save()
        #Cart.objects.filter(id=i.id).update(status=1)
    return redirect('history')
#def checkout_session(request, product_id):
    # product = Product.objects.get(id=product_id)
    # session = stripe.checkout.Session.create(
    #     payment_method_types = ['card'],
    #     line_items=[{
    #             'price_data':{
    #                 'currency': 'inr',
    #                 'product_data':{
    #                     'name': product.name,
    #                 },
    #                 'unit_amount':int(product.price)*100,
                   
    #             },
    #             'quantity':1,
    #     }],
    #     mode='payment',
    #     success_url = "http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}",
    #     cancel_url = "http://127.0.0.1:8000/pay_cancel",
    #     client_reference_id=product_id,
    # )
    # return redirect(session.url, code=303)

# def pay_success(request):
#     session = stripe.checkout.Session.retrieve(request.GET['session_id'])
#     plan_id = session.client_reference_id
#     plan = SubscriptionPlan.objects.get(id=plan_id)
#     customer_id = request.session.get('cid')
#     #print(customer_id)
#     subscriber = SubscribedUser(
#         customer = Customer.objects.get(id=customer_id),
#         subscription = plan,
#     )
#     subscriber.save()
#     Customer.objects.filter(id=customer_id).update(is_subscribed=True)

#     subscriber.end_date = subscriber.start_date+timedelta(days=plan.plan_validity)
#     subscriber.save()
   
   
#     if 'cid' in request.session:
#         del request.session['cid']
#     return redirect('customer_login')




def history(request):
    u=request.session.get('u_id')
   
    data=Checkout.objects.filter(userid=u).order_by('-id')
    data1=Replay.objects.filter(userid=u).order_by('-id')
    
    return render(request,'history.html',{'data':data,'data1':data1})
def cancel(request):
    return render(request,'cancel.html')

def complaint(request,id):
    u=request.session.get('u_id')
    data=Checkout.objects.filter(userid=u,id=id)
    return render(request,'complaint.html',{'data':data})
def discomplaint(request,id):
    if request.method == "POST":
        userid = request.session.get('u_id')
        issue=request.POST['issues']
        
        data=Complaint(userid=Register.objects.get(id=userid),
                        compid=Checkout.objects.get(id=id),
                        issue=issue
                  
                  )
        data.save()
        return redirect('complainaccept')
def complainaccept(request):
    u=request.session.get('u_id')
    data=Checkout.objects.filter(userid=u)
    return render(request,'complainaccept.html',{'data':data})

def message(request):
    u=request.session.get('u_id')
    data1=Replay.objects.filter(userid=u).order_by('-id')
    return render(request,'message.html',{'data1':data1})