from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import logout,authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import VotingForm
from .models import VotingData, VoterDataAccess
from django.core.paginator import Paginator
# Create your views here.
@login_required(login_url="login")
def index(request):
    if request.method == 'POST':
        form =VotingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=VotingForm()
    return render(request,"index.html",{"form":form})

@login_required(login_url="login")
def view(request):
    if request.method == 'POST':
        booth_number_filter = request.POST.get('booth_number_filter')
        booth_name_filter = request.POST.get('booth_name_filter')
        
        # Retrieve all data initially
        filtered_data = VotingData.objects.all()

        # Apply filters if provided
        if booth_number_filter:
            filtered_data = filtered_data.filter(polling_booth_number__icontains=booth_number_filter)
        if booth_name_filter:
            filtered_data = filtered_data.filter(polling_booth_name__icontains=booth_name_filter)

        pagination = Paginator(filtered_data, 10)
        page_number = request.GET.get('page')
        form = pagination.get_page(page_number)
    else:
        # If it's not a POST request, show all data
        data = VotingData.objects.all()
        pagination = Paginator(data, 10)
        page_number = request.GET.get('page')
        form = pagination.get_page(page_number)

    return render(request, "view.html", {"form": form})

@login_required(login_url="login")
def delete(request, id):
    if request.method == "POST":
        # Get the VotingData instance by its primary key (id)
        voting_data = VotingData.objects.get(pk=id)
        # Delete the instance
        voting_data.delete()
        # Redirect to the home page or any other appropriate URL
        return HttpResponseRedirect("/")
    
# def filter(request):
#     if request.method=='POST':
#         polling_booth_number=request.POST['polling_booth_number']
#         polling_booth_name=request.POST['polling_booth_name']
#         emps =VotingData.objects.all()
#         if polling_booth_number:
#             emps=VotingData.filter(Q(polling_booth_number=polling_booth_number))

#         if polling_booth_name:
#             emps=VotingData.filter(Q(polling_booth_name__icontains=polling_booth_name))

#         context ={
#             'emps':emps
#          }
#         return render(request,'view.html',context)

#     elif request.method=='GET':
#         return render(request,'filter.html')

#     else:
#         return HttpResponse("an exception occured")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("view")  # Assuming you have defined the 'index' URL pattern in your Django project's urls.py
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")  # Optional: You can add a logout message
    return redirect('login')