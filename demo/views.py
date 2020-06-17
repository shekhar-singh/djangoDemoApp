from django.shortcuts import render, redirect
from .models import Details
from .forms import DetailForm
# Create your views here.
def index(request):
    persons = Details.objects.all()
    return render(request, 
                  'demo_list.html', 
                  {'persons' : persons } )

def new_detail(request):
    if request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = DetailForm()
    return render(request, 'detail_form.html', {'form': form})