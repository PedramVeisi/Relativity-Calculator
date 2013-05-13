# -*- coding: utf-8 -*-

"""
Relativity Calculator Version 1.0

A simple python script to calculate Lorentz Factor from relative speed is given and relative speed from Lorentz Factor.
More information: http://en.wikipedia.org/wiki/Lorentz_factor

Special thanks to Prof. Larry Randles Lagerstrom and Coursera for this great course: https://www.coursera.org/course/einstein

I'm new to relativity. So, there me new features added to this script.

Copyright 2013 (©) Pedram Veisi <pedramveisi@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""


import math

class RelativityCalculator( ):

    #Speed of lingt (m / s)
    c = 3 * (10 ** 8)

    def speed_to_gamma(self, v):
        '''(float) > float

        Claculate Lorentz Factor. v is relative speed.

        Precondition: v <= c (speed of light)

        >>>speed_to_gamma(0)
        1.0
        >>>speed_to_gamma(3000000)
        1.0000500037503126
        >>>speed_to_gamma(297000000)
        7.088812050083354
        >>>speed_to_gamma(300000000)
        -1
        '''

        if not (v < 300000000):
            gamma = -1
        else:
            gamma = 1 / (math.sqrt(1 - ((v / self.c) ** 2)))

        return gamma

    def gamma_to_speed(self, gamma):
        '''(float) -> float

        Calculate relative speed. gamma is Lorentz factor.

        Precondition: gamma >= 1

        >>>gamma_to_speed(0)
        0.0
        >>>gamma_to_speed(1.5)
        223606797.74997896
        >>>gamma_to_speed(10)
        298496231.13198596
        '''

        if (gamma < 1):
            v = -1
        else:
            v = (self.c * (math.sqrt(1 - (1 / gamma ** 2))))

        return v


class Main():

    #Speed of lingt (m / s)
    c = 3 * (10 ** 8)

    def __init__(self):

        self.rc = RelativityCalculator()
        print("\nWelcome to Relativity Calculater 1.0\n")

        while(True):
            print("1. Compute Lorentz Factor from relative speed")
            print("2. Compute relative speed from Lorentz Factor")
            print("3. Exit")
            print("")
            user_input = input("Enter Command Number: ")

            try:
                command_number = int(user_input)

                if (command_number == 1):
                    print("You have to options for providing relative speed: km/s or relative to c (For example: 0.5c)")
                    speed_input = input("Enter relative speed: ")
                    gamma = self.speed_to_gamma_handler(speed_input)

                    if (gamma == -1):
                        print("\nInvalid speed. Relative speed must be a number and cannot be greater than c (300000 km/s).\n")
                    else:
                        print("\nLorentz Factor is: {0}\n".format(gamma))

                elif (command_number == 2):
                    gamma_input = input("Enter Lorentz Factor (>= 1): ")
                    speed = self.gamma_to_speed_handler(gamma_input)

                    if (speed == -1):
                        print("\nInvalid Lorentz Factor.It must be greater than or equal to 1.\n")
                    else:
                        print("\nRelative Speed is: {0:.4f} m/s = {1:.4f} km/s = {2:.10f}c\n".format(speed, speed / 1000, speed / self.c))
                elif (command_number == 3):
                    print("Bye!")
                    break
                else:
                    print("\nInvalid command! Enter command Number (1, 2, ...).")
            except ValueError:
                print("Enter a number. For example if you want to exit enter 3.")

    def speed_to_gamma_handler(self, user_speed):
        '''(float) -> float

        Check speed and call speed_to_gamma form Relativity Calculator if it's valid.

        '''
        try:
            if (user_speed[-1] == 'c'):
                speed = float(user_speed[:-1]) * self.c
            else:
                #convert user input from km/s to m/s
                speed = float(user_speed) * 1000

            gamma = self.rc.speed_to_gamma(speed)
            return gamma

        except ValueError:
            return -1


    def gamma_to_speed_handler(self, user_gamma):
        '''(float) -> float

        Check gamma and call gamma_to_speed form Relativity Calculator if it's valid.

        '''
        try:
            gamma = float(user_gamma)
            speed = self.rc.gamma_to_speed(gamma)
            return speed
        except ValueError:
            return -1

if __name__ == "__main__":
    Main()
