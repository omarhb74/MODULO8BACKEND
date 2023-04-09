# Generated by Django 4.1.6 on 2023-02-12 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_rename_fechavencimiento_producto_fechavencimientogarantia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True)),
                ('estado', models.BooleanField(default=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ordendecompra', models.CharField(max_length=10)),
                ('descripcion', models.TextField(blank=True)),
                ('fechavencimientogarantia', models.DateTimeField(null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.TextField(blank=True)),
                ('fecharegistro', models.DateTimeField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='tipoproducto',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
        migrations.RenameModel(
            old_name='Tipoproducto',
            new_name='Tipodispositivo',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='dispositivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.tipodispositivo'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.usuario'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='dispositivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.dispositivo'),
        ),
    ]
