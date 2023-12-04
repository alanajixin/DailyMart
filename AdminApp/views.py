from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from. models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from UserApp.models import *

# Create your views here.

def admins(request):
    category=Category.objects.all().count()
    product=Product.objects.all().count()
    contact=Contact.objects.all().count()
    feedback=Complaint.objects.all().count()
    user=Register.objects.all().count()
    order=Checkout.objects.all().count()
    
    return render(request,'admins.html',{'category':category,'product':product,'contact':contact,'feedback':feedback,'user':user,
                                         'order':order})
def logins(request):
    return(render,'adminlogin.html')
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username_a'] = username
            request.session['password_a'] = password
            return redirect('admins')
        else:
            return render(request,'adminlogin.html', {'msg':'Sorry Invalid User Credentials'})
    else:
        return render(request, 'adminlogin.html')
def adminlogout(request):
    del request.session['username_a']
    del request.session['password_a']
    return redirect('admins')
def addcategory(request):
    return render(request,'addcategory.html')
def discategory(request):
    if request.method=='POST':
        categoryname=request.POST['categoryname']
        categorydescription=request.POST['description']
        categoryimage=request.FILES['categoryimage']
        data=Category(categoryname=categoryname,
                      categoryimage=categoryimage,
                      description=categorydescription)
        data.save()
        return redirect('addcategory')

def addproduct(request):
    data=Category.objects.all()
    return render(request,'addproduct.html',{'data':data})
def disproduct(request):
    if request.method=='POST':
        productname=request.POST['productname']
        productprice=request.POST['productprice']
        productcategory=request.POST['productcategory']
        productimage=request.FILES['productimage']
        data=Product(productname=productname,
                      productcategory=productcategory,
                      productimage=productimage,
                      productprice=productprice)
        data.save()
        return redirect('addproduct')
def edit(request,id):
    data=Category.objects.filter(id=id)
    return render(request,'editcategory.html',{'data':data})
def update(request,id):
    if request.method=='POST':
        categoryname=request.POST['categoryname']
        categorydescription=request.POST['description']
        try:
            img_c = request.FILES['categoryimage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=id).categoryimage
        Category.objects.filter(id=id).update(categoryname=categoryname,
                      categoryimage=file,
                      description=categorydescription
                    )
        return redirect('categorytable')
def delete(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('categorytable')
def categorytable(request):
    data=Category.objects.all()
    return render(request,'categorytable.html',{'data':data})
def producttable(request):
    data=Product.objects.all()
    return render(request,'producttable.html',{'data':data})
def edit(request,id):
    data=Category.objects.filter(id=id)
    return render(request,'editcategory.html',{'data':data})
def update(request,id):
    if request.method=='POST':
        categoryname=request.POST['categoryname']
        categorydescription=request.POST['description']
        try:
            img_c = request.FILES['categoryimage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=id).categoryimage
        Category.objects.filter(id=id).update(categoryname=categoryname,
                      categoryimage=file,
                      description=categorydescription
                    )
        return redirect('categorytable')
def delete(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('categorytable')

def producttable(request):
    data=Product.objects.all()
    
    return render(request,'producttable.html',{'data':data})
   
def edit1(request,id):
    data=Product.objects.filter(id=id)
    data1=Category.objects.all()
    return render(request,'edit1.html',{'data':data,'data1':data1})
def update1(request,id):
    if request.method=='POST':
        productname=request.POST['productname']
        productcategory=request.POST['productcategory']
        productprice=request.POST['productprice']

        try:
            img_c = request.FILES['productimage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Product.objects.get(id=id).productimage
        Product.objects.filter(id=id).update(productname=productname,
                                             productcategory=productcategory,
                                             productprice=productprice,
                                             productimage=file
                    )
        return redirect('producttable')
    
def delete1(request,id):
    Product.objects.filter(id=id).delete()
    return redirect('producttable') 

def viewregister(request):
    data=Register.objects.all()
    return render(request,'viewregister.html',{'data':data})   
def viewcontacts(request):
    data=Contact.objects.all()
    return render(request,'viewcontacts.html',{'data':data})   
def vieworder(request):
    
    data=Checkout.objects.filter(status=0)
    return render(request,'vieworder.html',{'data':data}) 
def deliver(request,id) :
    data=Checkout.objects.filter(id=id).update(status=1)
    return redirect('deliveredorder')
def deliveredorder(request):
    data=Checkout.objects.filter(status=1)
    return render(request,'deliveredorder.html',{'data':data}) 
def viewcomplaints(request):
    data=Complaint.objects.filter(status=0)
    return render(request,'viewcomplaint.html',{'data':data})

def replay(request,id):
    data=Complaint.objects.filter(id=id)
    return render(request,'replay.html',{'data':data})
def displayreplay(request,id):
    data=Complaint.objects.filter(id=id).update(status=1)
    if request.method == "POST":
        u=request.session.get('u_id')
        message=request.POST['message']
        data=Replay(userid=Register.objects.get(id=u),
                    complaintid=Complaint.objects.get(id=id),
                    message=message
                  
                  )
        data.save()
        return redirect('viewcomplaints')

