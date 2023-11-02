# Calc-ULTRA: Calculus Calculator

[![GPLv3 License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/) [![Version](https://img.shields.io/badge/Version-5.0.4-blue.svg)](https://github.com/sudoer-Huatao/Calc-ULTRA_Calculus-Calculator)

This is a multi-functional, user-friendly Calculus Calculator!

- No Python background knowledge needed.
- Supports derivatives, antiderivatives, and definite integrals - with a graph!
- (Please FULL SCREEN your console/terminal for better experience!)

<img width="1641" alt="截屏2023-10-26 15 49 25" src="https://github.com/sudoer-Huatao/Calc-ULTRA_Calculus-Calculator/assets/135504586/163fe4df-2945-4b18-8f67-286871b9bacb">

## Requirements

This program requires the Sympy, SciPy, NumPy, and MatPlotLib modules.

<img width="1641" alt="截屏2023-10-26 15 51 54" src="https://github.com/sudoer-Huatao/Calc-ULTRA_Calculus-Calculator/assets/135504586/9b1efdb8-554d-4412-8834-4d2dec49f750">

# Warnings!!!

If your computer returns this error:

`PermissionError: [Errno 1] Operation not permitted: '/Users/YOUR_USERNAME/../Calc-ULTRA_Calculus-Calculator-main/texts/main_screen.txt'`

Please ensure that your current directory is the "Calc-ULTRA_Calculus-Calculator-main" folder, then run this command in the terminal to resolve the error:

`sudo python3 Calc-ULTRA.py`

This should resolve the issue.


Due to limitations of the SymPy module, SOME FUNCTIONS CAN NOT BE INTEGRATED. The Error Function erf(x) can be integrated in both indefinite integral and definite integral calculation, but the Absolute Value and Factorial functions are only available to definite integral calculations. Also, the factorial function cannot be graphed properly. Integration of composed functions are also limited due to SymPy limitations. While some composed functions work, others don't.

## How to run

To run this project, simply open the Calc-ULTRA.py file and run it.

# Acknowledgements

A general thank-you to all GitHub users who gave feedback and/or starred this repository,
and a SPECIAL THANK-YOU to @Haobot for troubleshooting and feedback!

This program was made using SymPy and SciPy for calculation and Matplotlib and NumPy for graphing.

# License

This project is licensed under the terms of the MIT license.
