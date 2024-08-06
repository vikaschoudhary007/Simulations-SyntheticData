import time
from flightgear_python.fg_if import TelnetConnection
import pandas as pd

# Connect to FlightGear's Telnet server
telnet_conn = TelnetConnection('localhost', 5500)
telnet_conn.connect()  # Make an actual connection


# Set initial parameters for takeoff
telnet_conn.set_prop("/controls/engines/current-engine/throttle", 1.0)  # Full throttle
telnet_conn.set_prop("/controls/flight/flaps", 1)  # Set flaps for takeoff
telnet_conn.set_prop("/controls/flight/elevator", 0.1)  # Elevator up for takeoff
telnet_conn.set_prop("/controls/flight/aileron", 0)  # Center ailerons
telnet_conn.set_prop("/controls/flight/rudder", 0)  # Center rudder
time.sleep(10)  # Allow time for the aircraft to accelerate and take off

# Example commands to control the simulation
commands = [
    ("/controls/flight/aileron", 0.1, 2),
    ("/controls/flight/elevator", 0.1, 2),
    ("/controls/flight/rudder", 0.1, 2)
]

# List to store collected data
data = []

i = 0
# Run multiple simulations
try:
    while True:
        for prop_str, value, duration in commands:
            telnet_conn.set_prop(prop_str, value)
            time.sleep(duration)  # Wait for the command to take effect

            # Retrieve data (e.g., aircraft position)
            lat = telnet_conn.get_prop('/position/latitude-deg')
            lon = telnet_conn.get_prop('/position/longitude-deg')
            alt = telnet_conn.get_prop('/position/altitude-ft')

            # Append data to list
            data.append({
                "latitude": lat,
                "longitude": lon,
                "altitude": alt,
                "command": prop_str,
                "duration": duration
            })

            # Print collected data for debug
            print(f"Sim {i+1}, Command: {prop_str}, Lat: {lat}, Lon: {lon}, Alt: {alt}")

# Exception handling to ensure proper closure of telnet connection
except KeyboardInterrupt:
    print("Script stopped by user.")

# No need to close telnet connection explicitly as it doesn't have a close() method

# Convert collected data to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("flight_data.csv", index=False)
