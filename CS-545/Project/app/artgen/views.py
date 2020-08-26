from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .forms import RegisterForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtForm
from .forms import CustomUserCreationForm
from .genart import *

from .models import * 

from django.http import HttpResponseRedirect



def index(request):
    artlist = Art.objects.order_by('-date_created')[:5]
    context = {
        'artlist': artlist,
    }

    return render(request, 'artgen/index.html', context)

def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    return render(request, 'artgen/user.html', {'user': user})

# def art_like(request, art_id):
#     new_like, created = Like.objects.get_or_create(user=request.user, art=art_id)
#     if not created:
#         # the user already liked this picture before -- unlike the photo
#         new_like.delete()
#         pass
#     else:
#         # the user hasnt liked this picture before -- add like
#         new_like.save()

def art_like(request, art_id):
    print("TEST")
    if request.method == "POST":
        art = get_object_or_404(Art, id=art_id)

        like, created = Like.objects.get_or_create(user=request.user, art=art)

        if created: 
            art.number += 1 
            art.save()
        else: 
            like.delete()
            art.number -= 1 
            art.save()

    return redirect("/")

        # like, created = Like.objects.get_or_create(user=request.user, art=art_id)
        # # new_like, created = Like.objects.get_or_create(user=request.user, art=art_id)
        # if not created:
        # #     # the user already liked this picture before -- unlike the photo
        #     new_like.delete()
        #     art.number += 1 
        #     art.save()
        #     pass
        # else:
        # #     # the user hasnt liked this picture before -- add like
        #     new_like.save()
        #     art.number -= 1 
        #     art.save()
        #     pass


def art(request, art_id): 
    art = get_object_or_404(Art, pk=art_id)

    return render(request, 'artgen/art.html', {'art': art})

def art_new(request):
    if request.method == "POST":
        form = ArtForm(request.POST, request.FILES)

        if form.is_valid():
            art = form.save(commit=True)
            art.creator = request.user
            art.date_created = timezone.now()
            save_path = "/media/generated/" + art.title + ".jpg"
            genImage(art.image_1.file.name, art.image_2.file.name, "." + save_path)
            art.filepath = save_path 
            art.save()

            like = Like(user=request.user, art=art)
            like.save()

            return redirect('art', art_id=art.id)
    else: 
        form = ArtForm()

    return render(request, 'artgen/art_edit.html', {'form': form})


def art_edit(request, pk):
    art = get_object_or_404(Art, pk=pk)
    if request.method == "POST":
        form = ArtForm(request.POST, instance=art)
        if form.is_valid():
            art = form.save(commit=False)
            art.creator = request.user
            art.date_created = timezone.now()
            art.save()
            return redirect('art', pk=art.pk)
        # TODO 
        # Run Function for AI
    else:
        form = ArtForm(instance=art)
    return render(request, 'artgen/art_edit.html', {'form': form})

def art_delete(request, art_id=None):
    art = Art.objects.get(id=art_id)
    art.delete()
    return redirect('index')

# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
