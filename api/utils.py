from rest_framework.authtoken.models import Token
from datetime import datetime

def convert_to_twelve_format(hour_obj):
    if hour_obj == 24:
        hour_obj = 0
    time_obj = datetime.strptime(str(hour_obj), "%H")
    return time_obj.strftime("%I %p")

def get_token(user):
    token, _ = Token.objects.get_or_create(user=user)
    return token.key

def change_time_format(input_time, time_delta = 1):
    in_time = datetime.strptime(input_time, "%I:%M %p")
    out_time = datetime.strftime(in_time, "%H:%M")
    return in_time.hour+time_delta if in_time.minute else in_time.hour

def get_available_slots(availablity_query_set):
    required_set = set()
    for each in availablity_query_set:
        for available_hour in range(each.available_from, each.available_to):
            required_set.add((convert_to_twelve_format(available_hour), convert_to_twelve_format(available_hour+1)))
    return required_set