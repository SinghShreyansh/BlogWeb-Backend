# Generated by Django 4.0.3 on 2022-03-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('body', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=500)),
            ],
        ),
    ]