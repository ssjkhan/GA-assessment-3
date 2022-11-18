from django.forms import ModelForm
from . import models


class WidgetForm(ModelForm):
    class Meta:
        model = models.Widget
        fields = ["description", "quantity"]