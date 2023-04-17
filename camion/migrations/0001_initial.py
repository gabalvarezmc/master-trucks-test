# Generated by Django 4.0.5 on 2023-04-14 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_marca', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ModeloVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo_camion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SistemaControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistema_control', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCamion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_camion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_equipo', models.CharField(max_length=100)),
                ('clasificacion', models.CharField(choices=[('Camion Fabrica', 'Camion Fabrica')], max_length=50)),
                ('estado', models.CharField(choices=[('activo', 'ACTIVO'), ('inactivo', 'inactivo')], max_length=20)),
                ('numero_celular1', models.CharField(max_length=36)),
                ('numero_celular2', models.CharField(blank=True, max_length=36, null=True)),
                ('id_mac', models.CharField(max_length=256)),
                ('patente', models.CharField(max_length=100)),
                ('leasing', models.BooleanField(blank=True, default=True, null=True)),
                ('año', models.DateField()),
                ('capacidad_total', models.FloatField()),
                ('matriz', models.FloatField()),
                ('nitrato_amonio', models.FloatField()),
                ('vin', models.CharField(max_length=255)),
                ('alto_desempeño', models.BooleanField()),
                ('alto_tonelaje', models.BooleanField()),
                ('capacidad_agente', models.BooleanField()),
                ('last_seen', models.DateTimeField(blank=True, null=True)),
                ('last_latitud', models.FloatField(blank=True, null=True)),
                ('last_longitud', models.FloatField(blank=True, null=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camion.marcavehiculo')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camion.modelovehiculo')),
                ('sistema_control', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camion.sistemacontrol')),
            ],
        ),
        migrations.CreateModel(
            name='CompaniaCelular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_compania', models.CharField(max_length=100)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.pais')),
            ],
        ),
    ]