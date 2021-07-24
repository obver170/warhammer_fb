# Generated by Django 3.2.4 on 2021-07-24 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0013_alter_baseattribute_initial_meaning'),
        ('baseList', '0005_auto_20210724_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_nation', models.CharField(choices=[('Человек', 'Человек'), ('Полурослик', 'Полурослик'), ('Гном', 'Гном'), ('Высший эльф', 'Высший эльф'), ('Лесной эльф', 'Лесной эльф')], max_length=30, verbose_name='Народ')),
            ],
            options={
                'verbose_name': 'Народ',
                'verbose_name_plural': 'Народы',
            },
        ),
        migrations.AlterField(
            model_name='character',
            name='init_attribute',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='attribute.attributelist', verbose_name='Начальные значения характеристик'),
        ),
        migrations.AddField(
            model_name='character',
            name='nation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseList.nation'),
        ),
    ]
