# Generated by Django 4.2.6 on 2024-10-07 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_department_name_employee_attendance_employee_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='department',
            new_name='department_id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(default='12345', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=120),
        ),
    ]
