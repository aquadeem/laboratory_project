# Generated by Django 4.0.4 on 2022-05-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0010_alter_student_social_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='social_url',
            field=models.URLField(default=None, max_length=100),
        ),
    ]
