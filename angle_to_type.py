#!/usr/bin/env python3
# Created By: Victor Victor-Calixte
# Date: 11/02/26
# This program will determine the type of triangle based on 2 given angles.

import constants


def main():
    print(constants.WELCOMING_MSG)

    # Getting 2 angles of triangle from the user
    angle_a_str = input("Enter an angle of the triangle: ")
    angle_b_str = input("Enter another angle of the triangle: ")

    # the try statement will make sure the code safely with invalid user inputs
    try:
        # converting the given angles
        angle_a = float(angle_a_str)
        angle_b = float(angle_b_str)

        # calculating the remaining angle
        angle_c = constants.ANGLE_180 - (angle_b + angle_a)
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

        # getting the triangle type
        if possible:

            if angle_a == constants.ANGLE_90 or angle_b == constants.ANGLE_90:
                print(constants.RIGHT_TRIANGLE)
                is_right = True

            if not is_right:

                if angle_a != angle_b:
                    print(constants.SCALENE_TRAINGLE)

                if angle_a == angle_b and angle_a == angle_c:
                    print(constants.EQUILATERAL_TRIANGLE)

                if angle_a == angle_b and angle_a != angle_c:
                    print(constants.ISOSCELES_TRIANGLE)

            # displaying the results back to the user
            print(constants.REMAININNG_ANGLE.format(angle_c))

    except ValueError:
        print(constants.ERR_MSG.format(angle_a_str, angle_b_str))


if __name__ == "__main__":
    main()
