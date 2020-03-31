# Generated by Django 3.0.4 on 2020-03-31 10:44

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='codeapp.USER')),
                ('career', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('portfolioweb', models.URLField()),
                ('location', models.CharField(max_length=30)),
                ('skills', models.CharField(max_length=500)),
                ('githublink', models.URLField(blank=True, null=True)),
                ('fblink', models.URLField(blank=True, null=True)),
                ('instalink', models.URLField(blank=True, null=True)),
                ('tweetlink', models.URLField(blank=True, null=True)),
                ('youtubelink', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=30)),
                ('aff_company', models.CharField(max_length=30)),
                ('loc_company', models.CharField(max_length=30)),
                ('frm_date', models.DateField()),
                ('to_date', models.DateField()),
                ('job_des', models.CharField(max_length=500)),
                ('whose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeapp.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=30)),
                ('college', models.CharField(max_length=30)),
                ('frm_date', models.DateField()),
                ('to_date', models.DateField()),
                ('whose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeapp.Developer')),
            ],
        ),
    ]