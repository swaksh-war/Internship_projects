from django.db import models
# Create your models here.
class Crimecase(models.Model):
    CASE_CAT = (
        ('robbery', 'Robbery'),
        ('murder', 'Murder'),
        ('kidnapping', 'Kidnapping'),
        ('theft', 'Theft'),
        ('threat', 'Threat'),
        ('burglary', 'Burglary')
    )
    case_name = models.CharField(max_length=200, default='Name of the crime scene', blank=False)
    case_desc = models.TextField(default='Add description here')
    case_date = models.DateField()
    case_loc = models.CharField(default='Delhi', max_length=70)
    case_cover = models.FileField(upload_to='media/case', default='media/case/n.png')
    case_category = models.CharField(default='Robbery', choices= CASE_CAT, max_length=50)
    case_criminal = models.ForeignKey('criminal.Criminal', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.case_name)
