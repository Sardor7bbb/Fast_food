from django import forms
from reservations.models import ReservationsModel


class ReservationForm(forms.ModelForm):
    class Meta:
        madel = ReservationsModel
        fields = '__all__'
