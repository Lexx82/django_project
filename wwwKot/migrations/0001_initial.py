# Generated by Django 3.1.2 on 2020-10-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WwwDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abr', models.CharField(max_length=6)),
                ('dep', models.CharField(max_length=100)),
                ('hw_info', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('note', models.TextField(blank=True)),
            ],
        ),
    ]