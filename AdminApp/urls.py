from django.urls import path
from. import views
urlpatterns = [
        path('admins',views.admins,name='admins'),
        path('logins',views.logins,name='logins'),
        path('adminlogin',views.adminlogin,name='adminlogin'),
        path('adminlogout',views.adminlogout,name='adminlogout'),
        path('addcategory',views.addcategory,name='addcategory'),
        path('discategory',views.discategory,name='discategory'),
        path('addproduct',views.addproduct,name='addproduct'),
        path('disproduct',views.disproduct,name='disproduct'),
        path('categorytable',views.categorytable,name='categorytable'),
        path('edit/<int:id>/',views.edit,name='edit'),
        path('update/<int:id>/',views.update,name='update'),
        path('delete/<int:id>/',views.delete,name='delete'),
        path('producttable',views.producttable,name='producttable'),
        path('edit1/<int:id>/',views.edit1,name='edit1'),
        path('update1/<int:id>/',views.update1,name='update1'),
        path('delete1/<int:id>/',views.delete1,name='delete1'),
        path('viewregister',views.viewregister,name='viewregister'),
        path('viewcontacts',views.viewcontacts,name='viewcontacts'),
        path('vieworder',views.vieworder,name='vieworder'),
        path('viewcomplaints',views.viewcomplaints,name='viewcomplaints'),
        path('deliver/<int:id>/',views.deliver,name='deliver'),
        path('deliveredorder',views.deliveredorder,name='deliveredorder'),
        
        path('replay/<int:id>/',views.replay,name='replay'),
        path('displayreplay/<int:id>/',views.displayreplay,name='displayreplay'),
]