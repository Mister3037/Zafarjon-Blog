# Generated by Django 5.0.1 on 2024-01-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogone', '0011_rename_urls_homepostnews_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('xabar', models.TextField()),
            ],
        ),
    ]
