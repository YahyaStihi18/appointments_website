from django.shortcuts import render,redirect,reverse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterFrom,AddInfoForm
from core.models import Appointment
from .models import Profile
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf



@login_required
def profile(request):
    user=request.user
    appointments = Appointment.objects.filter(user=user)
    context = {
        'appointments':appointments,
    }
    return render(request,'users/profile.html',context)

@login_required
def delete_appointment(request,id):
    user = request.user  # you get the loged user
    appointment = Appointment.objects.get(id=id)  # you get the order through the pk
    if appointment.user == user:  # you check if the user is the owner of the order
        appointment.delete() 
        return HttpResponseRedirect(reverse('profile'))
    else:
        raise PermissionDenied()


@login_required()
def view_appointment(request,id):
    user = request.user
    appointment = Appointment.objects.get(id=id)
    if appointment.user == user:  # you check if the user is the owner of the order
        date = appointment.date.strftime("%Y-%m-%d")
        timecode = appointment.on_date.strftime("%y%H%M%m%d")
        service = 'Obtention de documents médicaux'
        if appointment.service == 'فحص طبي' :
            service = 'Examen médical'
        elif appointment.service == 'تصوير بالاشعة':
            service = 'Radiographie médicale'
        elif appointment.service == 'اكمال علاج سابق':
            service = 'Poursuite du traitement précédent'
    else:
        raise PermissionDenied()
 

    context={
        'appointment':appointment,
        'user':user,
        'date':date,
        'timecode':timecode,
        'service':service
    }
    pdf = render_to_pdf('users/view_appointment.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

@login_required
def add_info(request):
    form = AddInfoForm
    context = {
        'form':form,
    }
    if request.method == 'POST':
        form = AddInfoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.notes = 'لاشيئ'
            instance.save()
            messages.success(request, 'تم تحديث المعلومات بنجاح')
            return redirect('profile')

    return render(request,'users/add_info.html',context)









#=======================register====================================================================
def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request,'تم نسجيلك بنجاح سجل دخولك الان')
            return redirect ('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'users/register.html', {'form': form})
    

