from django.shortcuts import render,redirect,HttpResponse
from .forms import AppointmentForm
from .models import Appointment
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required
import string




def index(request):
    return render(request,'core/index.html')


@login_required()
def appointment(request):
    form = AppointmentForm
    user = request.user 
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            for i in first_name and last_name:
                x = string.ascii_lowercase+string.ascii_uppercase
                if i not in x:
                    messages.warning(request, ' الاسم يجب ان يكون بالحروف اللاتينية فقط')
                    return redirect('appointment')


            if date.strftime("%A") == 'Friday':
                messages.warning(request, 'نحن لانعمل ايام الجمعة')
                return redirect('appointment')
            if date > datetime.date.today()+datetime.timedelta(6):
                messages.warning(request, 'لايمكن الحجز بعد اكثر من اسبوع من تاريخ اليوم')
                return redirect('appointment')
            if date < datetime.date.today():
                messages.warning(request, 'ناريخ فائت! اختر تاريخا مستقبليا')
                return redirect('appointment')

            appointments=Appointment.objects.filter(date=date)
            for appointment in appointments:
                if appointment.time == time:
                    messages.warning(request, 'هذا الموعد محجوز مسبقا')
                    return redirect('appointment')
            
            userappointments = Appointment.objects.filter(user=user,date=date)
            X=0
            for x in userappointments :
               X +=1
               if X >= 1:
                    messages.warning(request, 'لا يمكنك حجز اكثر من موعد واحد في اليوم')
                    return redirect('appointment')

     
            else:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, 'لقد حجزت موعدا جديدا, الرجاء تحميل استمارة الموعد او طباعتها وارفاقها مع المريض عند الزيارة, مرحبا بكم ')
                return redirect('profile')


    
    day1 = datetime.date.today()
    opp1 = Appointment.objects.filter(date=day1)

    day2 = datetime.date.today()+datetime.timedelta(1)
    opp2 = Appointment.objects.filter(date=day2)

    day3 = datetime.date.today()+datetime.timedelta(2)
    opp3 = Appointment.objects.filter(date=day3)

    day4 = datetime.date.today()+datetime.timedelta(3)
    opp4 = Appointment.objects.filter(date=day4)

    day5 = datetime.date.today()+datetime.timedelta(4)
    opp5 = Appointment.objects.filter(date=day5)

    day6 = datetime.date.today()+datetime.timedelta(5)
    opp6 = Appointment.objects.filter(date=day6)

    day7 = datetime.date.today()+datetime.timedelta(6)
    opp7 = Appointment.objects.filter(date=day7)


    timelist = [
        '09:00-10:00',
        '10:00-11:00',
        '11:00-12:00',
        '14:00-15:00',
        '15:00-16:00',
        '16:00-17:00',
        ]
    context = {
        'form':form, 
        'timelist':timelist,

        'day1':day1,
        'opp1':opp1,
        'day2':day2,
        'opp2':opp2,
        'day3':day3,
        'opp3':opp3,
        'day4':day4,
        'opp4':opp4,
        'day5':day5,
        'opp5':opp5,
        'day6':day6,
        'opp6':opp6,
        'day7':day7,
        'opp7':opp7,
        }

    return render(request, 'core/appointment.html',context)
