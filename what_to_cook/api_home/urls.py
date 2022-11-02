from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "api_home"

urlpatterns = [
    path('test', views.login),   #api est nom de l'application definit sur views
    path('', views.page_home, name ='home'),
    path('api/', views.create_recipe, name ='api'),
    #path('special/', views.create_recipe, name='special'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
    path('recipe/', views.recipe_rslt),
]