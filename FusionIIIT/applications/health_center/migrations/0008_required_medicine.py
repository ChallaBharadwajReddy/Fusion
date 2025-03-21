# Generated by Django 3.1.5 on 2024-07-21 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health_center', '0007_auto_20240719_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Required_medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('threshold', models.IntegerField()),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.all_medicine')),
            ],
        ),
    ]
