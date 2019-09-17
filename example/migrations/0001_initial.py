# Generated by Django 2.2.5 on 2019-09-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(default='xxx', max_length=5)),
                ('field2', models.CharField(blank=True, max_length=23, null=True)),
                ('field3', models.BooleanField(default=False)),
                ('field4', models.IntegerField(default=42)),
                ('field5', models.TextField(blank=True, null=True)),
            ],
        ),
    ]