from rest_framework.throttling import SimpleRateThrottle

class UserSignUpRateThrottle(SimpleRateThrottle):
    scope = 'user_signup'

    def get_cache_key(self, request, view):
        if request.method == 'POST':
            ident = request.data.get('email') or self.get_ident(request)
            return self.cache_format % {
                'scope': self.scope,
                'ident': ident
            }

class CompanyRegistrationRateThrottle(SimpleRateThrottle):
    scope = 'company_registration'

    def get_cache_key(self, request, view):
        if request.method == 'POST':
            ident = request.data.get('companyCode') or self.get_ident(request)
            return self.cache_format % {
                'scope': self.scope,
                'ident': ident
            }

class ModuleCreationRateThrottle(SimpleRateThrottle):
    scope = 'module_creation'

    def get_cache_key(self, request, view):
        if request.method == 'POST':
            ident = request.data.get('moduleName') or self.get_ident(request)
            return self.cache_format % {
                'scope': self.scope,
                'ident': ident
            }

class ProcessDesignRateThrottle(SimpleRateThrottle):
    scope = 'process_design'

    def get_cache_key(self, request, view):
        if request.method == 'POST':
            ident = request.data.get('moduleId') or self.get_ident(request)
            return self.cache_format % {
                'scope': self.scope,
                'ident': ident
            }

class FormCreationRateThrottle(SimpleRateThrottle):
    scope = 'form_creation'

    def get_cache_key(self, request, view):
        if request.method == 'POST':
            ident = request.data.get('formName') or self.get_ident(request)
            return self.cache_format % {
                'scope': self.scope,
                'ident': ident
            }

class WorkflowManagementRateThrottle(SimpleRateThrottle):
    scope = 'workflow_management'

    def get_cache_key(self, request, view):
        if request.method == 'POST':
            ident = request.data.get('formId') or self.get_ident(request)
            return self.cache_format % {
                'scope': self.scope,
                'ident': ident
            }

class DashboardAccessRateThrottle(SimpleRateThrottle):
    scope = 'dashboard_access'

    def get_cache_key(self, request, view):
        if request.method == 'GET':
            ident = self.get_ident(request)
            return self.cache_format % {
                'scope': self.scope,
                'ident': ident
            }

class ReportGenerationRateThrottle(SimpleRateThrottle):
    scope = 'report_generation'

    def get_cache_key(self, request, view):
        if request.method == 'GET':
            ident = self.get_ident(request)
            return self.cache_format % {
                'scope': self.scope,
                'ident': ident
            }