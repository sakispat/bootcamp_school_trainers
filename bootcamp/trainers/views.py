from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from .models import Trainer
from .forms import TrainerForm


# Home Page and List Table All Trainers
# Paginators 
def index(request):
    all_trainers = Trainer.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_trainers, 6)
    try:
        trainer_lists = paginator.page(page)
    except PageNotAnInteger:
        trainer_lists = paginator.page(1)
    except EmptyPage:
        trainer_lists = paginator.page(paginator.num_pages)
    context = { 'trainer_lists': trainer_lists }
    return render(request, 'trainers/index.html', context)


# Create Trainers Form
def create_trainer(request):
    if request.method == 'POST':
        trainerForm = TrainerForm(request.POST)
        if trainerForm.is_valid():
            trainerForm.save()
            messages.success(request, 'Registration was successfully')
            return redirect('home')
    else:
        trainerForm = TrainerForm()
    return render(request, 'trainers/create.html', { 'form': trainerForm })


# Edit/Update ID Trainer Form
def edit_trainer(request, id):
    if request.method == 'POST':
        trainer = Trainer.objects.get(id=id)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')

        Trainer.objects.filter(id=id).update(first_name=first_name)
        Trainer.objects.filter(id=id).update(last_name=last_name)
        Trainer.objects.filter(id=id).update(subject=subject)

        return redirect('home')
    else:
        trainer = Trainer.objects.get(id=id)
    return render(request, 'trainers/edit.html', { 'trainer': trainer })


# Delete ID Trainer
def delete_trainer(request, id):
    trainer = Trainer.objects.filter(id=id)
    trainer.delete()
    messages.success(request, 'Okay! Successfully delete the trainer')
    return redirect('home')


# Search Trainers in Table
def search_trainer(request):
    if request.method == 'POST':
        search = request.POST['search']
        search_trainer = Trainer.objects.filter(last_name__contains=search)
        if not search_trainer:
            messages.error(request, 'The search for an instructor you are looking for was not successfully try again')
        else:
            messages.success(request, 'The search for trainer what you were looking for was successfully')
        return render(request, 'trainers/search.html', { 'search': search, 'search_trainer': search_trainer })
    else:
        return render(request, 'trainers/search.html')

