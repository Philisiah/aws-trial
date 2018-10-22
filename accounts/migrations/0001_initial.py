# Generated by Django 2.0.4 on 2018-10-22 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, choices=[('recruiter', 'RECRUITER'), ('developer', 'DEVELOPER')], max_length=30, null=True)),
                ('stage', models.CharField(choices=[('profile_type_selection', 'profile_type_selection'), ('recuiter_filling_details', 'recuiter_filling_details'), ('developer_filling_details', 'developer_filling_details'), ('complete', 'complete')], default='profile_type_selection', max_length=100)),
                ('profile_photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('github_repo', models.URLField(blank=True, null=True)),
                ('programming_languages', models.CharField(blank=True, choices=[('python', 'Python')], max_length=30, null=True)),
                ('frameworks', models.CharField(blank=True, choices=[('django', 'Django')], max_length=30, null=True)),
                ('years', models.CharField(blank=True, choices=[('1-2', '1-2'), ('2-4', '2-4'), ('4-above', '4-above')], max_length=30, null=True)),
                ('company', models.CharField(blank=True, max_length=140, null=True)),
                ('job_role', models.CharField(blank=True, max_length=140, null=True)),
                ('industry', models.CharField(blank=True, max_length=80, null=True)),
                ('staff_size', models.IntegerField(blank=True, null=True)),
                ('company_url', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
