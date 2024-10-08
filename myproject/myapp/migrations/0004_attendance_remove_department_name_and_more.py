# Generated by Django 4.2.6 on 2024-10-05 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_department_parent_department_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('PRESENT', 'Present'), ('ABSENT', 'Absent'), ('LATE', 'Late')], max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('CITY_ACCOUNTANT', "CITY ACCOUNTANT'S OFFICE"), ('CITY_AGRICULTURE', 'CITY AGRICULTURE OFFICE'), ('CITY_ASSESSOR', "CITY ASSESSOR'S OFFICE"), ('CITY_BUDGET', 'CITY BUDGET OFFICE'), ('CITY_ENGINEERING', 'CITY ENGINEERING OFFICE'), ('CITY_GENERAL_SERVICES', 'CITY GENERAL SERVICES OFFICE'), ('CITY_HEALTH', 'CITY HEALTH DEPARTMENT'), ('CITY_TREASURER', "CITY TREASURER'S OFFICE"), ('CITY_DISASTER_RRM', 'CITY DISASTER RRM OFFICE'), ('ORMOC_WATERWORKS', 'ORMOC WATERWORKS OFFICE'), ('SPORTS', 'SPORTS OFFICE')], default='CITY_ACCOUNTANT', max_length=100),
        ),

        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_date', models.DateField(auto_now_add=True)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_records', to='myapp.attendance')),
                
            ],
        ),

    ]
