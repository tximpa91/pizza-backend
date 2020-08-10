# Generated by Django 3.1 on 2020-08-10 08:54

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('topping_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('pizza_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('toppings', models.ManyToManyField(to='pizza_app.Topping')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]