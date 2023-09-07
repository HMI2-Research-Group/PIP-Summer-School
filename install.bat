@echo off

title Install Script!
echo Installing...
conda create -n pip_summer_school -y -c conda-forge jupyterlab=3 "ipykernel>=6" xeus-python python=3.8
conda activate pip_summer_school
conda install -y scipy
conda install -y -c conda-forge pandas
conda install -y -c conda-forge scikit-learn
conda install -y -c conda-forge statsmodels
conda install -y -c conda-forge matplotlib
conda install -y -c conda-forge seaborn
