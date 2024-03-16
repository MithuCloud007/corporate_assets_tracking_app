# Generated by Django 4.2.7 on 2024-03-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateTimeField()),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('condition_on_checkout', models.CharField(max_length=50)),
                ('condition_on_return', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]