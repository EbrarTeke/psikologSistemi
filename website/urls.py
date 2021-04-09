from django.urls import path, include
from . import views
urlpatterns = [
    
    path('', views.home , name="home"),
    path('contact.html', views.contact , name="contact"),
    path('about.html', views.about, name="about"),
    path('gallery.html', views.gallery , name="gallery"),
    path('blog.html', views.blog , name="blog"),
    path('services.html', views.services , name="services"),
    path('login_user.html', views.login_user , name="login_user"),
    path('register/', views.register , name="register"),
    path('logout/',views.logout_user,name='logout'),
    path('personelinf/',views.personelinf,name='personelinf'),
    path('change_password/',views.change_password,name='change_password'),
    path('booking/',views.booking,name='booking'),
   

]
