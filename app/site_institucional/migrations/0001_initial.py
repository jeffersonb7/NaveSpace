# Generated by Django 3.2.7 on 2021-09-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
            ],
        ),
    ]