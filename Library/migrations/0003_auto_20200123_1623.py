# Generated by Django 3.0.1 on 2020-01-23 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_auto_20200123_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='generalColour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='things', to='Library.generalColour'),
        ),
    ]
