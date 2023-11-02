# Generated by Django 4.2.6 on 2023-10-31 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0003_awards1_delete_awards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderproduct',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_item_id', models.PositiveIntegerField()),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_item_metas',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='orderitemmetas',
            options={},
        ),
    ]