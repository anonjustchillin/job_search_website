# Generated by Django 4.2.13 on 2024-05-13 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_applyjob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(blank=True, choices=[('Remote', 'Remote'), ('On-site', 'On-site'), ('Hybrid', 'Hybrid')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='industry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='job.industry'),
        ),
        migrations.AddField(
            model_name='job',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='job.region'),
        ),
    ]
