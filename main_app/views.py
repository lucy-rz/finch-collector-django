from django.shortcuts import render, redirect
from .models import Finch, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
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
    id_list = finch.toys.all().values_list('id')
    missing_toys = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'toys': missing_toys,
    })

def assoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)

def add_feeding(request, finch_id):
    submitted_form = FeedingForm(request.POST) #creates django version of req.body
    if submitted_form.is_valid():
        new_feeding = submitted_form.save(commit=False) #commit=false ensures it doesn't submit to db
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


#finch classes
class FinchCreate(CreateView):
    model = Finch
    fields = ['breed', 'habitat', 'color', 'wingspan_inches']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ('habitat', 'wingspan_inches')

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

#toy classes
class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys'