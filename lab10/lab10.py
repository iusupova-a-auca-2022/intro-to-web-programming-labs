import math
import random
from datetime import datetime, timedelta

radius = 10
area = math.pi * math.pow(radius, 2)
print("Area of the circle:", area)


colors = ["red", "blue", "green", "yellow", "orange", "purple"]
chosen = random.choice(colors)
print("The chosen color is", chosen)


now = datetime.now()
print("The current date and time are", now)

future_date = now + timedelta(days=3)
print("The future date after three days is", future_date)


