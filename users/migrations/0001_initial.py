# Generated by Django 3.1 on 2020-08-11 10:36

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
                ('first_name', models.CharField(max_length=200, verbose_name='الاسم')),
                ('last_name', models.CharField(max_length=200, verbose_name='اللقب')),
                ('phone', models.BigIntegerField(null=True, verbose_name='الهاتف')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='العنوان')),
                ('date_of_birth', models.DateField(verbose_name='تاريخ الميلاذ')),
                ('sex', models.CharField(choices=[('دكر', 'دكر'), ('انثى', 'انثى')], max_length=200, verbose_name='الجنس')),
                ('notes', models.TextField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
