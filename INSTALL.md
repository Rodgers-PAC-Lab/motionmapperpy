# Installation instructions

## Clone repository

Be sure not to clone to a location on PYTHONPATH. 

```
cd ~/installed
git clone git@github.com:Rodgers-PAC-Lab/motionmapperpy 
cd ~/installed/motionmapperpy
```

## Remove any pre-existing mmpy environment

This step is optional, but recommended if things are not working. Be careful - only run this line if you want to remove your current environment.

```
conda env remove -n mmpy
```

## Install the environment

```
# Create a new environment called mmpy and install everything into it
conda env create -f environment.yml 

# Activate it
conda activate mmpy
```

Optional installs afterward

```
conda install ipython pyqt pandas pytz
```

## Set XLA flags

Often this is necessary with conda to avoid "libdevice not found at ./libdevice.10.bc"

```
conda env config vars set XLA_FLAGS="--xla_gpu_cuda_data_dir=$CONDA_PREFIX" -n mmpy
```

## Run the demo

```
cd ~/installed/motionmapperpy/demo
python3 demo.py
```
