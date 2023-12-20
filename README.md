# Calc-ULTRA: Calculus Calculator

[![GPLv3 License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/license/mit/) 

> **Calculus made easy**

This is a multi-functional, user-friendly Calculus Calculator!

- Little Python background knowledge needed.
- Supports derivatives, antiderivatives, and definite integrals - with a graph!
- (Please FULL SCREEN your console/terminal for better experience!)


## Note

This is the Python script of the Calc-ULTRA calculator. For the Python package, visit https://github.com/sudoer-Huatao/calc_ultra. Most updates will be based there.


## Requirements

This program requires the `sympy`,  `numpy`, and `matplotlib` modules installed. Other required modules are built in to most Python IDEs.

## Warnings

### Error Messages

If your computer returns this error:

PermissionError: [Errno 1] Operation not permitted: '/Users/YOUR_USERNAME/../Calc-ULTRA_Calculus-Calculator-main/texts/main_screen.txt'

Please ensure that your current directory is the "Calc-ULTRA_Calculus-Calculator-main" folder, then run this command in the terminal to resolve the error:

`sudo python3 Calc-ULTRA.py`

This should resolve the issue. 😅

### Function limitations

Due to limitations of the SymPy module, **some functions cannot be integrated**. The Error Function `erf(x)` can be integrated in both indefinite integral and definite integral calculation, but the Absolute Value and Factorial functions are only available to definite integral calculations. Also, the factorial function cannot be graphed properly. Integration of composed functions are also limited due to SymPy limitations. While some composed functions work, others don't. 😟


## Acknowledgements

> Without them, this would be impossible

A general thank-you to all GitHub users who gave feedback and/or starred this repository. ⭐️
And... a SPECIAL THANK-YOU to @Haobot for troubleshooting and feedback! 👍❤️

This program was made using SymPy and SciPy for calculation and Matplotlib and NumPy for graphing.

## Gallery

DerivaCalc implicit derivative demo:
![derivacalc_demo](https://github.com/sudoer-Huatao/calc_ultra/assets/135504586/a0ddc731-f673-42fd-9729-e3573ae4e4a0 "derivacalc_demo")

InteCalc antiderivative demo:
![intecalc_demo](https://github.com/sudoer-Huatao/calc_ultra/assets/135504586/d5c6cf35-24e4-4687-bbb7-c16ebd8d1470 "intecalc_demo")

InteCalc definite integral with graph demo:
![intecalc_graph_demo](https://github.com/sudoer-Huatao/calc_ultra/assets/135504586/d3089d09-0ce8-44e6-86bd-3825254f1d52 "intecalc_graph_demo")

LimCalc limit demo:
![limcalc_demo](https://github.com/sudoer-Huatao/calc_ultra/assets/135504586/ab333d6c-f8ae-4039-b06c-132c1473770a "limcalc_demo")

## License

This project is licensed under the terms of the MIT license.
