# Generated by Django 4.0.5 on 2022-09-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=50)),
                ('product_type', models.CharField(max_length=50)),
                ('product_price', models.FloatField(max_length=20)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
