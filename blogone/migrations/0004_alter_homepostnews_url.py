# Generated by Django 5.0.1 on 2024-01-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogone', '0003_alter_homepostnews_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepostnews',
            name='url',
            field=models.URLField(default=True),
        ),
    ]
