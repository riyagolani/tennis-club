# Generated by Django 4.1.6 on 2023-02-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_alter_member_proficiency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
