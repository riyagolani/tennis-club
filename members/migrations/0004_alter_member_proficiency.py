# Generated by Django 4.1.6 on 2023-02-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_member_proficiency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='proficiency',
            field=models.CharField(choices=[('Beginner', '1'), ('Intermediate', '2'), ('Expert', '3')], default='Intermediate', max_length=20),
        ),
    ]
