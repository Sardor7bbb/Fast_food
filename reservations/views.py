from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from reservations.forms import ReservationForm


class ReservetionView(CreateView):
    template_name = 'reservation.html'
    form_class = ReservationForm

    def get_success_url(self):
        return reverse_lazy('pages:home')

