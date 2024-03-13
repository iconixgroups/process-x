from rest_framework import serializers
from user.models import User
from company.models import Company, Division, Department, Project
from settings.models import Module
from design.models import Process, Form
from workflow.models import Workflow
from reports.models import Report
from publish.models import Publication

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'is_active']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'companyName', 'aliasName', 'companyCode', 'registrationDate', 'address', 'contactNumber', 'email', 'website', 'owners']

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ['id', 'company', 'divisionCode', 'divisionName', 'activeStatus']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'division', 'departmentCode', 'departmentName', 'activeStatus']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'division', 'projectCode', 'projectName', 'activeStatus']

class UserAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'company', 'employeeCode', 'employeeName', 'activeStatus', 'assignments']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'moduleName', 'company', 'division']

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['id', 'moduleId', 'processType', 'details']

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id', 'process', 'formName', 'sections']

class WorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = ['id', 'form', 'reviewFields', 'reviewers', 'outcomes']

class DashboardDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'dataSubmissions', 'statuses']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'moduleId', 'reportData']

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'moduleId', 'publish']