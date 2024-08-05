# This file contains the setup instructions for [JSBSim](https://jsbsim.sourceforge.net/index.html) simulator for UAVs simulations.

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

### 2. Download [JSBSim](https://jsbsim.sourceforge.net/index.html)

* Clone JSBSim repository from [github](https://github.com/JSBSim-Team/jsbsim) for full source code.
* Install the python library for quickStart and accessing the APIs.
  ```
  pip install jsbsim
  ```

### 3. Run the following script for starting the flight dynamic module(simulated environment)

```
 JSBSim.exe --script=scripts/c1721.xml

 # to see more command option
 JSBSim.exe --help
```

### 4. Sample python code to interact with the python module of JSBSim

Providing ``jsbsim.FGFDMExec`` with the value ``None`` in the ``Sample`` script [scripts/Sample.py](scripts/Sample.py) allows using the installed default aircraft data and scripts.

  ```
  # Execute the Sample script [scripts/Sample.py](scripts/Sample.py)
  # it uses default FDM script scripts/c1723.xml
  python3 Sample.py
  ```
* Output/data after executing the above script with default configuration
  Following events occurs after the scripted is executed

  - Multiple configuration files are executed in order to load the initial aircraft and simulation environment.
  - Time Notify(event), provides information at a particular time instance before the engine starts.
  - Engine starts
  - Rolling/rotating - take off event of an aircraft
  - Multiple Time Notifications
  - Autopilot settings
* Output is stored as a ``csv`` data file with aircraft and environment data at different time instances.
  [out/JSBout172B.csv](scripts/Sample.py)

### 5. In order to get the path of directory where default aircraft data is located use the following command :-

```
 print(jsbsim.get_default_root_dir())
```
