# Generated by Django 4.2.6 on 2023-12-01 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0010_mobiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.PositiveIntegerField()),
                ('course', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=30)),
            ],
        ),
    ]