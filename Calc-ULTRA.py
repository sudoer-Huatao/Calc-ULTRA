from sympy import *
import sympy as sp
from math import floor, ceil
import numpy as np
import matplotlib.pyplot as plt
import pendulum
from matplotlib.patches import Polygon


# This program requires the Sympy, NumPy, Pendulum, and MatPlotLib modules!

def main():
    print("\nsudoer-Huatao Proudly Presents ... ... ...\n")
    print("\n   -------------------------------------------------------------------------")
    print("\n  +----      ^      |       +----      |   |  |    --+--  +---+      ^      |")
    print("  |         / \     |       |          |   |  |      |    |   |     / \     |")
    print("  |        / - \    |       |      --  |   |  |      |    |---+    / - \    |")
    print("  |       /     \   |       |          |   |  |      |    |  \    /     \ ")
    print("  +----  /       \  +-----  +----      +---+  +----  |    |   \  /       \  0")
    print("\n   -------------------------------------------------------------------------")
    print("\n               ------------------------------------------------")
    print("              | The ULTIMATE Derivative - Integral Calculator! |")
    print("               ------------------------------------------------")
    while True:
        now = pendulum.now()
        dt = now.format("Y-MM-DD HH:mm:ss")
        print("\n( Time now is:", dt, " )")
        print("\nCommands:\n\n - Type '1' to access DerivaCalc, the Derivative Calculator!")
        print(" - Type '2' to access InteCalc, the Integral Calculator!")
        print(" - Type '3' to access LimCalc, the Limit Calculator!")
        print(" - Type 'exit' to quit Calc-ULTRA")
        print("\n(Current Screen: Main Screen)\n")
        cmd_main = input("Enter Command: ")
        if cmd_main == "1":
            deriv()
        elif cmd_main == "2":
            integ()
        elif cmd_main == "3":
            take_lim()
        elif cmd_main == "exit":
            print("\nExiting Calc-ULTRA ... ... ...\n")
            break
        else:
            print("\nCommandError: '", cmd_main, "' is an invalid command")

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
    print("\nDerivaCalc supports:\n - Special numbers including Pi and e;")
    print(" - Basic Trigonometric Functions;\n - Exponents (for exponent with base e, input as 'exp(x)', NOT e**x);")
    print(" - The Natural Logarithm (input as log(x));")
    print(" - Inverse Trigonometric Functions (input as 'a' followed by a trigonometric function, e.g. asin(x) = arcsin(x));")
    print(" - Hyperbolic Functions and Inverse Hyperbolic Functions (same input format as inverse trigonometric functions);")
    print(" - Other Functions such as the Factorial function factorial(x), the Error Function erf(x) and more!")
    print("(Full list available on https://docs.python.org/3/library/math.html)\n")
    print("\nCommands:\n", "\n - Type 'd' in the main screen to calculate derivatives;")
    print(" - Type 'p' in the main screen to calculate partial derivatives;")
    print(" - Type 'help' in the main screen for a list of operations in Python;")
    print(" - Type 'exit' to quit DerivaCalc")
    print("\n(This version only supports single variable calculus)")
    while True:
        try:
            print("\n(Current Screen: DerivaCalc Main Screen)\n")
            cmd = input("Enter Command: ")
            if cmd == "help":
                print("\nBasic operations: \n", "+: add \n", "-: minus \n", "*: multiply \n", "/: divide \n", "**: exponent")
                print(" %: return the remainder of a division \n", "//: return the rounded-down quotient of a division")
            elif cmd == "d":
                print("\n(Current Screen: Derivative Screen)\n")
                opt = input("Choose option: normal derivative computation ('n') or implicit derivative computation ('i'): ")
                if opt == "n":
                    f = input("\nEnter a function: ")
                    if ("^" in f):
                        f = f.replace("^", "**")
                    fnum = input("Enter the order of derivative calculation: ")
                    if fnum.isnumeric() == False:
                        print("\nTypeError: Order of derivative calculation is not a number.")
                    elif int(fnum) < 0:
                        print("\nOrderError: Order of derivative calculation is smaller than 0.")
                    else:
                        x = symbols("x")
                        df = diff(f, x, fnum)
                        print("\nDerivative of",f,"with order",fnum,"is:\n")
                        pprint(df)
                        if str(sp.simplify(df, evaluate = False)) != str(df):
                            dsimp = input("\nSimplification of answer found. Simplify? (y/n) ")
                            if dsimp == "y":
                                print("\nSimplified:", df, "into:\n")
                                pprint(sp.simplify(df, evaluate = False))
                elif opt == "i":
                    circ = input("\nEnter an equation containing x and y: ")
                    if ("^" in circ):
                        circ = circ.replace("^", "**")
                    fnum = input("Enter the order of derivative calculation: ")
                    if fnum.isnumeric() == False:
                        print("\nTypeError: Order of derivative calculation is not a number.")
                    elif int(fnum) < 0:
                        print("\nOrderError: Order of derivative calculation is smaller than 0.")
                    else:
                        x,y = symbols('x,y')
                        df = idiff(eval(circ), y, x, fnum)
                        print("\nDerivative of order",fnum,"is:\n")
                        pprint(df)
                        if str(sp.simplify(df, evaluate = False)) != str(df):
                            dsimp = input("\nSimplification of answer found. Simplify? (y/n) ")
                            if dsimp == "y":
                                print("\nSimplified:", df, "into:\n")
                                pprint(sp.simplify(df, evaluate = False))
                else:
                    print("\nCommandError: '", opt, "' is an invalid command")
            elif cmd == "p":
                f = input("\nEnter a function containing x and y or x and y and z:")
                if ("z" in f):
                    x,y,z = symbols('x,y,z')
                else:
                    x,y = symbols('x,y')
                if ("^" in f):
                    f = f.replace("^", "**")
                res = input("Enter variable to differentiate in respect to: ")
                fnum = input("Enter the order of partial derivative calculation: ")
                if fnum.isnumeric() == False:
                    print("\nTypeError: Order of derivative calculation is not a number.")
                elif int(fnum) < 0:
                    print("\nOrderError: Order of derivative calculation is smaller than 0.")
                else:
                    df = diff(f, res, fnum)
                    print("\nPartial derivative in respect to",res,"of order",fnum,"is:\n")
                    pprint(df)
                    if str(sp.simplify(df, evaluate = False)) != str(df):
                        dsimp = input("\nSimplification of answer found. Simplify? (y/n) ")
                        if dsimp == "y":
                            print("\nSimplified:", df, "into:\n")
                            pprint(sp.simplify(df, evaluate = False))
            elif cmd == "exit":
                print("\nExiting DerivaCalc ... ... ...")
                break
            else:
                print("\nCommandError: '", cmd, "' is an invalid command.")
        except:
            print("\nUnknownError: An unknown error occured.")


def integ():
    print("\n\n   ------------------------------------------------------------")
    print("\n  --+--  |\    |  ---+---  +----  +----      ^      |      +----")
    print("    |    | \   |     |     |      |         / \     |      |")
    print("    |    |  \  |     |     +---   |        / - \    |      |")
    print("    |    |   \ |     |     |      |       /     \   |      |")
    print("  --+--  |    \|     |     +----  +----  /       \  +----  +----")
    print("\n   ------------------------------------------------------------")
    print("\n                      The Integral Calculator\n")
    print("\nInteCalc supports:\n - Special numbers including Pi and e;")
    print(" - Basic Trigonometric Functions;\n", "- Exponents (for exponent with base e, input as 'exp(x)', NOT e**x);")
    print(" - The Natural Logarithm (input as log(x));")
    print(" - Inverse Trigonometric Functions (input as 'a' followed by a trigonometric function, e.g. asin(x) = arcsin(x));")
    print(" - Hyperbolic Functions and Inverse Hyperbolic Functions (same input format as inverse trigonometric functions);")
    print("(Full list of Python Math functions available on https://docs.python.org/3/library/math.html)\n")
    print("\nCommands:\n", "\n - Type 'a' in the main screen to calculate antiderivatives (indefinite integrals);")
    print(" - Type 'd' in the main screen to calculate definite integrals - with a graph!")
    print(" - Type 'i' in the main screen to calculate improper integrals;")
    print(" - Type 'help' in the main screen for a list of operations in Python;")
    print(" - Type 'exit' to quit InteCalc")
    print("\n(This version only supports single variable calculus)")
    print("(Absolute value function and factorial function is only supported by definite integral computation!)")
    while True:
        try:
            print("\n(Current Screen: InteCalc Main Screen)\n")
            cmd = input("Enter Command: ")
            if cmd == "help":
                print("\nBasic operations: ", "\n +: add \n", "-: minus \n", "*: multiply \n", "/: divide \n", "**: exponent")
                print(" %: return the remainder of a division \n", "//: return the rounded-down quotient of a division")
            elif cmd == "a":
                print("\n(Current Screen: Antiderivative Screen)\n")
                f = input("Enter a function: ")
                if ("pi" in f):
                    f = f.replace("pi", str(sp.core.numbers.pi))
                if ("^" in f):
                    f = f.replace("^", "**")
                else:
                    str(f)
                x = Symbol("x")
                F = Integral(f, x)
                if ("Integral" in str(F.doit())):
                    print("\nCannot compute integral.")
                else:
                    print("\nAntiderivative is:\n")
                    pprint(F.doit())
                    if str(sp.simplify(F.doit(), evaluate = False)) != str(F.doit()):
                        isimp = input("\nSimplification of answer found. Simplify? (y/n) ")
                        if isimp == "y":
                            print("\nSimplified:", F.doit(), "into:\n")
                            pprint(sp.simplify(F.doit(), evaluate = False))
            elif cmd == "d":
                print("\n(Current Screen: Definite Integral Screen)\n")
                def d_integrate():
                    def g(x):
                        final = eval(f)
                        return final
                    f = input("Enter the function you want to integrate: ")
                    if ("^" in f):
                        f = f.replace("^", "**")
                    lbound = input("\nEnter the lower bound: ")
                    if (lbound.isnumeric() == False) and ("pi" not in lbound) and ("e" not in lbound) and ("-" not in lbound) and ("." not in lbound) and ("sqrt" not in lbound) and ("oo" not in lbound):
                        return "\nTypeError: Lower bound is a not a number."
                    if ("pi" in lbound):
                        lbound = lbound.replace("pi", str(sp.core.numbers.pi))
                    if ("e" in lbound):
                        lbound = lbound.replace("e", str(E))
                    lbound = float(eval(lbound))
                    rbound = input("Enter the upper bound: ")
                    if (rbound.isnumeric() == False) and ("pi" not in rbound) and ("e" not in rbound) and ("-" not in rbound) and ("." not in rbound) and ("sqrt" not in rbound) and ("oo" not in rbound):
                        return "\nTypeError: Upper bound is a not a number."
                    if ("pi" in rbound):
                        rbound = rbound.replace("pi", str(sp.core.numbers.pi))
                    if ("e" in rbound):
                        rbound = rbound.replace("e", str(E))
                    rbound = float(eval(rbound))
                    x = sp.Symbol("x")
                    dinteg = integrate(f, (x, lbound, rbound)).evalf()
                    if (("1/x" in f or f == "x^-1") and (lbound <= 0 or lbound <= lbound + 1)) or (str(dinteg) == "nan") or ("I" in str(dinteg)):
                        return "\nMathError: Cannot compute integral because integral does not converge."
                    else:
                        print("\nCalculated integral of", f, "from", lbound, "to", rbound, ". Final area is:", dinteg)
                        print("\nShow graph of area? (y/n)")
                        show = input("(Exit the graph window when you are finished to continue) ")
                        if show == "y":
                            try:
                                print("\nLoading graph. Might take some time on first startup ...")
                                x = np.linspace((-rbound-8), (rbound + 8), 200000)
                                if ("ln" in f or "log" in f):
                                    x = np.linspace(int(floor(lbound)) + 1, int(ceil(rbound)) + 8, 200000)
                                y = [g(a) for a in x]
                                fig, ax = plt.subplots()
                                title = "Shaded area beneath function"
                                plt.title(title)
                                plt.xlabel("x", weight = "bold")
                                plt.ylabel("y", rotation = 0, weight = "bold")
                                plt.plot(x,y, color = "red")
                                # if (float(g(lbound)) != 0) and (float(g(rbound)) != 0):
                                    # plt.axis([lbound - 5, rbound + 5, float(g(round(lbound)))-(float(g(round(lbound)))+float(g(round(rbound))))/2-1, float(g(round(rbound)))+(float(g(round(lbound)))+float(g(round(rbound))))/2+1])
                                # elif (float(g(lbound)) == 0) or (float(g(rbound)) == 0):
                                    # plt.axis([lbound - 5, rbound + 5, -(rbound-lbound)/2, (rbound+lbound)/2])
                                plt.axis([-7.5, 7.5, -7.5, 7.5])
                                plt.grid()
                                ix = np.linspace(lbound, rbound)
                                iy = [g(i) for i in ix]
                                verts = [(lbound, 0)] + list(zip(ix, iy)) + [(rbound, 0)]
                                poly = Polygon(verts, facecolor = "blue")
                                ax.add_patch(poly)
                                plt.show()
                                return "\nExited graph."
                            except:
                                return "\nGraphError: Could not graph function."
                        else:
                            return "\nExiting Definite Integral Screen ..."
                print(d_integrate())
            elif cmd == "i":
                print("\n(Current Screen: Improper Integral Screen)\n")
                f = input("Enter a function: ")
                if ("pi" in f):
                    f = f.replace("pi", str(sp.core.numbers.pi))
                if ("^" in f):
                    f = f.replace("^", "**")
                else:
                    str(f)
                lbound = input("\nEnter the lower bound: ")
                if (lbound.isnumeric() == False) and ("pi" not in lbound) and ("e" not in lbound) and ("-" not in lbound) and ("." not in lbound) and ("sqrt" not in lbound) and ("oo" not in lbound):
                    return "\nTypeError: Lower bound is a not a number."
                if ("pi" in lbound):
                    lbound = lbound.replace("pi", str(sp.core.numbers.pi))
                if ("e" in lbound):
                    lbound = lbound.replace("e", str(E))
                if ("oo" in lbound):
                    lbound = eval(lbound)
                else:
                    lbound = float(eval(lbound))
                rbound = input("Enter the upper bound: ")
                if (rbound.isnumeric() == False) and ("pi" not in rbound) and ("e" not in rbound) and ("-" not in rbound) and ("." not in rbound) and ("sqrt" not in rbound) and ("oo" not in rbound):
                    return "\nTypeError: Upper bound is a not a number."
                if ("pi" in rbound):
                    rbound = rbound.replace("pi", str(sp.core.numbers.pi))
                if ("e" in rbound):
                    rbound = rbound.replace("e", str(E))
                if ("oo" in rbound):
                    rbound = eval(rbound)
                else:
                    rbound = float(eval(rbound))
                x = Symbol("x")
                try:
                    improper_area = Integral(f, (x, lbound, rbound)).principal_value()
                    print("\nCalculated improper integral of", f, "from", lbound, "to", rbound, ". Final area is:\n")
                    pprint(improper_area)
                    if str(sp.simplify(improper_area, evaluate = False)) != str(improper_area):
                        isimp = input("\nSimplification of answer found. Simplify? (y/n) ")
                        if isimp == "y":
                            print("\nSimplified:", improper_area, "into:\n")
                            pprint(sp.simplify(improper_area, evaluate = False))
                except ValueError:
                    print("\nValueError: singularity while computing improper integral.")
            elif cmd == "exit":
                print("\nExiting InteCalc ... ... ...")
                break
            else:
                print("\nCommandError: '", cmd, "' is an invalid command")
        except:
            print("\nUnknownError: An unknown error occured.")

def take_lim():
    print("\n\n   -----------------------------------------------------")
    print("\n  |      --+--  ^       ^  +----      ^      |      +----")
    print("  |        |    |\     /|  |         / \     |      |")
    print("  |        |    | \   / |  |        / - \    |      |")
    print("  |        |    |  \ /  |  |       /     \   |      |")
    print("  +----  --+--  |   v   |  +----  /       \  +----  +----")
    print("\n   -----------------------------------------------------")
    print("\n                   The Limit Calculator\n")
    print("\nLimCalc supports:\n - Special numbers including Pi and e;")
    print(" - Basic Trigonometric Functions;\n", "- Exponents (for exponent with base e, input as 'exp(x)', NOT e**x);")
    print(" - The Natural Logarithm (input as log(x));")
    print(" - Inverse Trigonometric Functions (input as 'a' followed by a trigonometric function, e.g. asin(x) = arcsin(x));")
    print(" - Hyperbolic Functions and Inverse Hyperbolic Functions (same input format as inverse trigonometric functions);")
    print("(Full list of Python Math functions available on https://docs.python.org/3/library/math.html)\n")
    print("\nCommands:\n", "\n - Type 'n' in the main screen to calculate normal limits;")
    print(" - Type 'o' in the main screen to calculate one-sided limits;")
    print(" - Type 'help' in the main screen for a list of operations in Python")
    print(" - Type 'exit' to quit LimCalc")
    while True:
        try:
            print("\n(Current Screen: LimCalc Main Screen)\n")
            cmd = input("Enter Command: ")
            if cmd == "help":
                print("\nBasic operations: ", "\n +: add \n", "-: minus \n", "*: multiply \n", "/: divide \n", "**: exponent")
                print(" %: return the remainder of a division \n", "//: return the rounded-down quotient of a division")
            elif cmd == "n":
                print("\n(Current screen: Limit Screen)\n")
                f = input("Enter a function: ")
                if ("pi" in f):
                    f = f.replace("pi", str(sp.core.numbers.pi))
                if ("^" in f):
                    f = f.replace("^", "**")
                else:
                    str(f)
                num = input("Enter the point of evaluation: ")
                if (num.isnumeric() == False) and ("pi" not in num) and ("e" not in num) and ("-" not in num) and ("." not in num) and ("oo" not in num) and ("sqrt" not in num):
                    print("\nTypeError: point of evaluation is a not a number.")
                if ("pi" in num):
                    num = num.replace("pi", str(sp.core.numbers.pi))
                if ("e" in num):
                    num = num.replace("e", str(E))
                num = float(eval(num))
                x = symbols("x")
                l = limit(f, x, num)
                if ("Limit" in str(l)):
                    print("\nCannot compute limit.")
                else:
                    print("\nLimit of",f,"as x approaches",num,"is:\n")
                    pprint(l)
                    if str(sp.simplify(l, evaluate = False)) != str(l):
                        lsimp = input("\nSimplification of answer found. Simplify? (y/n) ")
                        if lsimp == "y":
                            print("\nSimplified:", l, "into:\n")
                            pprint(sp.simplify(l, evaluate = False))
            elif cmd == "o":
                print("\n(Current screen: One-sided Limit Screen)\n")
                f = input("Enter a function: ")
                if ("pi" in f):
                    f = f.replace("pi", str(sp.core.numbers.pi))
                if ("^" in f):
                    f = f.replace("^", "**")
                else:
                    str(f)
                num = input("Enter the point of evaluation: ")
                if (num.isnumeric() == False) and ("pi" not in num) and ("e" not in num) and ("-" not in num) and ("." not in num) and ("oo" not in num) and ("sqrt" not in num):
                    print("\nTypeError: point of evaluation is a not a number.")
                else:
                    if ("pi" in num):
                        num = num.replace("pi", str(sp.core.numbers.pi))
                    if ("e" in num):
                        num = num.replace("e", str(E))
                    num = float(eval(num))
                    direction = input("Enter direction to compute the limit ('left' or 'right'): ")
                    if (direction == "left") or (direction == "right"):
                        if direction == "left":
                            direction_sign = "-"
                        elif direction == "right":
                            direction_sign = "+"
                        x = symbols("x")
                        l = limit(f, x, num, dir = direction_sign)
                        if ("Limit" in str(l)):
                            print("\nCannot compute limit.")
                        else:
                            print("\nLimit of",f,"as x approaches",num,"from the", direction, "is:\n")
                            pprint(l)
                            if str(sp.simplify(l, evaluate = False)) != str(l):
                                lsimp = input("\nSimplification of answer found. Simplify? (y/n) ")
                                if lsimp == "y":
                                    print("\nSimplified:", l, "into:\n")
                                    pprint(sp.simplify(l, evaluate = False))
                    else:
                        print("\nTypeError: Direction is not right or left.")
            elif cmd == "exit":
                print("\nExiting LimCalc ... ... ...")
                break
            else:
                print("\nCommandError: '", cmd, "' is an invalid command")
        except:
            print("\nUnknownError: An unknown error occured.")


main()
