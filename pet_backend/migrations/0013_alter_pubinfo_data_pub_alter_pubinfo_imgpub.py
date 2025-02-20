# Generated by Django 5.1 on 2025-01-28 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_backend', '0012_pubinfo_imgpub_alter_pubinfo_data_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pubinfo',
            name='data_pub',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 28, 19, 23, 56, 365077, tzinfo=datetime.timezone.utc), editable=None),
        ),
        migrations.AlterField(
            model_name='pubinfo',
            name='imgpub',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
