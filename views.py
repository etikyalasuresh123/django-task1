from django.shortcuts import render,redirect
from website1.forms import EmployeeForm,SignUpForm
from website1.forms import EmployeeForm
from website1.models import Employee

from django.http import HttpResponseRedirect

def show_view(request):
	employees=Employee.objects.all()
	return render(request,'website1/index.html',{'employees':employees})

def insert_view(request):
	form=EmployeeForm()
	if request.method=='POST':
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	return render(request,'website1/insert.html',{'form':form})


def update_view(request,id):
	employee=Employee.objects.get(id=id)
	if request.method=='POST':
		form=EmployeeForm(request.POST,instance=employee)
		if form.is_valid():
			form.save()
			return redirect('/')
	return render(request,'website1/update.html',{'employee':employee})   


def delete_view(request,id):
	employee=Employee.objects.get(id=id)
	employee.delete()
	return redirect('/')


def signup_view(request):
	form=SignUpForm()
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
			return HttpResponseRedirect('/accounts/login')
	return render(request,'website1/signup.html',{'form':form})   
