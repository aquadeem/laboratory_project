# Generated by Django 4.0.4 on 2022-05-02 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0012_alter_student_social_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='social_url',
            field=models.URLField(default=0, max_length=100),
        ),
    ]
