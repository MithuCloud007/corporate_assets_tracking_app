# Generated by Django 4.2.7 on 2024-03-15 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset_tracking_app', '0001_initial'),
        ('assets_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetlog',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets_app.asset'),
        ),
    ]
