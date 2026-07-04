#Match case statement

def isWeekend(day):
    match day.lower():
        case "saturday" | "sunday":
            print("Today is Weekend")
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            print("Today is Weekday")
        case _:
            print("invalid Input")
            
isWeekend("ThurMon")

#def findDay(day):
#    match day.lower():
#        case "monday":
#            print("Today is Monday")
#        case "tuesday":
#            print("Today is Tuesday")
#        case "wednesday":
#            print("Today is Wednesday")
#        case "thursday":
#            print("Today is Thursday")
#        case "friday":
#            print("Today is Friday")
#        case "saturday":
#            print("Today is Saturday")
#        case "sunday":
#            print("Today is Sunday")
#        case _:
#            print("Invalid Input")    
#
#findDay("Monday")



