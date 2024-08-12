# This file contains the setup instructions for Infinigen simulator specifically for indoor scene generation.

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

### 2. Infinigen Simulator Installation Guide

### Install Infinigen - follow [instructions](https://github.com/princeton-vl/infinigen/blob/main/docs/Installation.md) for installation as a Python Module

```
# on Ubuntu / Debian / WSL / etc
sudo apt-get install wget cmake g++ libgles2-mesa-dev libglew-dev libglfw3-dev libglm-dev zlib1g-dev

# on conda, Useful when you don't have sudo permissions
conda install conda-forge::gxx=11.4.0 mesalib glew glm menpo::glfw3
export C_INCLUDE_PATH=$CONDA_PREFIX/include:$C_INCLUDE_PATH
export CPLUS_INCLUDE_PATH=$CONDA_PREFIX/include:$CPLUS_INCLUDE_PATH
export LIBRARY_PATH=$CONDA_PREFIX/lib:$LIBRARY_PATH
export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH

git clone https://github.com/princeton-vl/infinigen.git
cd infinigen
conda create --name infinigen python=3.10
conda activate infinigen
```

**This tutorial is on full install**
```
# Minimal install (No terrain or opengl GT, ok for Infinigen-Indoors or single-object generation) 
INFINIGEN_MINIMAL_INSTALL=True pip install -e .

# Full install (Terrain & OpenGL-GT enabled, needed for Infinigen-Nature HelloWorld)
pip install -e .

# Developer install (includes pytest, ruff, other recommended dev tools)
pip install -e ".[dev]"
```

### 3.1 Running Hello World Example - Natural Scene
* **After each command completes you can inspect its --output_folder for results.**

  ```
  mkdir outputs

  # Generate a scene layout
  python -m infinigen_examples.generate_nature --seed 0 --task coarse -g desert.gin simple.gin --output_folder outputs/hello_world/coarse

  # Populate unique assets
  python -m infinigen_examples.generate_nature --seed 0 --task populate fine_terrain -g desert.gin simple.gin --input_folder outputs/hello_world/coarse --output_folder outputs/hello_world/fine

  # Render RGB images
  python -m infinigen_examples.generate_nature --seed 0 --task render -g desert.gin simple.gin --input_folder outputs/hello_world/fine --output_folder outputs/hello_world/frames

  # Render again for accurate ground-truth
  python -m infinigen_examples.generate_nature --seed 0 --task render -g desert.gin simple.gin --input_folder outputs/hello_world/fine --output_folder outputs/hello_world/frames -p render.render_image_func=@flat/render_image 

  ```

**Results are in `out/helloworld_outdoor` folder**
  
#### Image
![Sample Original Image Data](out/helloWorld_outdoor/Image_0_0_0001_0.png)

#### Ambient Occlusion
![Ambient Occlusion](out/helloWorld_outdoor/AO_0_0_0001_0.png)

#### Instance Segmentation
![Instance Segmentation](out/helloWorld_outdoor/InstanceSegmentation_0_0_0001_0.png)

#### Object Segmentation
![Object Segmentation](out/helloWorld_outdoor/ObjectSegmentation_0_0_0001_0.png)

#### Surface Normal
![Surface Normal](out/helloWorld_outdoor/SurfaceNormal_0_0_0001_0.png)

#### VolumeDir
![VolumeDir](out/helloWorld_outdoor/VolumeDir_0_0_0001_0.png)

#### GlossInd
![GlossInd](out/helloWorld_outdoor/GlossInd_0_0_0001_0.png)

#### Depth
![Depth](out/helloWorld_outdoor/Depth_0_0_0001_0.png)
  

#### Ground-Truth Annotations - Extended Hello-World

* **To generate the hello-world scene using custom annotation system, run:**
  ```
  python -m infinigen.datagen.manage_jobs --output_folder outputs/hello_world/0 --num_scenes 1 --specific_seed 0 \
  --configs desert.gin simple.gin --pipeline_configs local_16GB.gin monocular.gin opengl_gt.gin --pipeline_overrides LocalScheduleHandler.use_gpu=False
  ```


### 3.2 Hello World Example - Infinigen-Indoors scene
#### To generate a `single scene` in one command, you can run the following:
* **After each command completes you can inspect its --output_folder for results.**
  ```
  screen python -m infinigen.datagen.manage_jobs --output_folder outputs/indoor --num_scenes 1000 --pipeline_configs local_256GB.gin monocular.gin blender_gt.gin indoor_background_configs.gin --configs singleroom.gin --pipeline_overrides get_cmd.driver_script='infinigen_examples.generate_indoors' manage_datagen_jobs.num_concurrent=16 --overrides compose_indoors.restrict_single_supported_roomtype=True
  ```

**Results are in `out/helloworld_indoor` folder**
  
#### Image
![Sample Original Image Data](out/helloWorld_indoor/Image.png)

#### Ambient Occlusion
![Ambient Occlusion](out/helloWorld_indoor/AO.png)

#### Instance Segmentation
![Instance Segmentation](out/helloWorld_indoor/InstanceSegmentation.png)

#### Object Segmentation
![Object Segmentation](out/helloWorld_indoor/ObjectSegmentation.png)

#### Surface Normal
![Surface Normal](out/helloWorld_indoor/SurfaceNormal.png)

#### VolumeDir
![VolumeDir](out/helloWorld_indoor/VolumeDir.png)

#### GlossCol
![GlossCol](out/helloWorld_indoor/GlossCol.png)

#### Depth
![Depth](out/helloWorld_indoor/Depth.png)


### 3.3 Hello World Example - Infinigen-Indoors scene
#### To create a `large dataset of many random rooms`:
* **After each command completes you can inspect its --output_folder for results.**
  ```
  screen python -m infinigen.datagen.manage_jobs --output_folder outputs/my_dataset --num_scenes 1000 --pipeline_configs local_256GB.gin monocular.gin blender_gt.gin indoor_background_configs.gin --configs singleroom.gin --pipeline_overrides get_cmd.driver_script='infinigen_examples.generate_indoors' manage_datagen_jobs.num_concurrent=16 --overrides compose_indoors.restrict_single_supported_roomtype=True
  ```

**Results are in `out/indoor_multi` folder for single scene generation**  
  
#### Image
![Sample Original Image Data](out/indoor_multi/Image.png)

#### Ambient Occlusion
![Ambient Occlusion](out/indoor_multi/AO.png)

#### Instance Segmentation
![Instance Segmentation](out/indoor_multi/InstanceSegmentation.png)

#### Object Segmentation
![Object Segmentation](out/indoor_multi/ObjectSegmentation.png)

#### Depth
![Depth](out/indoor_multi/Depth.png)

### 3.4 Hello World Example - Infinigen-Indoors scene
#### To create a large dataset of `multistory building`:
* **After each command completes you can inspect its --output_folder for results.**
  ```
  screen python -m infinigen.datagen.manage_jobs --output_folder outputs/multistory --num_scenes 1000 --pipeline_configs local_256GB.gin monocular.gin blender_gt.gin indoor_background_configs.gin --configs multistory.gin --pipeline_overrides get_cmd.driver_script='infinigen_examples.generate_indoors' manage_datagen_jobs.num_concurrent=16 --overrides compose_indoors.restrict_single_supported_roomtype=True

  ```


### 4. Infinigen Simulator Installation Guide

#### See [ExportingToExternalFileFormats](https://github.com/princeton-vl/infinigen/blob/main/docs/ExportingToExternalFileFormats.md) and [ExportingToSimulators](https://github.com/princeton-vl/infinigen/blob/main/docs/ExportingToSimulators.md) to export to OBJ/USD.


### 5.1 Installing Infinigen as a Blender Python script

```
git clone https://github.com/princeton-vl/infinigen.git
cd infinigen
```

```
# Minimal installation (recommended setting for use in the Blender UI)
INFINIGEN_MINIMAL_INSTALL=True bash scripts/install/interactive_blender.sh

# Normal install (includes CPU Terrain, and CUDA Terrain if available)
bash scripts/install/interactive_blender.sh

# Enable OpenGL GT
INFINIGEN_INSTALL_CUSTOMGT=True bash scripts/install/interactive_blender.sh
```

### 5.2 Generate scenes in one command
#### INFINIGEN provides infinigen/datagen/manage_jobs.py, a utility which runs similar steps automatically.

```
conda activate infinigen

python -m infinigen.datagen.manage_jobs --output_folder outputs/hello_world --num_scenes 1 --specific_seed 0 \
--configs desert.gin simple.gin --pipeline_configs local_16GB.gin monocular.gin blender_gt.gin --pipeline_overrides LocalScheduleHandler.use_gpu=False

```

### 6. Ground Truth Extractor 
#### Infinigen also provides an OpenGL-based ground truth extractor which offers additional ground truth channels, read more about using our ground truth [here](https://github.com/princeton-vl/infinigen/blob/main/docs/GroundTruthAnnotations.md).

