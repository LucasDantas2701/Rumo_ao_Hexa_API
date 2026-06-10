from django.db import models

# Create your models here.
class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Person(ModelBase):
    class ShirtSize(models.TextChoices):
        XS = 'XS', 'Extra Small'
        S = 'S', 'Small'
        M = 'M', 'Medium'
        L = 'L', 'Large'
        XL = 'XL', 'Extra Large'

    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    height = models.FloatField()
    weight = models.FloatField()
    foot_size = models.FloatField()
    shirt_size = models.CharField(max_length=2, choices=ShirtSize.choices, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Player(Person):

    class Position(models.TextChoices):
        GOALKEEPER = 'GK', 'Goalkeeper'
        DEFENDER = 'DF', 'Defender'
        MIDFIELDER = 'MF', 'Midfielder'
        FORWARD = 'FW', 'Forward'

    class Foot(models.TextChoices):
        LEFT = 'L', 'Left'
        RIGHT = 'R', 'Right'
        BOTH = 'B', 'Both'

    position = models.CharField(max_length=2, choices=Position.choices)
    foot_preference = models.CharField(max_length=1, choices=Foot.choices)
    number = models.IntegerField()
    team = models.ForeignKey("Team", on_delete=models.CASCADE, related_name='players')

class TeamGroup(ModelBase):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = 'Team Group'
        verbose_name_plural = 'Team Groups'
        
    def __str__(self):
        return self.name
    
class Team(ModelBase):
    name = models.CharField(max_length=255)
    federation = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    team_group = models.ForeignKey(TeamGroup, on_delete=models.CASCADE, related_name='teams', null=True, blank=True)
    def __str__(self):
        return self.name
    
class Coach(Person):
    team_group = models.ForeignKey(TeamGroup, on_delete=models.CASCADE, related_name='coaches')