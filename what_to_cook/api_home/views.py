from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .forms import IngredientsForm
from . import functions
from .models import ingredients_list




def page_home(request):

    return render(request, 'pages_main/home.html')



# def index(request):
#     if request.method == "POST":
#         form = StudentsForm(request.POST).save()
#         return redirect('/api')











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


def create_recipe(request):
    form = IngredientsForm(request.POST)
    ingredient_choices = ingredients_list
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print(functions.findrecipe(functions.ingredients_from_UI)["RecipeName"])
            print(dict(form.cleaned_data))
        return render(request, 'pages_main/cedric.html', {'form': form })
    else:
        return render(request, 'pages_main/cedric.html', {'form': form, 'ingredient_choices': ingredient_choices })


@login_required
def special_view(request):
    return render(request, 'divers/special_view_page.html')

class SignupPage(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
