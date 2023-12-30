from django.shortcuts import render, redirect, get_object_or_404
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
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Create trainer was successfully')
            return redirect('home')
    form = TrainerForm()
    context = { 'form': form }
    return render(request, 'trainers/create.html', context)


# Edit/Update ID Trainer Form
def update_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update trainer was successfully')
            return redirect('home')
    form = TrainerForm()
    context = { 'form': form, 'trainer': trainer }
    return render(request, 'trainers/edit.html', context)


# Delete ID Trainer
def delete_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    trainer.delete()
    messages.success(request, 'Okay! Successfully delete the trainer')
    return redirect('home')


# Search Trainers in Table
def search_trainer(request):
    query = request.POST.get('q')
    results = []
    if query:
        results = Trainer.objects.filter(last_name__icontains=query)
        if not results:
            messages.error(request, 'The search for an instructor you are looking for was not successfully try again')
        else:
            messages.success(request, 'The search for trainer what you were looking for was successfully')
    context = {'results': results, 'query': query}
    return render(request, 'trainers/search.html', context)
