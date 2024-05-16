from django.contrib import admin

from reservations.models import ReservationsModel


@admin.register(ReservationsModel)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'create_at']
    search_fields = ['full_name', 'email', 'massage']
    list_filter = ['create_at', 'update_at']
