# import sys
# import json
# import requests
from fonoapi import fonoapi
fon = fonoapi.FonoAPI('cf3590b49448175eb05232c57bfc1d257cbf93113742cbfc')
#
device = 'galaxy s7'
phones = fon.getdevice(device)
# # list = phones.list_of_lists()
# # new_list = []
# # new1_list = []
# # for i in list[0]:
# #     new1_list.append(i)
# # for j in list[1]:
# #     new_list.append(j)
# # print(new_list)
# # print(new1_list)
# # print(new_list[0], ':', new1_list[0][0], )
#
#OPTIONS = ['Brand', 'DeviceName', '_2g_bands', '_3_5mm_jack_', '_3g_bands', '_4g_bands', 'alert_types', 'announced', 'audio_quality', 'battery_c', 'bluetooth', 'body_c', 'browser', 'build', 'call_records', 'camera', 'camera_c', 'card_slot', 'chipset', 'colors', 'cpu', 'dimensions', 'display', 'display_c', 'edge', 'features', 'features_c', 'games', 'gprs', 'gps', 'gpu', 'infrared_port', 'internal', 'java', 'keyboard', 'loudspeaker', 'loudspeaker_', 'memory_c', 'messaging', 'multitouch', 'music_play', 'network_c', 'nfc', 'os', 'performance', 'phonebook', 'price', 'primary_', 'protection', 'radio', 'resolution', 'sar', 'sar_eu', 'sar_us', 'secondary', 'sensors', 'sim', 'size', 'sound_c', 'speed', 'stand_by', 'status', 'talk_time', 'technology', 'type', 'usb', 'video', 'weight', 'wlan']
# from fonoapi import fonoapi
# device = 'galaxy s7'
# phones = fon.getdevice(device, brand='samsung')
# fon = fonoapi.FonoAPI('cf3590b49448175eb05232c57bfc1d257cbf93113742cbfc')
# list = phones.list_of_lists()
# new_list = []
# for j in list[1]:
#     new_list.append(j)


# from fonoapi import fonoapi
#
# fon = fonoapi.FonoAPI('cf3590b49448175eb05232c57bfc1d257cbf93113742cbfc')
# OPTIONS = []
# device = 'galaxy s7'
# phones = fon.getdevice(device, brand='samsung')
# list = phones.list_of_lists()
# x = 0
# for j in list[1]:
#     OPTIONS.append(j)
#     x += 1
keys = ['DeviceName']
list_dicts = phones.list_of_dicts()
for i in list_dicts:
    print(i)
