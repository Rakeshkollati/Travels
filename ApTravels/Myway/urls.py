from django.urls import path
from django.contrib.auth import views as v
from Myway import views

urlpatterns = [
	
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('bt/',views.bookticket,name="bkt"),
	path('register/',views.register,name="rg"),
	path('login/',v.LoginView.as_view(template_name="html/login.html"),name="log"),

]