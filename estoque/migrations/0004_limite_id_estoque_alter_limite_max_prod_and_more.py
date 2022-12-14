# Generated by Django 4.0.5 on 2022-09-09 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_limite_delete_min_max'),
    ]

    operations = [
        migrations.AddField(
            model_name='limite',
            name='id_estoque',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='estoque.estoque'),
        ),
        migrations.AlterField(
            model_name='limite',
            name='max_prod',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='limite',
            name='min_prod',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
