# Generated by Django 3.0.5 on 2020-04-02 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='myurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=25, unique=True),
        ),
    ]
