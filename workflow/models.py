from django.db import models

class Workflow(models.Model):
    name = models.CharField(max_length=255)
    module = models.ForeignKey('settings.Module', on_delete=models.CASCADE)
    form = models.ForeignKey('design.Form', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ReviewField(models.Model):
    workflow = models.ForeignKey(Workflow, related_name='review_fields', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255)
    is_editable = models.BooleanField(default=False)

    def __str__(self):
        return self.field_name

class Reviewer(models.Model):
    workflow = models.ForeignKey(Workflow, related_name='reviewers', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.user.email} (Order: {self.order})"

class WorkflowOutcome(models.Model):
    workflow = models.ForeignKey(Workflow, related_name='outcomes', on_delete=models.CASCADE)
    outcome_type = models.CharField(max_length=255)
    action = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.outcome_type} - {self.action}"