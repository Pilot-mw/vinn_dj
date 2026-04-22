from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils import timezone
from django.http import JsonResponse
from .models import Mix, Client, GalleryImage, Booking
import json


class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'caption', 'image')
    search_fields = ('caption',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'logo')
    search_fields = ('name',)


class MixAdmin(admin.ModelAdmin):
    list_display = ('title', 'audio_file')
    list_display_links = ('title',)
    search_fields = ('title',)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event_type', 'event_date', 'event_time', 'venue', 'created_at', 'row_actions')
    list_filter = ('event_type', 'event_date')
    search_fields = ('name', 'email', 'venue')
    readonly_fields = ('created_at',)

    def event_time(self, obj):
        if obj.event_time:
            return obj.event_time.strftime('%H:%M')
        return '-'
    event_time.short_description = 'Time'

    def row_actions(self, obj):
        if not obj:
            return ''
        reply_url = f'mailto:{obj.email}?subject=Re:%20Your%20Booking%20-%20DJ%20VIN&body=Hi%20{obj.name},%20%0A%0AThank%20you%20for%20booking%20DJ%20VIN.%20%0A%0AWe%20will%20be%20in%20touch%20soon.'
        return format_html(
            '<div class="row-actions">'
            '<a href="{}" class="view-btn" target="_blank">View</a>'
            '<a href="{}" class="reply-btn" target="_blank">Reply</a>'
            '<a href="{}" class="edit-btn">Edit</a>'
            '<a href="{}" class="delete-btn">Delete</a>'
            '</div>',
            reverse('admin:core_booking_change', args=[obj.pk]) + '?pop=1',
            reply_url,
            reverse('admin:core_booking_change', args=[obj.pk]),
            reverse('admin:core_booking_delete', args=[obj.pk])
        )
    row_actions.short_description = 'Actions'


admin.site.register(Mix, MixAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Booking, BookingAdmin)
