# Generated by Django 2.0.7 on 2018-07-18 08:13

import app1.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0027_barcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('file', models.FileField(blank=True, null=True, upload_to=app1.models.generateFilename)),
                ('sec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Section')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]