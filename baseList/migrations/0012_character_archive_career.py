# Generated by Django 3.2.4 on 2021-07-24 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0007_listarchivecarriers'),
        ('baseList', '0011_character_current_career'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='archive_career',
            field=models.ManyToManyField(blank=True, null=True, to='career.ListArchiveCarriers', verbose_name='Ранние должности'),
        ),
    ]
