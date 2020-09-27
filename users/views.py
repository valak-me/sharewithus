from django.shortcuts import render, redirect
from .forms import  UserRegisterForm,Userupdateform,profileupdateform
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form =  UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'your account has been created successfully  {username} enter detailes for login')
            return redirect('login')


    else:
        form =  UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_update = Userupdateform(request.POST, instance=request.user)
        p_update = profileupdateform(request.POST,
                                     request.FILES,
                                instance=request.user.profile)
        if u_update.is_valid() and p_update.is_valid():
            u_update.save()
            p_update.save()
            messages.success(request,
                             f'your account has been updated')
            return redirect('profile')
    else:
        u_update = Userupdateform(instance=request.user)
        p_update = profileupdateform(instance=request.user)

    context={
     'u_update':u_update,
     'p_update':p_update
    }
    return render(request, 'users/profile.html', context)


