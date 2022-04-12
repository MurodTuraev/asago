# Generated by Django 4.0.2 on 2022-03-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0011_rename_drivers_firstname_limitedjismoniy_drivers_one_lastname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractJson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.JSONField(blank=True, null=True)),
                ('insuranceFormUuid', models.CharField(blank=True, max_length=512, null=True)),
                ('policy_seria', models.CharField(blank=True, max_length=512, null=True)),
                ('policy_number', models.CharField(blank=True, max_length=512, null=True)),
                ('policy_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Полис',
                'verbose_name_plural': 'Полисв',
                'ordering': ['-created_at'],
            },
        ),
    ]
