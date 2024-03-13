from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    registration_date = models.DateField()
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    owners = models.JSONField()  # This field can store owner details as a JSON

    def __str__(self):
        return self.name

class Division(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='divisions')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class User(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='users')
    employee_code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    active_status = models.BooleanField(default=True)
    assignments = models.JSONField()  # This field can store assignments as a JSON

    def __str__(self):
        return self.name
