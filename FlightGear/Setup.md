# This file contains the setup instructions for [FlightGear](https://www.flightgear.org/) simulator for UAVs simulations.

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

### 2. Download [FlightGear](https://www.flightgear.org/)

* Download and install the current stable release of flightgear from the official [site](https://www.flightgear.org/). 
* Install the python library for quickStart and accessing the APIs.
  ```
  pip3 install flightgear-python
  ```


### 3. Run the following script for connecting to aircraft and performing simulation

* Use the telnet connection
Paste the following configurations in the FlightGear Simulator’s Additional Settings
```
--telnet=socket,bi,60,localhost,5500,tcp
```

Following a python [script](scripts/flightgear_data_gen.py) that uses ``flightgear-python`` library to make a telnet connection to the simulator. In the script we change a few properties like throttle and elevation and then save the aircraft data like latitude, longitude and altitude(this is continuous data), data is stored in a csv file.
```
 python3 scripts/flightgear_data_gen.py

```

### 4. Results

Output is stored as a ``csv`` data file with aircraft and environment data at different time instances.
  [out/flight_data.csv](out/flight_data.csv)
