# Generated by Django 3.1.1 on 2020-09-29 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
            ],
            options={
                'db_table': 'mentor_data',
            },
        ),
        migrations.CreateModel(
            name='TimeMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'hours_data',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('student_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('class_standing', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('PG', 'Post Graduate'), ('GR', 'Graduate')], max_length=2)),
                ('DAS_mentor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to='api.mentor')),
                ('hour_sheet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.timemaster')),
            ],
            options={
                'db_table': 'student_data',
            },
        ),
        migrations.CreateModel(
            name='HourInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_activity', models.DateField()),
                ('number_of_hours', models.FloatField()),
                ('description_of_activity', models.TextField()),
                ('type_of_hour', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('PG', 'Post Graduate'), ('GR', 'Graduate')], max_length=3)),
                ('learning_goal', models.CharField(choices=[('CONFIDENCE', 'Gain confidence and skills to identify, define and tackle complex problems that impact communities and transcend borders.'), ('EMPATHY', 'Value empathy, understanding and responsiveness to diverse others in their work and public roles.'), ('EXPLORE', 'Explore and take action on solutions to real-world problems that fulfill the goals of social impact, financial viability, and environmental sustainability.')], max_length=10)),
                ('activity_description', models.TextField()),
                ('time_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.timemaster')),
            ],
        ),
    ]
