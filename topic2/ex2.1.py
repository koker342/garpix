room_temp = int(input())
desired_temp = int(input())
humidity = int(input())

if room_temp > desired_temp and humidity > 80:
    print('on')
else:
    print('off')    