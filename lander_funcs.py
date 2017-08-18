# Project 2 - Moonlander
#
# Name: Justin Mo
# Instructor: Brian Jones
# Section: 17
import math

def show_welcome():
   print("")
   print("Welcome aboard the Lunar Module Flight Simulator")
   print("")
   print("   To begin you must specify the LM's initial altitude")
   print("   and fuel level.  To simulate the actual LM use")
   print("   values of 1300 meters and 500 liters, respectively.")
   print("")
   print("   Good luck and may the force be with you!")
   print("")
 
def get_altitude():
   altitude = float(input("Enter the initial altitude of the LM (in meters): "))
   
   while altitude > 9999 or altitude < 1:
      print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
      print("")
      altitude = float(input("Enter the initial altitude of the LM (in meters): "))
   return altitude

def get_fuel():
   fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): ")) 
   while fuel <= 0:
      print("ERROR: Amount of fuel must be positive, please try again")
      print("")
      fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
   return fuel

def display_LM_state(elapsed_time, altitude, velocity, fuel_amount, fuel_rate):
   print("{:>12s} {:4d} s".format("Elapsed Time:",elapsed_time))
   print("{:>13s} {:4d} l".format("Fuel:",fuel_amount))
   print("{:>13s} {:4d} l/s".format("Rate:",fuel_rate))
   print("{:>13s} {:7.2f} m".format("Altitude:",altitude))
   print("{:>13s} {:7.2f} m/s".format("Velocity:",velocity))

def get_fuel_rate(current_fuel):
   fuel_rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   
   while fuel_rate < 0 or fuel_rate > 9:
      print("ERROR: Fuel rate must be between 0 and 9, inclusive")
      print("")
      fuel_rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   if fuel_rate > current_fuel:
      return current_fuel
   else:
      return fuel_rate
   
def display_LM_landing_status(velocity):
   if velocity < 1 and velocity > -2:
      print("Status at landing - The eagle has landed!")
   if velocity > -10 and velocity < -1:
      print("Status at landing - Enjoy your oxygen while it lasts!")
   if velocity <= -10:
      print("Status at landing - Ouch - that hurt!")
 
def update_acceleration(gravity, fuel_rate):
   new_acceleration =  gravity * ((fuel_rate/5) - 1)
   return new_acceleration

def update_altitude(altitude, velocity, new_acceleration):
   new_altitude =  altitude + velocity + new_acceleration/2
   if new_altitude < 0.00:
      return 0.00
   return float(new_altitude)

def update_velocity(velocity, new_acceleration):
   new_velocity = velocity + new_acceleration
   return float(new_velocity)

def update_fuel(fuel, fuel_rate):
   new_fuel = fuel - fuel_rate
   return int(new_fuel)

