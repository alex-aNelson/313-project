from django import forms
from .models import Event

class AddEventForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        label="",
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control", "placeholder": "Title"}
        ),
    )
    description = forms.CharField(
        required=False,
        label="",
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control", "placeholder": "Description"}
        ),
    )

    # event_date = forms.DateField(
    #     required=True,
    #     label="",
    #     widget=forms.widgets.DateTimeBaseInput(
    #         attrs={"class": "form-control", "placeholder": "Date"}
    #     )
    #      )

    class Meta:
        model = Event
        fields = "__all__"