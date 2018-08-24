# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

LANDCOVER_VALUE_TO_TYPE = {
    0: 'water',
    1: 'evergreen needleleaf forest',
    2: 'evergreen broadleaf forest',
    3: 'deciduous needleleaf forest',
    4: 'deciduous broadleaf forest',
    5: 'mixed forest',
    6: 'closed shrublands',
    7: 'open shrublands',
    8: 'woody savannas',
    9: 'savannas',
    10: 'grasslands',
    11: 'permanent wetlands',
    12: 'croplands',
    13: 'urban and built-up',
    14: 'cropland/natural vegetation mosaic',
    15: 'snow and ice',
    16: 'barren or sparsely vegetated',
    244: 'unclassified',
    255: 'fill Value',
}

# LANDCOVER is a numpy array of (x, y, landcover value)
LANDCOVER = np.array([
    [2, 0, 0],
    [3, 0, 0],
    [4, 0, 0],
    [5, 0, 0],
    [4, 1, 0],
    [4, 5, 0],
    [5, 5, 0],
    [0, 0, 4],
    [0, 1, 4],
    [5, 1, 4],
    [3, 2, 4],
    [4, 2, 4],
    [5, 2, 4],
    [3, 3, 4],
    [2, 4, 6],
    [3, 5, 6],
    [3, 4, 7],
    [2, 5, 7],
    [0, 2, 8],
    [2, 3, 8],
    [0, 4, 8],
    [0, 3, 9],
    [1, 3, 9],
    [1, 4, 9],
    [0, 5, 9],
    [1, 5, 9],
    [1, 0, 10],
    [1, 2, 10],
    [4, 3, 10],
    [4, 4, 10],
    [5, 4, 10],
    [3, 1, 11],
    [1, 1, 12],
    [2, 2, 12],
    [2, 1, 13],
    [5, 3, 13]
])

# CARBON is a numpy array of (x, y, carbon content)
CARBON = np.array([
    [0, 0, 207],
    [1, 0, 26],
    [2, 0, 0],
    [3, 0, 0],
    [4, 0, 0],
    [0, 1, 135],
    [1, 1, 96],
    [2, 1, 156],
    [3, 1, 47],
    [4, 1, 0],
    [0, 2, 196],
    [1, 2, 70],
    [2, 2, 106],
    [3, 2, 126],
    [4, 2, 48],
    [0, 3, 254],
    [1, 3, 225],
    [2, 3, 54],
    [3, 3, 125],
    [4, 3, 230],
    [0, 4, 140],
    [1, 4, 175],
    [2, 4, 48],
    [3, 4, 215],
    [4, 4, 46]
])


####################### The function ##############################


def carbon_cont(land, stdv):
    DFland = pd.DataFrame(LANDCOVER, columns=['X', 'Y', 'Land_Type'])
    DFcarb = pd.DataFrame(CARBON, columns=['X', 'Y', 'Carbon_Content'])

    DFland['Land_Type'].replace(LANDCOVER_VALUE_TO_TYPE, inplace=True)
    LanCar = pd.merge(DFcarb, DFland, on=['X', 'Y'])
    MLanCar = LanCar.groupby('Land_Type')['Carbon_Content'].mean()

    Jrd = LanCar.groupby('Land_Type').Carbon_Content.agg(['mean', 'std'])

    MLanCar.to_csv('h.csv')
    dt = pd.read_csv('h.csv')
    Jrd.to_csv('r.csv')
    rr = pd.read_csv('r.csv')

    if mn == 'a':
        print('\n')
        print(tabulate(dt, headers=["Land Type", "Carbon Content"], tablefmt='rst', floatfmt='.2f'))
        print('\n')
        plt.plot(MLanCar)
        plt.ylabel('Carbon')
        plt.xlabel('Land Type')
        plt.xticks([])
        plt.title('Soil Carbon Classification')
        plt.show()

    if mn == 'c':
        print('\n')
        print(tabulate(rr, headers=["Land Type", "Carbon Cont AVG", "Carbon Cont STD"], tablefmt='rst', floatfmt='.2f'))
        print('\n')
        plt.plot(Jrd)
        plt.ylabel('Carbon')
        plt.xlabel('Land Type')
        plt.xticks([])
        plt.title('Soil Carbon Classification')
        plt.show()

    if mn == 'b':
        try:
            if land not in LanCar.Land_Type.values:
                print("\nError: This land cover has no index!!!")

            if stdv == 'y':
                rg = Jrd.loc[land]
                print("\nThe values for " + land + " are:\n" + rg.to_string())

            if stdv == 'n':
                ave = MLanCar.loc[land]
                print("\nThe average for " + land + " is: " + str(ave))

            if stdv != 'y' and stdv != 'n':
                print("\nYou most enter Y or N")

        except Exception as err:
            print("Error {}".format(err))


print("\nCarbon Stocks in the Soil according to Land Cover\n")
print('''
    A to use default values
    B to enter the land cover and the standard deviation "Y or N"
    C to see standard deviation and average with the default values
''')

mn = input("Select by entering the letter of your preference:  ").lower()

if mn == 'a':
    carbon_cont('a', 'a')
elif mn == 'b':
    la = input("Enter the land cover: ").lower()
    sa = input("Enter Y if you want the standard deviation or N if not: ").lower()
    carbon_cont(la, sa)
elif mn == 'c':
    carbon_cont('a', 'a')