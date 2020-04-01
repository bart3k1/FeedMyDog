from django.contrib.admin.widgets import AdminDateWidget

from .models import AddCallendog, Caretaker
from django import forms


class CallendogForm(forms.ModelForm):
    class Meta:
        model = AddCallendog
        exclude = ["user"]
        fields = ["title", "start_date", "stop_date", "frequency", "caretakers"]
        widgets = {
            'start_date': forms.DateInput(format=('%d/%m/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'stop_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CallendogForm, self).__init__(*args, **kwargs)
        self.fields['caretakers'].queryset = Caretaker.objects.all().filter(user=user)