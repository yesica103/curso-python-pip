from django.shortcuts import render
from my_first_app.models import Car, Author, Profile
from django.http import HttpResponse 
from django.views.generic.base import TemplateView

#from my_first_app.models import Car, Profile
# Create your views here.
def my_view(request):
    # This is a simple view that renders a template
    car_list = Car.objects.all() 
    context = {
        "car_list": car_list
    }
    return render(request, "my_first_app/car_list.html", context)

class CarListView(TemplateView):
    template_name = "my_first_app/car_list.html"

    def get_context_data(self):
        car_list = [
            {"title": "BMW"},
            {"title": "Mazda"}
        ]
        return {
            "car_list": car_list
        }


def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

def author_profile_view(request, *args, **kwargs):
    # This is a simple view that renders a template
    author = Author.objects.get(id=kwargs['id'])
    
    context = {
        "author_profile": author
    }
    return render(request, "my_first_app/author_profile.html", context)

