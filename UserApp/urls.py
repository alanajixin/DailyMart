from django.urls import path
from. import views
urlpatterns = [path('users',views.users,name='users'),
               path('products',views.products,name='products'),
                path('contact',views.contact,name='contact'),
                path('discontact',views.discontact,name='discontact'),
                path('about',views.about,name='about'),
                path('viewfruit/<int:id>/',views.viewfruit,name='viewfruit'),
                path('Fruits',views.fruits,name='fruits'),
                path('Vegetables',views.vegetables,name='vegetables'),
                path('Dry Fruits',views.dryfruits,name='dryfruits'),
                path('login',views.login,name='login'),
                path('register',views.register,name='register'),
                path('disregister',views.disregister,name='disregister'),
                path('publicdata',views.publicdata,name='publicdata'),
                path('userlogout',views.userlogout,name='userlogout'),
                path('feedback',views.feedback,name='feedback'),
                
                path('cart',views.cart,name='cart'),
                path('cartdata/<int:id>/',views.cartdata,name='cartdata'),
                path('removecart/<int:id>/',views.removecart,name='removecart'),
                path('checkout',views.checkout,name='checkout'),
                
                path('checkoutdata1',views.checkoutdata1,name='checkoutdata1'),
                path('history',views.history,name='history'),
                path('complaint/<int:id>/',views.complaint,name='complaint'),
                path('discomplaint/<int:id>/',views.discomplaint,name='discomplaint'),
                path('complainaccept',views.complainaccept,name='complainaccept'),
                path('cancel',views.cancel,name='cancel'),
                path('message',views.message,name='message'),

]