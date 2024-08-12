from django.shortcuts import render
from .models import Social
from .form import SocialForm
from django.shortcuts import get_object_or_404,redirect
# Create your views here.
def socialHomeView(request):
    return render(request, 'index.html')



def socialListView(request):
    socials=Social.objects.all().order_by('-created_at')
    return render(request, 'social_list.html', {'socials':socials})

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


def socialDeleteView(request, pk):
    social=get_object_or_404(Social, pk=pk , user=request.user)
    if request.method == 'POST':
        social.delete()
        return redirect('socialListView')
    return render(request, 'social_delete.html', {'social':social})
    