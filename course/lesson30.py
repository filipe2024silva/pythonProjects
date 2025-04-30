velocity = 60
car_local = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

car_got_ticket = car_local >= (LOCAL_1 - RADAR_RANGE) and car_local <= (LOCAL_1 + RADAR_RANGE)
car_high_speed = velocity > RADAR_1

if car_high_speed:
    print("Car velocity in radar 1")
    
if car_got_ticket and car_high_speed:
    print('The car got a ticket')
    
print(id(car_local))