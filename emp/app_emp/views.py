# app_emp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee

def index(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(name__icontains=query)
    else:
        employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees, 'query': query})
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.salary = request.POST.get('salary')
        employee.age = request.POST.get('age')
        employee.birthday = request.POST.get('birthday')
        employee.remarks = request.POST.get('remarks')
        employee.save()
        return redirect('index')

    return render(request, 'app_emp/edit_employee.html', {'employee': employee})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('index')

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
        return redirect('index')

    return render(request, 'app_emp/add_employee.html')
