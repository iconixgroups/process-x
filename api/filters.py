from django_filters import rest_framework as filters
from company.models import Company, Division, Department, Project
from settings.models import Module
from design.models import Process, Form
from workflow.models import Workflow
from reports.models import Report

class CompanyFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    code = filters.CharFilter(lookup_expr='icontains')
    registration_date = filters.DateFromToRangeFilter()

    class Meta:
        model = Company
        fields = ['name', 'code', 'registration_date']

class DivisionFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    status = filters.BooleanFilter()

    class Meta:
        model = Division
        fields = ['name', 'status']

class DepartmentFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    status = filters.BooleanFilter()

    class Meta:
        model = Department
        fields = ['name', 'status']

class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    status = filters.BooleanFilter()

    class Meta:
        model = Project
        fields = ['name', 'status']

class ModuleFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    company_code = filters.CharFilter(field_name='company__code', lookup_expr='exact')
    division_code = filters.CharFilter(field_name='division__code', lookup_expr='exact')

    class Meta:
        model = Module
        fields = ['name', 'company_code', 'division_code']

class ProcessFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    type = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Process
        fields = ['name', 'type']

class FormFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Form
        fields = ['name']

class WorkflowFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Workflow
        fields = ['name']

class ReportFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    module_id = filters.NumberFilter(field_name='module__id', lookup_expr='exact')

    class Meta:
        model = Report
        fields = ['name', 'module_id']