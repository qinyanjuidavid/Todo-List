from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
app_name="myapp"


urlpatterns=[
path('home/',views.home,name='home'),
path('register/',views.Registration,name='register'),
path('',auth_views.LoginView.as_view(template_name="myapp/login.html"),name="login"),
path('logout/',auth_views.LogoutView.as_view(template_name='myapp/logout.html'),name="logout"),
path('update/<id>/',views.update,name="update"),
path('delete/<id>/',views.delete,name='delete')
]
