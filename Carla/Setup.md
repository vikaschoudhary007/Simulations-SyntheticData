# This file contains the setup instructions for CARLA simulator specifically for simulations and synthetic data.

### 1. **Install and setup conda environment**

* Download the installer for linux
  ```
  sudo apt-get update

  # install prerequisite libraries
  apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

  # following two steps are for your downloadedFile
  Shasum -a 256 ./Anaconda_downloaded_file.sh

  Chmod +x ./Anaconda_downloaded_file.sh

  source ~/.bashrc 

  conda -version
  ```
* Create a conda environment
  ```
  #create conda env
  conda create --name carla_env python=3.9
  conda activate carla_env
  ```

### 2. CARLA Simulator Installation Guide

### Prerequisites

Before you begin, ensure that your system meets the requirements.

#### Check Python & Pip Version

```
#For Python 3:
pip3 -V

#For Python 2 
pip -V
```

#### If you want to upgrade

```
# For Python 3
 pip3 install --upgrade pip

 # For Python 2
 pip install --upgrade pip

```

#### Install numpy

```
pip install --user pygame numpy &&
pip3 install --user pygame numpy

```

### 3. CARLA Installation

Download the stable release from [github](https://github.com/carla-simulator/carla/releases/tag/0.9.15)(this tutorial uses version 0.9.15)

Import additional assets

- [Download](https://github.com/carla-simulator/carla/blob/master/Docs/download.md) appropriate package as per your CARLA version
- Extract the package:
- move the package to the Import folder and run the following script to extract the contents:

```
 cd path/to/carla/root

 ./ImportAssets.sh
```

#### Install client library

```
# Python 3
 pip3 install carla
```

#### Running CARLA

```
cd path/to/carla/root

./CarlaUE4.sh

```

This is the server simulator which is now running and waiting for a client to connect and interact with the world. You can try some of the example scripts to spawn life into the city and drive a car:

```
# Terminal A 
cd PythonAPI\examples

python3 -m pip install -r requirements.txt

# Support for Python2 is provided in the CARLA release packages

python3 generate_traffic.py  

# Terminal B
cd PythonAPI\examples

python3 manual_control.py

```

### 4. Run Simulation

* **Script for autonomous driving(auto pilot) simulation and data capturing**

  ```
  ./scrips/sensor_camera.ipynb
  ```
* **Results are in `out` folder**

![Sample Data Generated via Simulation](out/All%20Cameras_screenshot_23.07.2024.png)
