# Generated by Django 4.2.6 on 2023-11-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_remove_student_subject_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
