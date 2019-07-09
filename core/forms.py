from django import forms
from core.models import Customer


class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['user'].required = False
        self.fields['Emi'].required = False

    class Meta:
        model = Customer
        fields = "__all__"
