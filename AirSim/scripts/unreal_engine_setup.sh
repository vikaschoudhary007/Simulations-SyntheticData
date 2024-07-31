#!/bin/sh

# this option might not work you will have to connect your github account to EpicGames in order to download Unreal Engine from github
#git clone -b 5.4 https://github.com/EpicGames/UnrealEngine

cd UnrealEngine

./Setup.sh

./GenerateProjectFiles.sh

make

echo "Unreal Engine Setup is Done"