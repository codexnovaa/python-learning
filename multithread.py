#Used to perform multiple tasks concunrrently (multitasking) Good gor I/O bound tasks like reading files or fetching data from API's ------ threading.Thread(target=myFunction)

import threading
import time

def walkDog(dog1, dog2):
    time.sleep(8)
    print(f"You finished walking {dog1} and {dog2}")
    
def takeOutTrash():
    time.sleep(2)
    print("You take out the trash")
    
def getMail():
    time.sleep(4)
    print("You get the mail")
    
chore1 = threading.Thread(target=walkDog, args=("Scoobyy", "Doobyy"))
chore2 = threading.Thread(target=takeOutTrash)
chore3 = threading.Thread(target=getMail)

chore1.start()
chore2.start()
chore3.start()

chore2.join()
chore1.join()
chore3.join()

print("All chores are finished! :)")
