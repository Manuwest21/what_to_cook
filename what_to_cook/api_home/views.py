from django.shortcuts import redirect, render
from . import functions
from django.views.generic import *
from .forms import IngredientsForm


# Create your views here.

def login(request):
    return render(request,'pages_main/login.html')



def register(request):
    return render(request,'pages_main/register.html')



def page_home(request):
    return render(request, 'pages_main/home.html')


# def index(request):
#     if request.method == "POST":
#         form = StudentsForm(request.POST).save()
#         return redirect('/api')
#     else :
#         form = StudentsForm()

#     return render(request, 'pages_main/api_page.html', {'form' : form})




def create_recipe(request):
    form = IngredientsForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print(functions.findrecipe(functions.ingredients_from_UI)["RecipeName"])
            print(dict(form.cleaned_data))
        return render(request, 'pages_main/api_page.html', {'form': form })
    else:
        return render(request, 'pages_main/api_page.html', {'form': form })





# def ingred_fnct(request):
#     if request.method == 'GET':
        
#         form = IngredientsForm()
#        # a = dict(form.data)['proteins']
#        # return(a)
#        # print(dict(form.data)['proteins'])

        
#         return render(request, 'pages_main/api_page.html', {'form' : form})

   
#     if request.method == "POST":
#         form = IngredientsForm(request.POST)
#         db_response = form.save()
#        # print(db_response.
#         if form.is_valid():
#            # a = dict(form.data)['proteins']
#            ingredients_list = form.cleaned_data
#            for cle, valeur in ingredients_list.items() :
#             if len(valeur) != 0:
#                 print ("les ingrédients du groupe", cle, "sont" , valeur)
            

#             return render(request, 'pages_main/api_page.html', {'form': form })
           
            
#         else :
#             print("formulaire non valide")
#     else :
#         form = IngredientsForm()

#     return render(request, 'pages_main/api_page.html', {'form' : form})



