from django.db import models
from django.db.models.base import ModelState
#
from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField


class Habilidades(models.Model):
      Habilidad = models.CharField('habilidad', max_length=50)

      class Meta:
        verbose_name = 'habilidad'
        verbose_name_plural = 'Habilidades de Empleados'

      def __str__(self):
        return str(self.id) + '-' + self.Habilidad

# Create your models here.
class Empleado(models.Model):
    """Modelo para tabla empleado """
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),

    )
    # Contador
    # Administrador 
    # Economista
    # otro    
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres completos',
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=1, choices= JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades =  models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()    
    #FIELDNAME = models.ImageField(, upload_to=None, h  eight_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = 'Personal de la empresa'
        verbose_name_plural = 'Datos Empleado'
        ordering = ['last_name','first_name']
        unique_together = ['first_name', 'last_name']




    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
        
