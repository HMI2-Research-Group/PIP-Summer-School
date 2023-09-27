# Installation
## softwares to be installed ahead
- [Anaconda](https://www.anaconda.com/download)
- [VS Code](https://code.visualstudio.com/)

Tip: VS Code has the best IDE.

Both of the software are very important. If any issues installing them please contact the instructor. 


Assuming you have a Windows or Linux laptop below are the commands to be executed in an anaconda prompt shell. The anaconda prompt shell varies upon distribution. For Windows search ```anaconda shell```. For Linux, you have to activate the anaconda environment and when you activate it should give the output a *non empty output* for

```bash
which conda
```
and then please install by executing everything line by line:
```bash
conda create -n pip_summer_school -y -c conda-forge jupyterlab=3 "ipykernel>=6" xeus-python python=3.8
conda activate pip_summer_school
conda install -y scipy
conda install -y -c conda-forge pandas
conda install -y -c conda-forge scikit-learn
conda install -y -c conda-forge statsmodels
conda install -y -c conda-forge matplotlib
conda install -y -c conda-forge seaborn
conda install -c conda-forge shap
```

To activate the newly created environment, please execute the following command:
```bash
conda activate pip_summer_school
```
The environment needs to be activated before you install any new packages or use the virtual environment.

Quick Tip: The Python version is 3.8 so you can use the walrus operator. 

The workshop will use the YAHBOOM IMU sensor. Please refer to

 - [YAHBOOM IMU](https://github.com/YahboomTechnology/10-axis_IMU_Module)
 - [Annex Download](https://drive.google.com/drive/u/1/folders/1XkIL0RvOkqZD_GbHdTRHtLtMkgXIC3lu)

 - You also need CP2102 Driver
