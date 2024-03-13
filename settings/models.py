from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    division = models.ForeignKey('company.Division', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Process(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    process_type = models.CharField(max_length=50)  # BPMN or UML
    details = models.JSONField()

    def __str__(self):
        return f"{self.module.name} - {self.process_type}"

class Form(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sections = models.JSONField()

    def __str__(self):
        return self.name

class Workflow(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    review_fields = models.JSONField()
    reviewers = models.JSONField()
    outcomes = models.JSONField()

    def __str__(self):
        return f"Workflow for {self.form.name}"