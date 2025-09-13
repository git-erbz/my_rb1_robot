import math


### The following is a calculator to help me determine

# 1. the total volume of the robot
# 2. The density from knowing mass and volume 
# 3. The individual compenets masses
# 4. inertial moments for each component

#____________________________________________________________#

# Given Values:

totalMass = 25 #kg
base_h = 0.3 #m
base_r = 0.25 #m
wheel_h = 0.03 #m
wheel_r = 0.0025 #m
caster_r= 0.025 #m
laser_r = 0.05 #m chose this


# Volume calculations
base_vol = math.pi * base_r**2 * base_h
wheel_vol = math.pi * wheel_r**2 * wheel_h
caster_vol =(4/3) * math.pi * caster_r**3
laser_vol =(4/3) * math.pi * laser_r**3
totalVol = base_vol + 2*wheel_vol + 2*caster_vol + laser_vol

# Claculation for Density
rho = totalMass / totalVol
print(rho)

# Calculate the mass for each member
base_mass = rho * base_vol # ~49.88
wheel_mass = rho * wheel_vol #~ 0.005
caster_mass = rho * caster_vol #~ 0.055
laser_mass = rho * laser_vol 
print(str(base_mass) +', '+ str(wheel_mass) +', '+ str(caster_mass) +', '+ str(laser_mass))



# claculation for Inertial moments
print(" ")
## Base 
base_ixx = (1/12) * base_mass * (3*base_r**2 + base_h**2)
base_iyy = base_ixx
base_izz = 0.5  *base_mass * base_r**2
string = "base inertials: "
print(string, base_ixx, base_iyy, base_izz)

## wheel
wheel_ixx = (1/12) * wheel_mass * (3*wheel_r**2 + wheel_h**2)
wheel_iyy = wheel_ixx
wheel_izz = 0.5  *wheel_mass * wheel_r**2
string = "wheel inertials: "
print(string, wheel_ixx, wheel_iyy, wheel_izz)

## caster 
caster_ixx = (2/5)*caster_mass*caster_r**2
caster_iyy = caster_ixx
caster_izz = caster_ixx
string = "caster inertials: "
print(string, caster_ixx, caster_iyy, caster_izz)
print(" ")

## laser
laser_ixx = (2/5)*laser_mass*laser_r**2
laser_iyy = laser_ixx
laser_izz = laser_ixx
string = "laser inertials: "
print(string, laser_ixx, laser_iyy, laser_izz)




