from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reminder

# Create your views here.

def create_reminder(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')

       
        reminder = Reminder.objects.create(date_and_time=f"{date} {time}", message=message)
        reminder.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'})