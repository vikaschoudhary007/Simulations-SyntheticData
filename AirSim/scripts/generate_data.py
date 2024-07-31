import setup_path
import airsim
import os
import time
import numpy as np
import cv2

print("""This script is designed to fly on the streets of the Neighborhood environment
and assumes the unreal position of the drone is [160, -1500, 120].""")

# Connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

print("arming the drone...")
client.armDisarm(True)

state = client.getMultirotorState()
if state.landed_state == airsim.LandedState.Landed:
    print("taking off...")
    client.takeoffAsync().join()
else:
    client.hoverAsync().join()

time.sleep(1)

state = client.getMultirotorState()
if state.landed_state == airsim.LandedState.Landed:
    print("take off failed...")
    sys.exit(1)

# AirSim uses NED coordinates so negative axis is up.
# z of -5 is 5 meters above the original launch point.
z = -5
print("make sure we are hovering at {} meters...".format(-z))
client.moveToZAsync(z, 1).join()

# Create a folder to save images and labels - give full path
output_folder = '/AirSim/airsim_setup/AirSim_env/airsim_generate_data'
os.makedirs(output_folder, exist_ok=True)

# Function to save images
def save_image(response, count, img_type):
    img1d = np.frombuffer(response.image_data_uint8, dtype=np.uint8)
    img_rgb = img1d.reshape(response.height, response.width, 3)
    filename = os.path.join(output_folder, f"{img_type}_{count}.png")
    cv2.imwrite(filename, img_rgb)
    return filename

# Main flight loop to capture data
def capture_data_during_flight():
    count = 0
    try:
        # Fly along the specified path
        print("flying on path...")
        result = client.moveOnPathAsync([
            airsim.Vector3r(125, 0, z),
            airsim.Vector3r(125, -130, z),
            airsim.Vector3r(0, -130, z),
            airsim.Vector3r(0, 0, z)
        ], 12, 120, airsim.DrivetrainType.ForwardOnly, airsim.YawMode(False, 0), 20, 1)

        while True:
            # Get images from the drone's camera
            scene_response = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)])[0]
            segmentation_response = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Segmentation, False, False)])[0]
            
            # Save the scene image
            scene_filename = save_image(scene_response, count, "scene")
            
            # Save the segmentation image
            segmentation_filename = save_image(segmentation_response, count, "segmentation")
            
            count += 1
            time.sleep(1)  # Capture image every second

            # Check if the flight path is completed
            if result.result:
                break

    except KeyboardInterrupt:
        print("Data capture stopped")

# Start the data capture during flight
capture_data_during_flight()

# Move back to the start point before landing
client.moveToPositionAsync(0, 0, z, 1).join()
print("landing...")
client.landAsync().join()
print("disarming...")
client.armDisarm(False)
client.enableApiControl(False)
print("done.")