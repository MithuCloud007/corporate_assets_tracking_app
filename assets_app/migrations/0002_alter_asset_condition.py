# Generated by Django 4.2.7 on 2024-03-15 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='condition',
            field=models.CharField(choices=[('PHONE', 'PHONE'), ('LAPTOP', 'LAPTOP'), ('TABLETS', 'TABLETS'), ('OTHERS', 'OTHERS')], max_length=50),
        ),
    ]
