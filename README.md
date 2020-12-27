# ERC-project
The growth_model.py file represents the model of the growth of Pseudomonas putida lysis strain with pS221Lys device.
The program calculates the time course of bacterial growth (growth curve) and substrate concentration based on the input values (initial substrate concentration, specific growth rate, the length lag phase, biomass yield, time of the induction of the Switch module).

The bacterial growth curve is calculated using the modified Gompertz equation ([Zwietering et al., 1990](https://pubmed.ncbi.nlm.nih.gov/16348228/)):

<a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;Aexp&space;[-exp[\mu&space;_{m}*e&space;*&space;(\lambda&space;-&space;t)/A&space;&plus;&space;1]]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;Aexp&space;[-exp[\mu&space;_{m}*e&space;*&space;(\lambda&space;-&space;t)/A&space;&plus;&space;1]]" title="y = Aexp [-exp[\mu _{m}*e * (\lambda - t)/A + 1]]" /></a>

where
<br/>e=exp(1),
<br/><a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\mu&space;_{m}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\mu&space;_{m}" title="\mu _{m}" /></a> = the maximum specific growth rate,
<br/><a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\lambda" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\lambda" title="\lambda" /></a> = lag time,
<br/>A = the maximal value reached.

The substrate concentration in time is calculated using the equation:

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;S}{\mathrm{d}&space;t}&space;=&space;\frac{1}{Y}&space;\frac{\mathrm{d}&space;X}{\mathrm{d}&space;t}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\mathrm{d}&space;S}{\mathrm{d}&space;t}&space;=&space;\frac{1}{Y}&space;\frac{\mathrm{d}&space;X}{\mathrm{d}&space;t}" title="\frac{\mathrm{d} S}{\mathrm{d} t} = \frac{1}{Y} \frac{\mathrm{d} X}{\mathrm{d} t}" /></a>

where 
<br/>S = substrate concentartion, <br/>X = cell concentration, <br/>Y = yield coeficient.



## Requirements
* Python 3
* NumPy library
```
python -m pip install numpy
```
* Matplotlib library
```
python -m pip install matplotlib
```
