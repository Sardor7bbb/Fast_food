from django.db import models

class ReservationsModel(models.Model):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
