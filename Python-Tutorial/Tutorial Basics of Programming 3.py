from argparse import Action

from sympy.strategies import condition

#if condition:
#    Action

#click = True
#like = 0
#
#if click == True:
#    like = like + 1
#   click = False
#
#print(like)


# --- Like Counter Example ---
click = True  # User clicks the "like" button
like = 0      # Initial like count

if click:             # If the button is clicked
    like += 1         # Increment like count
    click = False     # Reset click state (to prevent double-counting)
print(like)           # Output: 1 (since click was True)

# --- Thermostat Control Example ---
Temperature = 20  # Current temperature (no need for ": int" in Python)
Thermo = 15       # Thermostat setting
print(Thermo)     # Output: 15

if 15 >= Temperature:  # If 15 ≥ 20 (False)
    Thermo += 5        # Won't execute
print(Thermo)          # Output: 15 (unchanged)

if Temperature >= 20:  # If 20 ≥ 20 (True)
    Thermo -= 3        # Thermo = 15 - 3 = 12
print(Thermo)          # Output: 12

# --- Pajama Time Logic ---
Time = "Day"        # Possible values: "Night", "Morning", or "Day"
Sleepy = False      # User is not sleepy
Pajamas = "Unknown" # Initial state
InBed = True        # User is in bed

print(Pajamas)      # Output: "Unknown" (initial value)

# Determine pajama state based on time
if Time == "Night":
    Pajamas = "On"   # Wear pajamas at night
elif Time == "Morning":
    Pajamas = "Off"  # Take off in the morning
else:
    Pajamas = "Off"  # Default to "Off" during the day

print(Pajamas)       # Output: "Off" (since Time is "Day")