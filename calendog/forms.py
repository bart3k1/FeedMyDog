from django.contrib.admin.widgets import AdminDateWidget

from .models import AddCallendog, Caretaker
from django import forms


class CallendogForm(forms.ModelForm):
    class Meta:
        model = AddCallendog
        fields = ["title", "start_date", "stop_date", "frequency", "caretakers"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CallendogForm, self).__init__(*args, **kwargs)
        self.fields['caretakers'].queryset = Caretaker.objects.all().filter(user=user)