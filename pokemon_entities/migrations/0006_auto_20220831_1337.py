# Generated by Django 3.1.14 on 2022-08-31 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20220830_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='longitude',
            new_name='lon',
        ),
    ]
