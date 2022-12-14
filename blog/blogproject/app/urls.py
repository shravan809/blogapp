from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.blog),
    path('signup/',v.sign_up),
    path('aboutus/',v.aboutus),
    path('login/',v.loginpage),
    path('details/',v.details,name='details'),
    path('logout/',v.logoutpage,name='logout'),
    path('contact/',v.contact_view),
    path('delete/<int:id>/',v.delete_data, name="deletedata"),
    path('<int:id>/', v.update_data, name="updatedata"),
    path('psw',v.password,name='psw')
]