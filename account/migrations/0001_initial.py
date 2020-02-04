# Generated by Django 3.0.2 on 2020-01-24 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='supervisors', to='project.Groups')),
                ('supervisor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supervisors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='project.Department')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='project.Groups')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hod', to='project.Department')),
                ('hod_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hod', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dean_name', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='dean', to=settings.AUTH_USER_MODEL)),
                ('school_id', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='dean', to='project.School')),
            ],
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='coordinator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
