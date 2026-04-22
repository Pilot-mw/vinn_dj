from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mix, Client, GalleryImage, Booking, Notification
from .forms import BookingForm


def home(request):
    mixes = Mix.objects.all()
    clients = Client.objects.all()
    gallery = GalleryImage.objects.all()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            send_booking_notification(booking)
            return redirect('/?booked=1')
    else:
        form = BookingForm()

    return render(request, 'core/home.html', {
        'mixes': mixes,
        'clients': clients,
        'gallery': gallery,
        'form': form
    })


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            send_booking_notification(booking)
            return redirect('/?booked=1')
    else:
        form = BookingForm()

    return render(request, 'core/booking.html', {'form': form})


def send_booking_notification(booking):
    subject = f'New Booking: {booking.name} - {booking.get_event_type_display()}'
    message = f'''New Booking Received!

Name: {booking.name}
Email: {booking.email}
Event Type: {booking.get_event_type_display()}
Date: {booking.event_date}
Time: {booking.event_time}
Venue: {booking.venue}
Message: {booking.message}

Login to admin to view details: http://127.0.0.1:8000/admin/core/booking/
'''
    from_email = settings.DEFAULT_FROM_EMAIL
    
    try:
        send_mail(
            subject,
            message,
            from_email,
            ['mtiwajason@gmail.com'],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Email error: {e}")
    
    Notification.objects.create(
        notification_type='booking',
        title=f'New Booking: {booking.name}',
        message=f'{booking.get_event_type_display()} - {booking.event_date} at {booking.venue}',
        link='/admin/core/booking/'
    )


def music(request):
    mixes = Mix.objects.all()
    return render(request, 'core/music.html', {'mixes': mixes})


def payment(request):
    track = request.GET.get('track', '')
    return render(request, 'core/payment.html', {'track': track})


def notifications(request):
    notifications = Notification.objects.all()[:20]
    unread_count = Notification.objects.filter(is_read=False).count()
    
    data = {
        'notifications': [
            {
                'id': n.id,
                'type': n.notification_type,
                'title': n.title,
                'message': n.message,
                'is_read': n.is_read,
                'created_at': n.created_at.strftime('%b %d, %Y %H:%M'),
                'link': n.link
            }
            for n in notifications
        ],
        'unread_count': unread_count
    }
    return JsonResponse(data)


@csrf_exempt
def mark_notification_read(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        notification_id = data.get('id')
        if notification_id:
            try:
                notification = Notification.objects.get(id=notification_id)
                notification.is_read = True
                notification.save()
                return JsonResponse({'success': True})
            except Notification.DoesNotExist:
                pass
    return JsonResponse({'success': False})
