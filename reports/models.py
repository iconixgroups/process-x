from django.db import models

class Report(models.Model):
    module = models.ForeignKey('settings.Module', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    def __str__(self):
        return self.name

class ReportField(models.Model):
    report = models.ForeignKey(Report, related_name='fields', on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=50)
    field_value = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Report Field'
        verbose_name_plural = 'Report Fields'

    def __str__(self):
        return f"{self.field_name} ({self.field_type})"

class ReportStatus(models.Model):
    report = models.ForeignKey(Report, related_name='statuses', on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Report Status'
        verbose_name_plural = 'Report Statuses'

    def __str__(self):
        return f"{self.report.name} - {self.status}"