#!/bin/sh

cd AirSim

# following steps need to executed after making the changes as mentioned in setup.md file
./setup.sh

./build.sh

echo "AirSim Setup is Done"

pip install numpy

pip install airsim

pip install msgpack-rpc-python

echo "AirSim installation is Done"

