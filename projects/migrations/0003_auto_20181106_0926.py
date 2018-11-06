# Generated by Django 2.0.4 on 2018-11-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20181105_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Projecttype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='devtype',
            field=models.ForeignKey(null=True, on_delete=False, to='projects.Devtype'),
        ),
        migrations.AddField(
            model_name='project',
            name='projecttype',
            field=models.ForeignKey(null=True, on_delete=False, to='projects.Projecttype'),
        ),
    ]