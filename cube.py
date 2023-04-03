# Credit to https://www.youtube.com/watch?v=p09i_hoFdd0&list=LL&index=4
# Mostly converted to python

import math, time, sys, os
import numpy as np

A, B, C = 0.0, 0.0, 0.0
x, y, z = 0.0, 0.0, 0.0
ooz = 0.0
x, y = 0.0, 0.0

# Parameters.
# Amount of points per half a side, so the more, the more calculated points per surface
cubeWidth = 10
# hight and width of printed image
width = 170
height = 50
# distance from cam
distanceFromCam = 30
incrementSpeed = 0.6
# amount of zoom
K1 = 30


# rotation around x axis
def calculateX(i, j, k):
    return (j * math.sin(A) * math.sin(B) * math.cos(C) 
            - k * math.cos(A) * math.sin(B) * math.cos(C)
            + j * math.cos(A) * math.sin(C)
            + k * math.sin(A) * math.sin(C)
            + i * math.cos(B) * math.cos(C))

# Rotation around y axis
def calculateY(i, j, k):
    return (j * math.cos(A) * math.cos(C)
            + k * math.sin(A) * math.cos(C)
            - j * math.sin(A) * math.sin(B) * math.sin(C)
            + k * math.cos(A) * math.sin(B) * math.sin(C)
            - i * math.cos(B) * math.sin(C))

# rotation around z axis
def calculateZ(i, j, k):
    return (k * math.cos(A) * math.cos(B)
            - j * math.sin(A) * math.cos(B)
            + i * math.sin(B))

# Calculate an entire surface of a cube using X, Y, and Z direction, 
#   and a char to represent the surface in printing
def calculateForSurface(cubeX, cubeY, cubeZ, char):
    x = calculateX(cubeX, cubeY, cubeZ)
    y = calculateY(cubeX, cubeY, cubeZ)
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam

    # 
    ooz = 1/z

    # 
    xp = int(width/2 + K1 * ooz * x * 2)
    yp = int(height/2 + K1 * ooz * y)

    # idx in buffer of screen
    idx = xp + yp * width
    if (idx >= 0 and idx < width * height):
        if (ooz > zbuffer[idx]):
            zbuffer[idx] = ooz
            buffer[idx] = char


def main():
    print(chr(27) + "[2J")

    global A, B, C
    global buffer
    global zbuffer

    try: 
        while (1):
        # buffer = ' ' * (width * height)
            buffer = list((' ' * width * height))
            zbuffer =  np.zeros(width * height * 4)

            cubeX = -cubeWidth
            while (cubeX < cubeWidth):
                cubeY = -cubeWidth
                while (cubeY < cubeWidth):
                    # all surfaces
                    calculateForSurface(cubeX, cubeY, -cubeWidth, '#')
                    calculateForSurface(cubeWidth, cubeY, cubeX, '.')
                    calculateForSurface(-cubeWidth, cubeY, -cubeX, 'x')
                    calculateForSurface(-cubeX, cubeY, cubeWidth, 'Y')
                    calculateForSurface(cubeX, -cubeWidth, -cubeY, '*')
                    calculateForSurface(cubeX, cubeWidth, cubeY, '^')

                    cubeY += incrementSpeed
                cubeX += incrementSpeed

            # print on screen
            # os.system('clear')
            print(chr(27) + "[H")

            bufferString = ''.join(buffer)

            for i in range(0, height):
                print(bufferString[i*width:(i+1)*width])

            A += 0.05
            B += 0.05
            time.sleep(0.001)

    except KeyboardInterrupt:
        sys.exit()

    return 0

if __name__ == "__main__":
    main()