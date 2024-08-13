from django.shortcuts import render
from .models import Social
from .forms import SocialForm,UserRegisterForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def socialHomeView(request):
    return render(request, 'index.html')



def socialListView(request):
    socials=Social.objects.all().order_by('-created_at')
    #print(socials)
    return render(request, 'social_list.html', {'socials':socials})
@login_required
def socialCreateView(request):
    if request.method == 'POST':
        form=SocialForm(request.POST, request.FILES)
        if form.is_valid():
            social=form.save(commit=False)
            social.user=request.user
            social.save()
            return redirect('socialListView')
    else:
        form=SocialForm()
    return render(request, 'social_form.html', {'form':form})

@login_required
def socialUpdateView(request, pk):
    social=get_object_or_404(Social, pk=pk, user=request.user)
    if request.method == 'POST':
        form=SocialForm(request.POST, request.FILES, instance=social)
        if form.is_valid():
            social=form.save(commit=False)
            social.user=request.user
            social.save()
            return redirect('socialListView')
    else:
        form=SocialForm(instance=social)
    return render(request, 'social_form.html', {'form':form})

@login_required
def socialDeleteView(request, pk):
    social=get_object_or_404(Social, pk=pk , user=request.user)
    if request.method == 'POST':
        social.delete()
        return redirect('socialListView')
    return render(request, 'social_delete.html', {'social':social})
    
def registerView(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('socialListView')
    else:
        form=UserRegisterForm()
    return render(request, 'registration/register.html', {'form':form})