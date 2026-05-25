distance_mi = 5
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True
if distance_mi <= 1 and not is_raining:
    print('You can walk')
elif distance_mi <= 5 and not is_raining and has_bike:
    print('You can ride a bike')
elif has_ride_share_app and is_raining and distance_mi >= 5:
    print("You can order a car")

else:
    print("You can't walk")








