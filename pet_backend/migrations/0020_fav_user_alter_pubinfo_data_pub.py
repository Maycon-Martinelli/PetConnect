# Generated by Django 5.0.6 on 2025-02-08 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_backend', '0019_alter_pubinfo_castramento_alter_pubinfo_data_pub'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fav_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pub', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='pubinfo',
            name='data_pub',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 8, 12, 21, 59, 293460, tzinfo=datetime.timezone.utc), editable=None),
        ),
    ]
