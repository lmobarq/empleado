# Generated by Django 3.2.7 on 2022-02-23 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_alter_empleado_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombres completos'),
        ),
    ]