```python
from django.db import models

class DashboardData(models.Model):
    moduleId = models.CharField(max_length=255)
    dataSubmissions = models.IntegerField(default=0)
    pending = models.IntegerField(default=0)
    approved = models.IntegerField(default=0)
    rejected = models.IntegerField(default=0)

    def __str__(self):
        return f"Dashboard Data for Module: {self.moduleId}"
```