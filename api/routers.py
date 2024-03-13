from django.urls import path
from .views import (
    SocialSignInView, EmailRegistrationView, EmailVerificationView,
    CompanyRegistrationView, AddDivisionView, AddDepartmentView, AddProjectView, AddUserView,
    AddModuleView, UpdateModuleView, DesignProcessView, CreateFormView, CreateWorkflowView,
    FetchDashboardDataView, GenerateReportView, PublishModuleView
)

urlpatterns = [
    path('auth/social', SocialSignInView.as_view(), name='social_sign_in'),
    path('auth/register', EmailRegistrationView.as_view(), name='email_register'),
    path('auth/verify', EmailVerificationView.as_view(), name='email_verify'),
    path('company', CompanyRegistrationView.as_view(), name='company_register'),
    path('company/division', AddDivisionView.as_view(), name='add_division'),
    path('company/department', AddDepartmentView.as_view(), name='add_department'),
    path('company/project', AddProjectView.as_view(), name='add_project'),
    path('company/user', AddUserView.as_view(), name='add_user'),
    path('settings/module', AddModuleView.as_view(), name='add_module'),
    path('settings/module/<str:moduleId>', UpdateModuleView.as_view(), name='update_module'),
    path('design/process', DesignProcessView.as_view(), name='design_process'),
    path('design/form', CreateFormView.as_view(), name='create_form'),
    path('design/workflow', CreateWorkflowView.as_view(), name='create_workflow'),
    path('dashboard/<str:moduleId>', FetchDashboardDataView.as_view(), name='fetch_dashboard_data'),
    path('reports/<str:moduleId>', GenerateReportView.as_view(), name='generate_report'),
    path('publish/module/<str:moduleId>', PublishModuleView.as_view(), name='publish_module'),
]