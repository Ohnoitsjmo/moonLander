# Project 2 - Moonlander
#
# Name: Justin Mo
# Instructor: Brian Jones
# Section: 17

from lander_funcs import *
  
def main():
   gravity = 1.62
   elapsed_time = 0
   velocity = 0.00
   fuel_rate = 0
   show_welcome()
   altitude = get_altitude()
   fuel_amount = get_fuel()
   print("")
   print("LM state at retrorocket cutoff")
   display_LM_state(elapsed_time, altitude, velocity, fuel_amount, fuel_rate)
   print("")
   while altitude > 0.00 and fuel_amount > 0:
      fuel_rate = get_fuel_rate(fuel_amount)
      fuel_amount = update_fuel(fuel_amount, fuel_rate)
      nu_acceleration = update_acceleration(gravity, fuel_rate)
      altitude = update_altitude(altitude, velocity, nu_acceleration)
      velocity = update_velocity(velocity, nu_acceleration) 
      elapsed_time += 1
      if fuel_amount == 0:
         fuel_rate = 0
         elapsed_time -= 1
         while altitude > 0.00:
            elapsed_time += 1
            print("OUT OF FUEL - Elapsed Time:{:4d} Altitude:{:8.2f} Velocity:{:8.2f}".format(elapsed_time, altitude, velocity)) 
            fuel_amount = update_fuel(fuel_amount, fuel_rate)
            nu_acceleration = update_acceleration(gravity, fuel_rate)
            altitude = update_altitude(altitude, velocity, nu_acceleration)
            velocity = update_velocity(velocity, nu_acceleration)
         elapsed_time += 1 
      if altitude == 0.00:
         print("")
         print("LM state at landing/impact")
      display_LM_state(elapsed_time, altitude, velocity, fuel_amount, fuel_rate)
      print("")
   landing_status = display_LM_landing_status(update_velocity(velocity, nu_acceleration))
if __name__ == "__main__":
   main()


