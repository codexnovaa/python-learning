#Logical Operator --- or, and, not


temp = 24
is_sunny = True

#if temp >= 35 or temp <= 0 or is_raining:
    #print("The outing is cancelled")
#else:
    #print("The outing is still on going")
    
if temp >= 28 and is_sunny:
    print("It is very HOT!")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    
    
#if not is_sunny:
    #print("It is cloudy outside")
#else:
    #print("Is is sunny outside")