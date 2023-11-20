from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Task(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_CHOICES = [
        (HIGH, 'Haute'),
        (MEDIUM, 'Moyenne'),
        (LOW, 'Faible'),
    ]
    
    title = models.CharField(_("Titre"), max_length=100)
    priority = models.CharField(_("Priorité"), max_length=1, choices=PRIORITY_CHOICES, default=MEDIUM)
    completed = models.BooleanField(_("Complétée"), default=False)
    
    def __str__(self):
        return self.title