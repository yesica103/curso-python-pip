from django.shortcuts import render

# Create your views here.
def my_view(request):
    # This is a simple view that renders a template
    return render(request, "my_first_app/car_list.html")
