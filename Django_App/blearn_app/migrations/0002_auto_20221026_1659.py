# Generated by Django 3.2.16 on 2022-10-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blearn_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]