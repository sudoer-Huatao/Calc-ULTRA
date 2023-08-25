from sympy.utilities.lambdify import lambdify
from sympy import *
import sympy as sp
from scipy.integrate import *
# from scipy import integrate
from math import *
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import warnings


# This program requires the Sympy, SciPy, NumPy, and MatPlotLib modules!

warnings.filterwarnings("ignore")

def main():
    print("\nsudoer-Huatao Proudly Presents ... ... ...\n")
    print("\n   -------------------------------------------------------------------------")
    print("\n  +----      ^      |       +----      |   |  |    --+--  +---+      ^      |")
    print("  |         / \     |       |          |   |  |      |    |   |     / \     |")
    print("  |        / - \    |       |      --  |   |  |      |    |---+    / - \    |")
    print("  |       /     \   |       |          |   |  |      |    |  \    /     \ ")
    print("  +----  /       \  +----+  +----      +---+  +----  |    |   \  /       \  0")
    print("\n   -------------------------------------------------------------------------")
    print("\n               ------------------------------------------------")
    print("              | The ULTIMATE Derivative - Integral Calculator! |")
    print("               ------------------------------------------------")
    print("\nCommands:\n\n - Type '1' to access DerivaCalc, the Derivative Calculator!")
    print(" - Type '2' to access InteCalc, the Integral Calculator!")
    print(" - Type 'exit' to quit Calc-ULTRA")
    while True:
        print("\n(Current Screen: Main Screen)\n")
        cmd_main = input("Enter Command: ")
        if cmd_main == "1":
            deriv()
        elif cmd_main == "2":
            integ()
        elif cmd_main == "exit":
            print("\nExiting Calculator ... ... ...\n")
            break
            quit()
        else:
            print("\nError 001: Unknown command.")

'''
Hey, you! Stop looking at my code, copycats! Quit the code now!

Just kidding. Have fun with the calculator! - h.t.
'''


def deriv():
    print("\n\n   ---------------------------------------------------------------------------")
    print("\n  +---   +----  +---+  --+--  \       /   ^      +----      ^      |      +----")
    print("  |   |  |      |   |    |     \     /   / \     |         / \     |      |")
    print("  |   |  |---   |---+    |      \   /   / - \    |        / - \    |      |")
    print("  |   |  |      |  \     |       \ /   /     \   |       /     \   |      |")
    print("  +---   +----  |   \  --+--      v   /       \  +----  /       \  +----  +----\n")
    print("   ---------------------------------------------------------------------------\n")
    print("                            The Derivative Calculator\n")
    print("\nThis calculator supports:\n - Special numbers including Pi and e;")
    print(" - Basic Trigonometric Functions;\n - Exponents and Logarithms (input format: log<base>(x));")
    print(" - Inverse Trigonometric Functions (input format: 'a' followed by a trigonometric function, e.g. asin(x) = arcsin(x));")
    print(" - Hyperbolic Functions and Inverse Hyperbolic Functions (same input format as inverse trigonometric functions);")
    print(" - Other Functions such as the Factorial function factorial(x), the Error Function erf(x) and more!")
    print("(Full list available on https://docs.python.org/3/library/math.html)\n")
    print("\nCommands:\n", "\n - Type 'start' in the main screen to start the calculator!")
    print(" - Type 'help' in the main screen for a list of operations in Python;")
    print(" - Type 'exit' to quit DerivaCalc")
    print("(This version only supports single variable calculus)")
    while True:
        try:
            print("\n(Current Screen: DerivaCalc Main Screen)\n")
            cmd = input("Enter Command: ")
            if cmd == "help":
                print("\nBasic operations: \n", "+: add \n", "-: minus \n", "*: multiply \n", "/: divide \n", "**: exponent")
                print("%: return the remainder of a division \n", "//: return the rounded-down quotient of a division")
            elif cmd == "start":
                print("\n(Current Screen: Derivative Screen)\n")
                f = input("Enter a function: ")
                if ("^" in f):
                    f= f.replace("^", "**")
                x = symbols("x")
                df = diff(f, x)
                print("\nDerivative is", df)
                dsimp = input("\nSimplify? (y/n) ")
                if dsimp == "y":
                    print("\nSimplified:", df, "-->", sp.simplify(df, evaluate = False))
                else:
                    break
            elif cmd == "exit":
                print("\nExiting Calculator ... ... ...")
                break
                quit()
            else:
                print("\nError 002: Invalid command.")
        except:
            print("\nError 001: An unknown error occured.\n")


def integ():
    print("\n\n   ------------------------------------------------------------")
    print("\n  --+--  |\    |  ---+---  +----  +----      ^      |      +----")
    print("    |    | \   |     |     |      |         / \     |      |")
    print("    |    |  \  |     |     +---   |        / - \    |      |")
    print("    |    |   \ |     |     |      |       /     \   |      |")
    print("  --+--  |    \|     |     +----  +----  /       \  +----  +----")
    print("\n   ------------------------------------------------------------")
    print("\n                      The Integral Calculator\n")
    print("\nThis calculator supports:\n - Special numbers including Pi and e;")
    print(" - Basic Trigonometric Functions;\n", "- Exponents (for exponent with base e, input as 'exp(x)', NOT e**x);")
    print(" - The Natural Logarithm (input as log(x));")
    print(" - Inverse Trigonometric Functions (input format: 'a' followed by a trigonometric function, e.g. asin(x) = arcsin(x));")
    print(" - Hyperbolic Functions and Inverse Hyperbolic Functions (same input format as inverse trigonometric functions);")
    print("(Full list of Python Math functions available on https://docs.python.org/3/library/math.html)\n")
    print("\nCommands:\n", "\n - Type 'istart' in the main screen to start the antiderivative (indefinite integral) calculator!")
    print(" - Type 'dstart' in the main screen to start the definite integral calculator with a graph!")
    print(" - Type 'help' in the main screen for a list of operations in Python")
    print(" - Type 'exit' to quit InteCalc")
    print("\n  -----------------------------------------------------------------------------------------------")
    print(" | (This calculator DOES NOT support Factorials, Absolute Value Functions, and other functions!) |")
    print("  -----------------------------------------------------------------------------------------------")
    while True:
        try:
            print("\n(Current Screen: InteCalc Main Screen)\n")
            cmd = input("Enter Command: ")
            if cmd == "help":
                print("\nBasic operations: ", "\n+: add \n", "-: minus \n", "*: multiply \n", "/: divide \n", "**: exponent")
                print("%: return the remainder of a division \n", "//: return the rounded-down quotient of a division")
            elif cmd == "istart":
                print("\n(Current Screen: Antiderivative Screen)\n")
                f = input("Enter a function: ")
                if ("pi" in f):
                    f = f.replace("pi", str(math.pi))
                if ("^" in f):
                    f = f.replace("^", "**")
                else:
                    str(f)
                x = sp.Symbol("x")
                print("\nAntiderivative is:", sp.integrate(f, x), "+ C")
                isimp = input("\nSimplify? (y/n) ")
                if isimp == "y":
                    print("\nSimplified: ", sp.integrate(f, x), "-->", simplify(sp.integrate(f,x), evaluate = False))
                else:
                    break
            elif cmd == "dstart":
                print("\n(Current Screen: Definite Integral Screen)\n")
                def d_integrate():
                    def g(x):
                        final = eval(f)
                        return final
                    f = input("Enter the function you want to integrate: ")
                    if ("^" in f):
                        f = f.replace("^", "**")
                    lbound = input("\nEnter the lower bound: ")
                    if ("pi" in lbound):
                        lbound = lbound.replace("pi", str(math.pi))
                        lbound = float(lbound)
                    elif ("e" in lbound):
                        lbound = lbound.replace("e", str(math.e))
                        lbound = float(lbound)
                    else:
                        lbound = float(lbound)
                    rbound = input("Enter the upper bound: ")
                    if ("pi" in rbound):
                        rbound = rbound.replace("pi", str(math.pi))
                        rbound = float(rbound)
                    elif ("e" in rbound):
                        rbound = rbound.replace("e", str(math.e))
                        rbound = float(rbound)
                    else:
                        rbound = float(rbound)
                    if (("1/x" in f or f == "x^-1") and (lbound <= 0 or lbound <= lbound + 1)):
                        return("\nDiverging integral. Cannot solve.")
                    x = sp.Symbol("x")
                    print("\nCalculated integral of", f, "from", lbound, "to", rbound, ". Final area is", sp.integrate(f, (x, lbound, rbound)))
                    print("\nShow graph of area? (y/n)")
                    show = input("(Exit the graph window when you are finished to continue) ")
                    if show == "y":
                        print("\nLoading graph. Might take some time ...")
                        x = np.linspace((lbound - 8), (rbound + 8), 200000)
                        if ("ln" in f or "log" in f):
                            x = np.linspace(int(math.floor(lbound)) + 1, int(math.ceil(rbound)) + 8, 200000)
                        y = [g(a) for a in x]
                        fig, ax = plt.subplots()
                        plt.xlabel("$x$")
                        plt.ylabel("$f(x)$")
                        plt.grid()
                        plt.plot(x,y, color = "red")
                        ix = np.linspace(lbound, rbound)
                        iy = [g(i) for i in ix]
                        verts = [(lbound, 0)] + list(zip(ix, iy)) + [(rbound, 0)]
                        poly = Polygon(verts, facecolor = "blue")
                        ax.add_patch(poly)
                        plt.show()
                        return "\nExited graph."
                    elif show == "n":
                        return "\nExiting Definite Integral Screen ...\n"
                print(d_integrate())
            elif cmd == "exit":
                print("\nExiting Calculator ... ... ...")
                break
                quit()
            else:
                print("\nError 002: Invalid command.")
        except:
            print("\nError 001: An unknown error occured.")


main()
