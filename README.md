# Calc-ULTRA: Calculus Calculator

[![GPLv3 License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/license/mit/) [![Version](https://img.shields.io/badge/Version-2.2.5-blue.svg)](https://github.com/sudoer-Huatao/Calc-ULTRA_Calculus-Calculator)

This is a multi-functional, user-friendly Calculus Calculator!

- Little Python background knowledge needed.
- Supports derivatives, antiderivatives, and definite integrals - with a graph!
- (Please FULL SCREEN your console/terminal for better experience!)


### Note:
This is the Python script of the Calc-ULTRA calculator. For the Python package, visit https://github.com/sudoer-Huatao/calc_ultra.

## How to Run

Simply open the Calc-ULTRA.py file, and then run it.


## Requirements

This program requires `sympy`,  `numpy`, `matplotlib`, `datetime`, `math`, `logging`, `warnings` and `os` modules. `datetime`, `math`, `logging`, `warnings` and `os` are built-in to most Python editors. 

## Warnings!!!

### Error Messages:

If your computer returns this error:

PermissionError: [Errno 1] Operation not permitted: '/Users/YOUR_USERNAME/../Calc-ULTRA_Calculus-Calculator-main/texts/main_screen.txt'

Please ensure that your current directory is the "Calc-ULTRA_Calculus-Calculator-main" folder, then run this command in the terminal to resolve the error:

`sudo python3 Calc-ULTRA.py`

This should resolve the issue. 😅

### Function limitations:

Due to limitations of the SymPy module, **some functions cannot be integrated**. The Error Function `erf(x)` can be integrated in both indefinite integral and definite integral calculation, but the Absolute Value and Factorial functions are only available to definite integral calculations. Also, the factorial function cannot be graphed properly. Integration of composed functions are also limited due to SymPy limitations. While some composed functions work, others don't. 😟


# Acknowledgements

A general thank-you to all GitHub users who gave feedback and/or starred this repository. ⭐️
And... a SPECIAL THANK-YOU to @Haobot for troubleshooting and feedback! 👍❤️

This program was made using SymPy and SciPy for calculation and Matplotlib and NumPy for graphing.

# Gallery

DerivaCalc implicit derivative demo:
<img width="1685" alt="derivacalc_demo" title="Derivacalc" src="https://github.com/sudoer-Huatao/calc_ultra/assets/135504586/a0ddc731-f673-42fd-9729-e3573ae4e4a0">

InteCalc antiderivative demo:
<img width="1685" alt="intecalc_demo" src="https://github.com/sudoer-Huatao/calc_ultra/assets/135504586/d5c6cf35-24e4-4687-bbb7-c16ebd8d1470">

InteCalc definite integral with graph demo:
<img width="1710" alt="graph_demo" src="https://github.com/sudoer-Huatao/calc_ultra/assets/135504586/d3089d09-0ce8-44e6-86bd-3825254f1d52">

LimCalc limit demo:
<img width="1685" alt="limcalc_demo" src="https://github.com/sudoer-Huatao/calc_ultra/assets/135504586/ab333d6c-f8ae-4039-b06c-132c1473770a">


# License

This project is licensed under the terms of the MIT license.
