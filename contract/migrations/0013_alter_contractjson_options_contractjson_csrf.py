# Generated by Django 4.0.2 on 2022-03-03 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0012_contractjson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contractjson',
            options={'verbose_name': 'Полис', 'verbose_name_plural': 'Полисв'},
        ),
        migrations.AddField(
            model_name='contractjson',
            name='csrf',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
