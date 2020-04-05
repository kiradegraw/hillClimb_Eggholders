# task1.1.py implements a hill climbing (descending) algorithm to find global minimum of Eggholder's function

from mpl_toolkits import mplot3d
import numpy as np
import random
import matplotlib.pyplot as plot
import time


def main():
    # declare variables
    startTime = time.time()
    xVals = []
    yVals = []
    functionVals = []

    # start loop of 100 iterations
    itr = 0
    while itr < 100:
        itr += 1
        print("-----Iteration ", itr, "-----")

        # create random initial solution
        arguments = [random.randrange(-10000, 10001), random.randrange(-10000, 10001)]
        print('initial:', arguments)

        initial = eggholder(arguments)
        best = initial
        print('eggholder: ', initial)

        # while solution is found within 100 consecutive steps
        steps = 0
        while steps < 100:
            # find new x' and y', along with new eggholder value
            newArg = newPos(arguments)
            nextVal = eggholder(newArg)

            # compare to determine lowest function value
            if nextVal < best:
                best = nextVal
                steps = 0

                # add lowest values to be plotted
                xVals.append(newArg[0])
                yVals.append(newArg[1])
                functionVals.append(best)
            else:
                steps += 1

        print('best:', best)

    endTime = time.time() - startTime  # total time
    print(endTime)

    # plot eggholder's minima distribution
    # 3D plotting info found from Python Data Science Handbook by Jake VanderPlas
    fig = plot.figure()
    ax = plot.axes(projection='3d')
    ax.scatter(xVals, yVals, functionVals, c=functionVals, cmap='viridis', linewidth=0.5)
    ax.set_title('Minima Distribution')
    ax.set_xlabel('X Value')
    ax.set_ylabel('Y Value')
    ax.set_zlabel("Eggholder's")
    plot.show()


# generate new x' and y' based on assignment requirements
def newPos(arg):
    newX = (random.random() - 0.5)*1.0 + arg[0]
    newY = (random.random() - 0.5)*1.0 + arg[1]
    return newX, newY

# determines eggholder's value for given x and y (param x[0] = x, x[1] = y)
def eggholder(x):
    return (-(x[1] + 47) * np.sin(np.sqrt(abs(x[0]/2 + (x[1] + 47))))
            -x[0] * np.sin(np.sqrt(abs(x[0] - (x[1] + 47)))))


if __name__ == "__main__":
    main()
