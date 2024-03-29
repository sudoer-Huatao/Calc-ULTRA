# (UNMAINTAINED REPO)calc-ultra

Visit <https://github.com/sudoer-Huatao/calc_ultra> for more info.

[![GPLv3 License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/license/mit/)

> **Calculus made easy**

The Calc-ULTRA calculus calculator, but as a module!

- Little Python background knowledge needed!

Supports:

- Derivatives
- Partials
- Implicit differentiation
- Antiderivatives
- Definite integrals
- Improper integrals

**NEW SINCE V1.2.1:** Graphs for differentiation and integrals are supported!

## Note

This is the module package of the Calc-ULTRA calculator. For the Python script of this package, visit <https://github.com/sudoer-Huatao/calc_ultra>

## Installation and Running

> Run the calculus calculator with a single line of code

Command line: `pip install calc-ultra`.
To run the calculator, import Calc-ULTRA as `calc_ultra` like so:

`from calc_ultra import main`

Make sure you have the latest version installed. For example, if the latest version is 1.0.2, type `pip install calc-ultra==1.0.2` to reinstall the module.

Demo (version used: v1.0.1):

<https://github.com/sudoer-Huatao/calc_ultra/assets/135504586/17170f6e-4d7a-42ef-8d1d-121cde82f26a>

## Requirements

This program requires the `sympy`,  `numpy`, and `matplotlib` modules installed. Other required modules are built in to most Python IDEs.

## Warnings

### Function limitations

Due to limitations of the SymPy module, **some functions cannot be integrated**. The Error Function `erf(x)` can be integrated in both indefinite integral and definite integral calculation, but the Absolute Value and Factorial functions are only available to definite integral calculations. Also, the factorial function cannot be graphed properly. Integration of composed functions are also limited due to SymPy limitations. While some composed functions work, others don't. 😟

## Test PYPI

Previous test version of this project is on Test PYPI. View on <https://test.pypi.org/project/calc-ultra/>.

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
