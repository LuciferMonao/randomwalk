import random
import matplotlib.pyplot as plt
import time
import sys
from datetime import datetime

def delete_line(amount=1):
    for _ in range(amount):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

class test_object:

    def __init__(self, dimensions=1, movement_speed=1, two_directions=True, history=False):
        self.dimensions = dimensions
        self.movement_speed = movement_speed
        self.two_directions = two_directions
        self.position = []
        self.history = history
        for _ in range(dimensions):
            self.position.append({"position": 0, "history": []})
    

    def move(self, movement_speed=False, maximum_distance=False):
        if not movement_speed == False:
            self.movement_speed = movement_speed
        
        if not maximum_distance == False:
            self.maximum_distance = maximum_distance

        movement = random.randint(0, self.dimensions) - 1

        if self.two_directions == True:
            random_int = random.randint(0, 3)
            if random_int == 0:
                self.position[movement]["position"] += self.movement_speed
                if self.history == True: self.position[movement]["history"].append(str(self.movement_speed))
            elif random_int == 1:
                self.position[movement]["position"] -= self.movement_speed
                if self.history == True: self.position[movement]["history"].append(str(-1 * self.movement_speed))
            else:
                if self.history == True: self.position[movement]["history"].append("0")
        else:
            random_int = random.randint(0, 2)
            if random_int == 0:
                self.position[movement]["position"] += self.movement_speed
                if self.history == True: self.position[movement]["history"].append(str(self.movement_speed))
            else:
                if self.history == True: self.position[movement]["history"].append("0")

    def get_position(self):
        return(self.position)




run = True


test_number = int(input("How many testobjects do you want to create?\n"))
print("Creating objects...")

objects = []


creating_objects_start = time.perf_counter()
for i in range(test_number):
    objects.append(test_object())

#print(f"Finished creating objects... It took {time.perf_counter() - creating_objects_start} Seconds.")

moving_objects_start = time.perf_counter()
input_data = input("How many Movements do you want to have?\n")

for i in range(int(input_data)):
    for element in objects:
        element.move()
    print(f"Movement {i} of {input_data} finished...")
    time.sleep(0.001)
        

    

#print(f"Finished moving objects... It took {time.perf_counter - moving_objects_start} Seconds.")
highest_x = -1000000000000000000000000000
lowest_x = 10000000000000000000000000000

for dimension in range(objects[0].dimensions):

    for test_object in objects:
        if highest_x < test_object.get_position()[dimension]["position"]:
            highest_x = test_object.get_position()[dimension]["position"]

        if lowest_x > test_object.get_position()[dimension]["position"]:
            lowest_x = test_object.get_position()[dimension]["position"]
        
    x_values = range(lowest_x - 1, highest_x + 2)
    y_values = []

    for element in x_values:
        y_values.append(0)
        for test_object in objects:
            if int(test_object.get_position()[dimension]["position"]) == int(element):
                y_values[x_values.index(element)] += 1

    plt.plot(x_values, y_values)
    plt.xlabel("Position")
    plt.ylabel("Number of testobjects there.")
    plt.title(f"Diffusion - v1")

plt.savefig(f'graphs/graph, object_amount: {test_number}, movement_amount:  {input_data}, time: {datetime.now()}.png')
plt.show()
print("plot shown.")
    
     

