# Generated by Django 4.1.6 on 2023-02-12 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.TextField(blank=True)),
                ('fecharegistro', models.DateTimeField(null=True)),
                ('estado', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('fechavencimiento', models.DateTimeField(null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'productos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tipoproducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True)),
                ('fechaventa', models.DateTimeField(null=True)),
                ('preciototal', models.FloatField(null=True)),
                ('estado', models.BooleanField()),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'db_table': 'ventas',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='tipoproducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.tipoproducto'),
        ),
    ]