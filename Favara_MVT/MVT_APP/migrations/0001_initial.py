# Generated by Django 4.1.3 on 2022-11-02 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('parentezco', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('fecha_nac', models.DateField()),
            ],
        ),
    ]
