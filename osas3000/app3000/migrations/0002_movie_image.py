# Generated by Django 4.1.7 on 2023-04-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3000', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, upload_to='app3000/movies'),
        ),
    ]
