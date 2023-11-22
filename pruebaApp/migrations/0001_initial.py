# Generated by Django 4.2.6 on 2023-11-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('tipo_user', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('duenno', models.CharField(max_length=30)),
                ('destino', models.CharField(max_length=30)),
                ('salida', models.CharField(max_length=15)),
                ('capacidad', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
