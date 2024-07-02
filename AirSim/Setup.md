# This file contains the setup instructions for AirSim simulator specifically for autonomous drone simulations.

### 1. **Install and setup conda environment**

* Download the installer for linux
* ```
  sudo apt-get update

  # install prerequisite libraries
  apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

  # following two steps are for your downloadedFile
  Shasum -a 256 ./Anaconda_downloaded_file.sh

  Chmod +x ./Anaconda_downloaded_file.sh

  source ~/.bashrc 

  conda -version
  ```

### 2.  Install and setup Unreal Engine

* Connect github to EpicGames account and download Unreal Engine for Linux
* Execute the ``unreal_engine_setup.sh`` file from scripts folder.

### 3. Download AirSim

* Clone AirSim repository from [github](https://github.com/microsoft/AirSim)
* Make the following changes to build - [Follow this youtube video](https://www.youtube.com/watch?v=jJ4mqo4Ge8U&t=585s)
* Execute ``airsim_setup.sh`` file from scripts folder.

### 4. Download Binaries

* For Linux - [Link](https://github.com/Microsoft/AirSim/releases)

### 5. Run Simulation

* ```
  # Run the binary file to start neighbourhood simulation enviroment of AirSim
  chmod +x ./AirSimNH.sh 
  ./AirSimNH.sh -windowed
  ```
* **Script for drone simulation and data capturing**
  The ``path.py`` file in scripts is present inside ``AirSim/PythonClient/multirotor`` folder, execute this file to run simulation and generate synthetic data from cameras.
* ``setings.json`` file is created once you start the bianry for the first time, see the [docs](https://microsoft.github.io/AirSim/settings/) to make chnages. the one I use is present in the scripts folder.
* This step will generate image data from drone sensors(depth, segmentation and original image data)
*
