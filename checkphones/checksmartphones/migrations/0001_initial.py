# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-20 07:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default=None, max_length=128)),
                ('device_name', models.CharField(default=None, max_length=128)),
                ('_2g_bands', models.CharField(default=None, max_length=128)),
                ('_3_5mm_jack', models.CharField(default=None, max_length=128)),
                ('_3g_bands', models.CharField(default=None, max_length=128)),
                ('_4g_bands', models.CharField(default=None, max_length=128)),
                ('alert_types', models.CharField(default=None, max_length=128)),
                ('announced', models.CharField(default=None, max_length=128)),
                ('audio_quality', models.CharField(default=None, max_length=128)),
                ('battery_c', models.CharField(default=None, max_length=128)),
                ('bluetooth', models.CharField(default=None, max_length=128)),
                ('body_c', models.CharField(default=None, max_length=128)),
                ('browser', models.CharField(default=None, max_length=128)),
                ('build', models.CharField(default=None, max_length=128)),
                ('call_records', models.CharField(default=None, max_length=128)),
                ('camera', models.CharField(default=None, max_length=128)),
                ('camera_c', models.CharField(default=None, max_length=128)),
                ('card_slot', models.CharField(default=None, max_length=128)),
                ('chipset', models.CharField(default=None, max_length=128)),
                ('colors', models.CharField(default=None, max_length=128)),
                ('cpu', models.CharField(default=None, max_length=128)),
                ('dimensions', models.CharField(default=None, max_length=128)),
                ('display', models.CharField(default=None, max_length=128)),
                ('display_c', models.CharField(default=None, max_length=128)),
                ('edge', models.CharField(default=None, max_length=128)),
                ('features', models.CharField(default=None, max_length=128)),
                ('features_c', models.CharField(default=None, max_length=128)),
                ('games', models.CharField(default=None, max_length=128)),
                ('gprs', models.CharField(default=None, max_length=128)),
                ('gps', models.CharField(default=None, max_length=128)),
                ('gpu', models.CharField(default=None, max_length=128)),
                ('infrared_port', models.CharField(default=None, max_length=128)),
                ('internal', models.CharField(default=None, max_length=128)),
                ('java', models.CharField(default=None, max_length=128)),
                ('keyboard', models.CharField(default=None, max_length=128)),
                ('loudspeaker', models.CharField(default=None, max_length=128)),
                ('loudspeaker_check', models.CharField(default=None, max_length=128)),
                ('memory_c', models.CharField(default=None, max_length=128)),
                ('messaging', models.CharField(default=None, max_length=128)),
                ('multitouch', models.CharField(default=None, max_length=128)),
                ('music_play', models.CharField(default=None, max_length=128)),
                ('network_c', models.CharField(default=None, max_length=128)),
                ('nfc', models.CharField(default=None, max_length=128)),
                ('os', models.CharField(default=None, max_length=128)),
                ('performance', models.CharField(default=None, max_length=128)),
                ('phonebook', models.CharField(default=None, max_length=128)),
                ('price', models.CharField(default=None, max_length=128)),
                ('primary', models.CharField(default=None, max_length=128)),
                ('protection', models.CharField(default=None, max_length=128)),
                ('radio', models.CharField(default=None, max_length=128)),
                ('resolution', models.CharField(default=None, max_length=128)),
                ('sar', models.CharField(default=None, max_length=128)),
                ('sar_eu', models.CharField(default=None, max_length=128)),
                ('sar_us', models.CharField(default=None, max_length=128)),
                ('secondary', models.CharField(default=None, max_length=128)),
                ('sensors', models.CharField(default=None, max_length=128)),
                ('sim', models.CharField(default=None, max_length=128)),
                ('size', models.CharField(default=None, max_length=128)),
                ('sound_c', models.CharField(default=None, max_length=128)),
                ('speed', models.CharField(default=None, max_length=128)),
                ('stand_by', models.CharField(default=None, max_length=128)),
                ('status', models.CharField(default=None, max_length=128)),
                ('talk_time', models.CharField(default=None, max_length=128)),
                ('technology', models.CharField(default=None, max_length=128)),
                ('type', models.CharField(default=None, max_length=128)),
                ('usb', models.CharField(default=None, max_length=128)),
                ('video', models.CharField(default=None, max_length=128)),
                ('weight', models.CharField(default=None, max_length=128)),
                ('wlan', models.CharField(default=None, max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HiddenModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_db', models.TextField()),
            ],
        ),
    ]