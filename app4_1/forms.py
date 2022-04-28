from app4_1.models import Model1
from django import forms


class Modelform1(forms.ModelForm):
    class Meta:
        model = Model1
        fields = (
            "id",
            "name",
            "address",
        )
