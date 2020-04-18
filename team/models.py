from django.db import models


class Team(models.Model):

    title = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.title


class Committee(models.Model):

    title = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class OfficeBearer(models.Model):

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
