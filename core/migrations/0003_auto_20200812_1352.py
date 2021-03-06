# Generated by Django 3.1 on 2020-08-12 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200812_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='status',
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('réservée', 'réservée'), ('terminé', 'terminé'), ('rejeté', 'rejeté')], default='réservée', max_length=200)),
                ('notes', models.TextField(max_length=700)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.appointment')),
            ],
        ),
    ]
