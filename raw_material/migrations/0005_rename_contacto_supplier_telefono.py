# Generated by Django 5.2.1 on 2025-06-18 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raw_material', '0004_alter_rawmaterial_precio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='contacto',
            new_name='telefono',
        ),
    ]
