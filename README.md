# Installation
## softwares to be installed ahead
- [Anaconda](https://www.anaconda.com/download)
- [VS Code](https://code.visualstudio.com/)

Tip: Always use VS Code. It's the best IDE and please try to prove me wrong. 

Both of the softwares are very important. If any issues installing them please contact the instructor. 


Assuming you have windows or linux laptop below are the commands to be executed in an anaconda prompt shell. The anaconda prompt shell varies upon distributions. For windows search ```anaconda shell```. For linux you have to activate the anaconda environment and when you activate it it should give output a *non empty output* for

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
```

Quick Tip: The python version is 3.8 so that you can use walrus operator. You are welcome!

