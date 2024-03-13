from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=255)
    company_code = models.CharField(max_length=50)
    division_code = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ModulePublication(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='publications')
    published_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.module.name} - {'Published' if self.is_active else 'Unpublished'}"