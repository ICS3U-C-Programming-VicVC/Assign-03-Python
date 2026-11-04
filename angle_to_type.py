#!/usr/bin/env python3
# Created By: Victor Victor-Calixte
# Date: 11/02/26
# This program will determine the type of triangle based on 2 given angles.

import constants


def main():
    print(constants.WELCOMING_MSG)

    angle_a_str = input("Enter an angle of the triangle: ")
    angle_b_str = input("Enter another angle of the triangle: ")

    try:
        angle_a = int(float(angle_a_str))
        angle_b = int(float(angle_b_str))

        remaining = constants.ANGLE_180 - (angle_b + angle_a)
        added_angles = angle_a + angle_b

        possible = False
        is_right = False

        if added_angles >= constants.ANGLE_180:
            print(constants.IMPOSSIBLE_MSG.format(angle_a_str, angle_b_str))

        if angle_a >= constants.ANGLE_180 or angle_b >= constants.ANGLE_180:
            print(constants.IMPOSSIBLE_MSG.format(angle_a_str, angle_b_str))

        if angle_a <= 0 or angle_b <= 0:
            print(constants.IMPOSSIBLE_MSG.format(angle_a_str, angle_b_str))
        else:
            possible = True

        if possible:

            if angle_a == constants.ANGLE_90 or angle_b == constants.ANGLE_90:
                print(constants.RIGHT_TRIANGLE)
                is_right = True

            if not is_right:

                if angle_a != angle_b:
                    print(constants.SCALENE_TRAINGLE)

                if angle_a == angle_b and angle_a == remaining:
                    print(constants.EQUILATERAL_TRIANGLE)

                if angle_a == angle_b and angle_a != remaining:
                    print(constants.ISOSCELES_TRIANGLE)

    except ValueError:
        print(constants.ERR_MSG.format(angle_a_str, angle_b_str))


if __name__ == "__main__":
    main()
