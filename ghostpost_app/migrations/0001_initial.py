# Generated by Django 3.1 on 2020-08-26 23:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roast_Boast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_input', models.CharField(max_length=200)),
                ('boast', models.BooleanField()),
                ('up_vote', models.IntegerField(default=0)),
                ('down_vote', models.IntegerField(default=0)),
                ('submission_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
