# Generated by Django 4.2.7 on 2024-01-04 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ostanshahr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airfare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=0, max_digits=999999999)),
                ('date', models.DateField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_city', to='ostanshahr.cities')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_city', to='ostanshahr.cities')),
            ],
        ),
    ]
