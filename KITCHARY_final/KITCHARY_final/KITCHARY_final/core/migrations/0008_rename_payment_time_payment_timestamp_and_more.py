# Generated by Django 5.1.3 on 2025-07-21 15:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_ordered_at_order_created_at_order_total_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_time',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_status',
        ),
        migrations.AddField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='payment',
            name='method',
            field=models.CharField(default='Card', max_length=100),
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(default='Success', max_length=50),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.FloatField(),
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('customer', 'Customer'), ('staff', 'Staff')], default='customer', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='core.menuitem'),
        ),
    ]
