# Generated by Django 4.0.5 on 2022-06-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EditPortfolio', '0010_socialmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='heromodel',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='heromodel',
            name='github',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='heromodel',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='heromodel',
            name='mail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='socialModel',
        ),
    ]
