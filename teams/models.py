from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=30)
    titles = models.IntegerField()
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3, unique=True)
    founded_at = models.DateField()

    def __repr__(self):
        return f'<[{self.id}] {self.name} {self.fifa_code}'
