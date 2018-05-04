from django import forms
from django.core.validators import EmailValidator

all_attributes =(
        ('Brand', 'Brand'),
        ('DeviceName','Device Name'),
        ('_2g_bands', '2g bands'),
        ('_3_5mm_jack_', '3.5mm jack'),
        ('_3g_bands', '3g bands'),
        ('_4g_bands', '4g bands'),
        ('alert_types', 'alert types'),
        ('announced', 'announced'),
        ('audio_quality', 'audio_quality'),
        ('battery_c', 'battery_c'),
        ('bluetooth', 'bluetooth'),
        ('body_c', 'body_c'),
        ('browser', 'browser'),
        ('build', 'build'),
        ('call_records', 'call_records'),
        ('camera', 'camera'),
        ('camera_c', 'camera_c'),
        ('card_slot', 'card_slot'),
        ('chipset', 'chipset'),
        ('colors', 'colors'),
        ('cpu', 'cpu'),
        ('dimensions', 'dimensions'),
        ('display', 'display'),
        ('display_c', 'display_c'),
        ('edge', 'edge'),
        ('features', 'features'),
        ('features_c', 'features_c'),
        ('games', 'games'),
        ('gprs', 'gprs'),
        ('gps', 'gps'),
        ('gpu', 'gpu'),
        ('infrared_port', 'infrared_port'),
        ('internal', 'internal'),
        ('java', 'java'),
        ('keyboard', 'keyboard'),
        ('loudspeaker', 'loudspeaker'),
        ('loudspeaker_', 'loudspeaker_'),
        ('memory_c', 'memory_c'),
        ('messaging', 'messaging'),
        ('multitouch', 'multitouch'),
        ('music_play', 'music_play'),
        ('network_c', 'network_c'),
        ('nfc', 'nfc'),
        ('os', 'os'),
        ('performance', 'performance'),
        ('phonebook', 'phonebook'),
        ('price', 'price'),
        ('primary_', 'primary_'),
        ('protection', 'protection'),
        ('radio', 'radio'),
        ('resolution', 'resolution'),
        ('sar', 'sar'),
        ('sar_eu', 'sar_eu'),
        ('sar_us', 'sar_us'),
        ('secondary', 'secondary'),
        ('sensors', 'sensors'),
        ('sim', 'sim'),
        ('size', 'size'),
        ('sound_c', 'sound_c'),
        ('speed', 'speed'),
        ('stand_by', 'stand_by'),
        ('status', 'status'),
        ('talk_time', 'talk_time'),
        ('technology', 'technology'),
        ('type', 'type'),
        ('usb', 'usb'),
        ('video', 'video'),
        ('weight', 'weight'),
        ('wlan', 'wlan')
        )


class SearchForm(forms.Form):
    device = forms.CharField(max_length=32, label='Device name')
    brand = forms.CharField(max_length=32, label='Brand', required=False)
    position = forms.IntegerField(required=False)
    device2 = forms.CharField(max_length=32, label='Second device')
    brand2 = forms.CharField(max_length=32, label='Second brand', required=False)
    position2 = forms.IntegerField(required=False)
    attributes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=all_attributes)
    similar = forms.BooleanField(required=False)
    similar2 = forms.BooleanField(required=False)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label='user-name')
    password = forms.CharField(widget=forms.PasswordInput(), label='password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='password2')
    first_name = forms.CharField(label='first-name')
    last_name = forms.CharField(label='last-name')
    email = forms.CharField(label='user-email', validators=[EmailValidator(message='zly email')])


class UserSearchForm(forms.Form):
    device = forms.CharField(max_length=32, label='Device name')
    brand = forms.CharField(max_length=32, label='Brand', required=False)
    position = forms.IntegerField(required=False)
    attributes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=all_attributes)

class HiddenForm(forms.Form):
     to_db = forms.Textarea()
