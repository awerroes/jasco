def equations(abs1, abs2, abs3, solvent):
    
    """Contains absorption constans (coef) and formulas."""
    
    separator = "___________________________________________"
    coef = [[10.05, 0.97, 16.36, 2.43, 7.62, 15.39, 1.43, 35.87, 205],
           [9.93, 0.75, 16.23, 2.42, 7.51,15.48, 1.3, 33.12, 213],
           [10.36, 1.28, 17.49, 2.72, 7.64, 16.21, 1.38, 40.05, 211],
           [13.36, 5.19, 27.43, 8.12, 5.24, 22.24, 2.13, 97.64, 209],
           [11.24, 2.04, 20.13, 4.19, 7.05, 18.09, 1.90, 63.14, 214],
           [12.25, 2.79, 21.50, 5.10, 7.15, 18.71, 1.82, 85.02, 198],
           [16.72, 9.16, 34.09, 15.28, 1.44, 24.93, 1.63, 104.96, 221],
           [16.82, 9.28, 36.92, 16.54, 0.28, 27.64, 1.91, 95.15, 225]]
               
    chl_a = coef[solvent][0] * abs3 - coef[solvent][1] * abs2
    chl_b = coef[solvent][2] * abs2 - coef[solvent][3] * abs3
    chl_ab = coef[solvent][4] * abs3 + coef[solvent][5] * abs2
    car = (1000 * abs1 - coef[solvent][6] * 
       chl_a - coef[solvent][7] * chl_b)/coef[solvent][8]

    results = [chl_a, chl_b, chl_ab, car]
    return results

print("Choose a solvent!")
print("0 = diethyl eter (pure solvent); 470, 642.2, 660.6 [nm]\n"
      "1 = diethyl eter (water free); 470, 641.8, 660.0 [nm]\n"
      "2 = diethyl eter (water saturated); 470, 643.2, 661.6 [nm]\n"
      "3 = ethanol (95 % [v/v]); 470, 648.6, 664.2 [nm]\n"
      "4 = aceton (100 % pure solvent); 470, 644.8, 661.6 [nm]\n"
      "5 = aceton (80 % [v/v]; 470, 646.8, 663.2 [nm]\n"
      "6 = methanol (100 % pure solvent); 470, 652.4, 665.2 [nm]\n"
      "7 = methanol (90 % [v/v]; 470, 652.4, 665.2 [nm]\n")

solvent = int(input("What is your solvent (0-7)?\n"))
next_sample = 'y'

while (next_sample == 'y'):

    abs1 = float(input("Insert A(470):\t\t"))
    abs2 = float(input("Insert A(640-652):\t"))
    abs3 = float(input("Insert A(660+):\t\t"))

    pigments = ["chlorophyll a: ", "chlorophyll b: ",
                "chlorophyll a+b: ", "carotenoids: "]
    results = equations(abs1, abs2, abs3, solvent)
    for item in zip(pigments, results):
        print(item[0], item[1])

    next_sample = input("Do you want measure next sample? (y|n)")
