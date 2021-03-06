# Generated by Django 4.0.5 on 2022-06-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EditPortfolio', '0003_alter_heromodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heromodel',
            name='before_description',
            field=models.CharField(blank=True, default='I create stuff for the Internet.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='heromodel',
            name='before_name',
            field=models.CharField(blank=True, default='Hi,my name is..', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='heromodel',
            name='description',
            field=models.CharField(blank=True, default='I am a Fullstack Web Devoloper From Bangladesh.I use React + Django stack.Currently open for work 😀', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='heromodel',
            name='fullname',
            field=models.CharField(blank=True, default='FirstName LastName', max_length=100, null=True),
        ),
    ]
