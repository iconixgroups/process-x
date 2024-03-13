from django.db import models

class Process(models.Model):
    MODULE_CHOICES = [
        ('BPMN', 'Business Process Model and Notation'),
        ('UML', 'Unified Modeling Language')
    ]

    module = models.ForeignKey('settings.Module', on_delete=models.CASCADE, related_name='processes')
    process_type = models.CharField(max_length=4, choices=MODULE_CHOICES)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Step(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='steps')
    name = models.CharField(max_length=255)
    step_type = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    outcomes = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

class Form(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='forms')
    name = models.CharField(max_length=255)
    fields = models.JSONField()

    def __str__(self):
        return self.name

class Workflow(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='workflows')
    name = models.CharField(max_length=255)
    review_fields = models.JSONField()
    reviewers = models.JSONField()
    outcomes = models.JSONField()

    def __str__(self):
        return self.name