from django.urls import path
from . import views


#api est nom de l'application definit sur views
app_name = "api_home"

urlpatterns = [
   
    path('', views.page_home),
    path('api/', views.create_recipe, name = 'page_api'),

]