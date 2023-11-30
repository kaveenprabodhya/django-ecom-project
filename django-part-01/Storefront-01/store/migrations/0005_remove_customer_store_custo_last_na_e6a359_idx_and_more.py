# Generated by Django 4.0.3 on 2022-03-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_store_custo_last_na_e6a359_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='customer',
            name='store_custo_last_na_e6a359_idx',
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='store_custo_last_na_2e448d_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table=None,
        ),
    ]
