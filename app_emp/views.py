from django.contrib.auth import login, authenticate , logout
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'index.html', {'error': 'Invalid username or password'})
    return render(request, 'index.html')

def dashboard(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(name__icontains=query)
    else:
        employees = Employee.objects.all()
    return render(request, 'dashboard.html', {'employees': employees, 'query': query})


def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.salary = request.POST.get('salary')
        employee.age = request.POST.get('age')
        employee.birthday = request.POST.get('birthday')
        employee.remarks = request.POST.get('remarks')
        employee.save()
        return redirect('dashboard')

    return render(request, 'app_emp/edit_employee.html', {'employee': employee})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('dashboard')

def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        salary = request.POST.get('salary')
        age = request.POST.get('age')
        birthday = request.POST.get('birthday')
        remarks = request.POST.get('remarks')

        Employee.objects.create(
            name=name,
            salary=salary,
            age=age,
            birthday=birthday,
            remarks=remarks
        )
        return redirect('dashboard')

    return render(request, 'app_emp/add_employee.html')


def logout_view(request):
    logout(request)
    return redirect('index')  # or redirect wherever you want
