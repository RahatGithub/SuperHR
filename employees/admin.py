from django.contrib import admin
from .models import EmployeeProfile, Department

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'designation', 'department', 'date_of_joining')
    list_filter = ('department', 'designation')
    search_fields = ('user__username', 'user__email', 'designation')
    autocomplete_fields = ['user', 'department']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
