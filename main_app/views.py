from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
# Create your views here.

def home(req):
    if req.method == "POST":
        form = WidgetForm(req.POST)
        new_widget = form.save(commit=False)
        new_widget.save()

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

def delete_widget(req, widget_id):
    widg = Widget.objects.filter(id = widget_id).delete()
    return redirect(home)