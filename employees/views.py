from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Department, EmployeeProfile
from .forms import DepartmentForm

# custom test for checking if the user is 'admin'
def is_admin(user):
    return user.is_superuser


@login_required
def department_list(request):
    departments = Department.objects.all()
    form = DepartmentForm()

    if request.method == 'POST' and request.user.is_superuser:
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')

    return render(request, 'employees/department_list.html', {
        'departments': departments,
        'form': form,
    })


@login_required
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    employees = EmployeeProfile.objects.filter(department=department)
    return render(request, 'employees/department_detail.html', {'department': department, 'employees': employees})


@login_required
@user_passes_test(is_admin)
def department_add(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    return redirect('department_list')


@login_required
@user_passes_test(is_admin)
def department_edit(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=dept)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=dept)
    return render(request, 'employees/department_edit.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def department_delete(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        dept.delete()
        return redirect('department_list')
    return render(request, 'employees/department_delete.html', {'department': dept})
