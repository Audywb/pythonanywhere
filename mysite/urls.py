<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from myweb import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.loginPage),
    #path('polls/', include('polls.urls')),
    path('myweb/', include('myweb.urls')),
    path('united', views.united),
    path('index', views.index),
    path('shopping1', views.shopping1),
    path('shopping2', views.shopping2),
    path('shopping3', views.shopping3),
    path('login/', views.loginPage),
    path('register/', views.registerPage),
    path('logout/', views.logout),
    path('sell01/', views.sell01),
    path('Sell_view/', views.Sell_view),
    path('add_model/', views.add_model),
    path('add_model2/', views.add_model2),
    path('show/', views.show),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
from django.contrib import admin
from django.urls import path, include
from myweb import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.loginPage),
    #path('polls/', include('polls.urls')),
    path('myweb/', include('myweb.urls')),
    path('united', views.united),
    path('index', views.index),
    path('shopping1', views.shopping1),
    path('shopping2', views.shopping2),
    path('shopping3', views.shopping3),
    path('login/', views.loginPage),
    path('register/', views.registerPage),
    path('logout/', views.logout),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> eef8e615a30ffdf2c1cbb57a112645b3b53aaa36
