from django.shortcuts import render, redirect
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm


# Create your views here.

def home(request):
    return render (request, 'home.html')

def about(request):
    return render (request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render (request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
    })

def add_feeding(request, finch_id):
    submitted_form = FeedingForm(request.POST) #creates django version of req.body
    if submitted_form.is_valid():
        new_feeding = submitted_form.save(commit=False) #commit=false ensures it doesn't submit to db
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ('habitat', 'wingspan_inches')

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'