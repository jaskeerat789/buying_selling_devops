# Generated by Django 2.2.10 on 2020-05-09 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200510_0021'),
    ]

    operations = [
        migrations.AlterField(model_name='profile', name='year', field=models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth')], max_length=1),),
    ]
