from django.shortcuts import render
from .models import Widget
from .forms import WidgetForm
# Create your views here.

def home(req):
    widgets = list(Widget.objects.values())

    count = 0 
    for w in widgets:
        count += int(w["quantity"])
    form = WidgetForm
    
    data = {
        "widgets" : widgets,
        "count" : count,
        "form" : form
    }


    return render(req, 'widgets.html', data) 