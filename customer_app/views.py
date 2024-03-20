
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib import messages
from .forms import SignUpForm,CustomerForm
from .models import Customer



def update_view(request,pk):
    record_instance=Customer.objects.get(pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST,instance=record_instance)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Customer Details Successfully")
            return redirect('retrieve-customer')
        else:
            messages.success("Error !Please Enter Correct Customer Detail")
    else:
        form = CustomerForm(instance=record_instance)
        return render(request,"update.html",{'form':form})



def delete_view(request,pk):
    customer = Customer.objects.get(pk=pk)
    customer.delete()
    messages.success(request,"Deleted Record Successfully")
    return redirect('retrieve-customer')
    
    
def customer_detail(request,pk):
    customer=Customer.objects.get(pk=pk)
    return render(request,"customer_detail.html",{'customer':customer})    


def retrieve_customer(request):
    customer = Customer.objects.all()
    return render(request,"retrieve_customer.html",{'customer':customer})


def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Customer Record Successfully Added")
            return redirect("home")
        else:
            messages.success(request,"Your has Error Please Enter Correct Data")
            return redirect("home")
    else:
        form= CustomerForm()
        return render(request,"create.html",{'form':form})
    




def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # for authentication 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have been successfully Registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})



def home_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged In")
            return redirect("home")
        else:
            messages.success(request,"There was an Error logging In")
            return redirect('home')
    return render(request,"homepage.html")

def logout_user(request):
    logout(request)
    messages.success(request,"You have been successfully logout")
    return redirect('home')

