# Generated by Django 4.0.4 on 2022-05-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0008_student_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default='Undefined', max_length=100),
        ),
    ]