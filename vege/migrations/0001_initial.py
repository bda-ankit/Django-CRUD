# Generated by Django 5.1 on 2024-08-26 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reciepe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciepe_name', models.CharField(max_length=100)),
                ('reciepe_desc', models.TextField()),
                ('reciepe_image', models.ImageField(upload_to='receipe')),
            ],
        ),
    ]
