# Generated by Django 5.0.1 on 2024-01-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogone', '0014_contact_ism'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='ism',
            field=models.CharField(max_length=50),
        ),
    ]
