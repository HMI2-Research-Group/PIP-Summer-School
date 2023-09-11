# Installation
## softwares to be installed ahead
- Anaconda
- VS Code

both of them are very important. If any issues please contact the instructor. 


Assuming you have windows or linux laptop blow are the commands to be executed in an anaconda prompt shell. The anaconda prompt shell varies upon distributions. For windows search ```anaconda shell```. For linux you have to activate the anaconda environment and when you activate it it should give output a *non empty output* for

```bash
which conda
```

```bash
conda create -n pip_summer_school -y -c conda-forge jupyterlab=3 "ipykernel>=6" xeus-python python=3.8
conda activate pip_summer_school
conda install -y scipy
conda install -y -c conda-forge pandas
conda install -y -c conda-forge scikit-learn
conda install -y -c conda-forge statsmodels
conda install -y -c conda-forge matplotlib
conda install -y -c conda-forge seaborn
```

## Extra Tips
Figure out how to replicate the environment with Poetry. Should take 10 minutes. 