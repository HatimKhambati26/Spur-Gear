import math


def calculate(P, N1, i, sf, pinion, FoS1, BHN1, gear, FoS2, BHN2, m, psi, u, gear_qua, pres_ang, E1, E2):
    global Pd, z1, z2, Y2, Y1, e, Cv, Ft, Vm, benstr2, benstr1, b, Fd, Fs, BHN, weak1, weak2, m1, Fw, round2, N12, N22
    benstr1 = -9999999999
    benstr2 = -9999999999
    Pd = -9999999999
    z1 = -9999999999
    z2 = -9999999999
    Y2 = -9999999999
    Y1 = -9999999999
    Vm = -9999999999
    Ft = -9999999999
    benstr2 = -9999999999
    benstr1 = -9999999999
    b = -9999999999
    Fd = -9999999999
    Fs = -9999999999
    BHN = -9999999999
    weak2 = -9999999999
    weak1 = -9999999999
    m1 = -9999999999
    Fw = -9999999999
    round2 = -9999999999
    N12 = -9999999999
    N22 = -9999999999
    # = -9999999999
    # = -9999999999
    # = -9999999999
    if i <= 5:
        while i != 0:
            print("Single stage gearbox")
            N2 = N1 / i
            print("N2=", round(N2, 2))

            # sf = float(input("Enter value of service factor(Sf): "))
            Pd = P * sf
            print("Design Power (Pd) is: ", Pd)
            # pres_ang = int(input("Select pressure angle in degrees "))
            # gear_qua = int(input(
            #     "Select gear quality \n 1. Precision gears, \n 2. Commercially cut gears< \n 3. First class "
            #     "commercial gears \n"))
            z1 = 18
            print("i=", i)
            z2 = int((z1 * i) + 1)
            print("\n z1=", z1, " \n z2= ", z2)
            # LEWIS FORM FACTOR
            Y1 = round((0.154 - (0.912 / z1)) * math.pi, 3)
            print("Lewis form factor of pinion Y1= ", round(Y1, 3))
            Y2 = round((0.154 - (0.912 / z2)) * math.pi, 3)
            print("Lewis form factor of gear Y2= ", round(Y2, 3))
            # MATERIAL SELECTION
            # PINION MATERIAL
            # pinion = int(input(
            #     "Select the material for pinion \n1. C50 \n2. C55 Mn75\n3. 40Cr1\n4. 35Ni1Cr60 \n5. C45 \n6. "
            #     "15Ni2Cr1Mo25 \n7. 40Ni2Cr1Mo28\n"))
            if pinion == 1:
                # # FoS = int(input("Enter the values of factor of safety: "))
                benstr1 = 380 / FoS1
                print("Bending stress= ", round(benstr1, 2))
                # BHN1 = int(input("Enter Brinell Hardness Number= "))
            if pinion == 2:
                # # FoS = int(input("Enter the values of factor of safety: "))
                benstr1 = 400 / FoS1
                print("Bending stress= ", round(benstr1, 2))
                # BHN1 = int(input("Enter Brinell Hardness Number= "))
            if pinion == 3:
                # # FoS = int(input("Enter the values of factor of safety: "))
                benstr1 = 875 / FoS1
                print("Bending stress= ", round(benstr1, 2))
                # BHN1 = int(input("Enter Brinell Hardness Number= "))
            if pinion == 4:
                # # FoS = int(input("Enter the values of factor of safety: "))
                benstr1 = round(875 / FoS1, 2)
                print("Bending stress= ", round(benstr1, 2))
                # BHN1 = int(input("Enter Brinell Hardness Number= "))
            if pinion == 5:
                benstr1 = 135
                print("Bending stress= ", round(benstr1, 2))
                # BHN1 = int(input("Enter Brinell Hardness Number= "))
            if pinion == 6:
                benstr1 = 300
                print("Bending stress= ", round(benstr1, 2))
                # BHN1 = int(input("Enter Brinell Hardness Number= "))
            if pinion == 7:
                benstr1 = 380
                print("Bending stress= ", round(benstr1, 2))
                # BHN1 = int(input("Enter Brinell Hardness Number= "))
            # GEAR MATERIAL
            # gear = int(input(
            #     "Select the material for gear \n1. C50 \n2. C55 Mn75\n3. 40Cr1\n4. 35Ni1Cr60 \n5. C45 \n6. "
            #     "15Ni2Cr1Mo25 \n7. 40Ni2Cr1Mo28\n"))
            if gear == 1:
                # # FoS = int(input("Enter the values of factor of safety: "))
                benstr2 = 380 / FoS2
                print("Bending stress= ", round(benstr2, 2))
                # BHN2 = int(input("Enter Brinell Hardness Number= "))
            if gear == 2:
                # # FoS = int(input("Enter the values of factor of safety: "))
                benstr2 = 400 / FoS2
                print("Bending stress= ", round(benstr2, 2))
                # BHN2 = int(input("Enter Brinell Hardness Number= "))
            if gear == 3:
                # # FoS = int(input("Enter the values of factor of safety: "))
                benstr2 = 875 / FoS2
                print("Bending stress= ", round(benstr2, 2))
                # BHN2 = int(input("Enter Brinell Hardness Number= "))
            if gear == 4:
                # # FoS = int(input("Enter the values of factor of safety: "))
                benstr2 = 875 / FoS2
                print("Bending stress= ", round(benstr2, 2))
                # BHN2 = int(input("Enter Brinell Hardness Number= "))
            if gear == 5:
                benstr2 = 135
                print("Bending stress= ", round(benstr2, 2))
                # BHN2 = int(input("Enter Brinell Hardness Number= "))
            if gear == 6:
                benstr2 = 300
                print("Bending stress= ", round(benstr2, 2))
                # BHN2 = int(input("Enter Brinell Hardness Number= "))
            if gear == 7:
                benstr2 = 380
                print("Bending stress= ", round(benstr2, 2))
                # BHN2 = int(input("Enter Brinell Hardness Number= "))
            BHN = BHN1 - BHN2
            while BHN < 30:
                BHN = BHN1 - BHN2
                print("BHN1-BHN2= ", BHN, "<30")
                # BHN1 = int(input("Enter the value of BHN1:- "))
                # BHN2 = int(input("Enter the value of BHN2:- "))
                BHN = BHN1 - BHN2
                print("BHN1-BHN2= ", BHN, ">=30")
                break
            # SELECTION OF WEAKER ELEMENT
            weak1 = round(benstr1 * Y1, 2)
            weak2 = round(benstr2 * Y2, 2)
            if weak1 < weak2:
                print("Since", "Strength of pinion = ", round(weak1, 2), "<", "Strength of gear = ",
                      round(weak2, 2),
                      "\nPinion is weaker")
            else:
                print("Since", "Strength of gear = ", round(weak2, 2), "<", "Strength of pinion = ",
                      round(weak1, 2),
                      "\nGear is weaker")
            # MODULE
            if weak1 < weak2:
                Mt1 = (9.55 * 1000000 * Pd) / N1
                m1 = round(1.26 * pow(Mt1 / (Y1 * benstr1 * 10 * z1), 0.33), 2)
                print("Module= ", round(m1, 2))
                # m = int(input("Enter module to be selected: "))
                # psi = int(input("Enter the values of psi: "))
                b = psi * m
                print("b=", b)
                # TOOTH STRENGTH
                Fs = round(benstr1 * b * m * Y1, 2)
                print("Fs= ", round(Fs, 2))
                # DYNAMIC LOAD
                # u = int(input(
                #     "Enter the method to calculate dynamic load\n1. Barth velocity method\n2. Buckingham method"))
                if u == 1:
                    d1 = m * z1
                    Ft = (2 * Mt1) / d1
                    Vm = (math.pi * d1 * N1) / 60000
                    if gear_qua == 1:
                        Cv = (5.5 + math.sqrt(Vm)) / 5.5
                    if gear_qua == 2:
                        Cv = (3 + math.sqrt(Vm)) / 3
                    if gear_qua == 3:
                        Cv = (6 + math.sqrt(Vm)) / 6
                    Fd = round(Ft * Cv, 2)
                    print("Dynamic load= ", round(Fd, 2))
                if u == 2:
                    d1 = m * z1
                    Ft = (2 * Mt1) / d1
                    Vm = (math.pi * d1 * N1) / 60000
                    # PRECISION GEARS
                    if m <= 4 and gear_qua == 1:
                        e = 0.0125
                    if m == 5 and gear_qua == 1:
                        e = 0.0125
                    if m == 6 and gear_qua == 1:
                        e = 0.015
                    if m == 7 and gear_qua == 1:
                        e = 0.017
                    if m == 8 and gear_qua == 1:
                        e = 0.019
                    if m == 9 and gear_qua == 1:
                        e = 0.0205
                    if m == 10 and gear_qua == 1:
                        e = 0.022
                    # COMMERCIAL GEARS
                    if m <= 4 and gear_qua == 2:
                        e = 0.05
                    if m == 5 and gear_qua == 2:
                        e = 0.056
                    if m == 6 and gear_qua == 2:
                        e = 0.064
                    if m == 7 and gear_qua == 2:
                        e = 0.072
                    if m == 8 and gear_qua == 2:
                        e = 0.08
                    if m == 9 and gear_qua == 2:
                        e = 0.085
                    if m == 10 and gear_qua == 2:
                        e = 0.09
                    # CAREFULLY CUT GEARS
                    if m <= 4 and gear_qua == 3:
                        e = 0.025
                    if m == 5 and gear_qua == 3:
                        e = 0.025
                    if m == 6 and gear_qua == 3:
                        e = 0.03
                    if m == 7 and gear_qua == 3:
                        e = 0.035
                    if m == 8 and gear_qua == 3:
                        e = 0.038
                    if m == 9 and gear_qua == 3:
                        e = 0.041
                    if m == 10 and gear_qua == 3:
                        e = 0.044
                    c = 11860 * e
                    Fd = Ft * ((0.164 * Vm * (c * b + Ft)) / (0.164 * Vm + 1.485 * math.sqrt(c * b + Ft)))
                    print("Dynamic load= ", round(Fd, 2))
                if Fs > Fd:
                    print("Design is safe")
                else:
                    print("Design Not Safe!!!")
                #                 while Fs < Fd:
                #                     print("\nFs= ", round(Fs, 2), " < Fd= ", round(Fd, 2), "\nDesign is not safe")
                #                     Mt1 = (9.55 * 1000000 * Pd) / N1
                #                     m = int(input("Enter module to be selected: "))
                #                     psi = int(input("Enter the values of psi"))
                #                     b = psi * m
                #                     print("b=", b)
                #                     # TOOTH STRENGTH
                #                     Fs = benstr1 * b * m * Y1
                #                     print("Fs= ", round(Fs, 2))
                #                     # DYNAMIC LOAD
                #                     u = int(input(
#                         "Enter the method to calculate dynamic load\n1. Barth velocity method\n2. Buckingham method"
                #                     ))
                #                     if u == 1:
                #                         d1 = m * z1
                #                         Ft = (2 * Mt1) / d1
                #                         Vm = (math.pi * d1 * N1) / 60000
                #                         if gear_qua == 1:
                #                             Cv = (5.5 + math.sqrt(Vm)) / 5.5
                #                         if gear_qua == 2:
                #                             Cv = (3 + math.sqrt(Vm)) / 3
                #                         if gear_qua == 3:
                #                             Cv = (6 + math.sqrt(Vm)) / 6
                #                         Fd = Ft * Cv
                #                         print("Dynamic load= ", round(Fd, 2))
                #                     if u == 2:
                #                         d1 = m * z1
                #                         Ft = (2 * Mt1) / d1
                #                         Vm = (math.pi * d1 * N1) / 60000
                #                         # PRECISION GEARS
                #                         if m <= 4 and gear_qua == 1:
                #                             e = 0.0125
                #                         if m == 5 and gear_qua == 1:
                #                             e = 0.0125
                #                         if m == 6 and gear_qua == 1:
                #                             e = 0.015
                #                         if m == 7 and gear_qua == 1:
                #                             e = 0.017
                #                         if m == 8 and gear_qua == 1:
                #                             e = 0.019
                #                         if m == 9 and gear_qua == 1:
                #                             e = 0.0205
                #                         if m == 10 and gear_qua == 1:
                #                             e = 0.022
                #                         # COMMERCIAL GEARS
                #                         if m <= 4 and gear_qua == 2:
                #                             e = 0.05
                #                         if m == 5 and gear_qua == 2:
                #                             e = 0.056
                #                         if m == 6 and gear_qua == 2:
                #                             e = 0.064
                #                         if m == 7 and gear_qua == 2:
                #                             e = 0.072
                #                         if m == 8 and gear_qua == 2:
                #                             e = 0.08
                #                         if m == 9 and gear_qua == 2:
                #                             e = 0.085
                #                         if m == 10 and gear_qua == 2:
                #                             e = 0.09
                #                         # CAREFULLY CUT GEARS
                #                         if m <= 4 and gear_qua == 3:
                #                             e = 0.025
                #                         if m == 5 and gear_qua == 3:
                #                             e = 0.025
                #                         if m == 6 and gear_qua == 3:
                #                             e = 0.03
                #                         if m == 7 and gear_qua == 3:
                #                             e = 0.035
                #                         if m == 8 and gear_qua == 3:
                #                             e = 0.038
                #                         if m == 9 and gear_qua == 3:
                #                             e = 0.041
                #                         if m == 10 and gear_qua == 3:
                #                             e = 0.044
                #                         c = 11860 * e
                #                         Fd = Ft + ((0.164 * Vm * ((c * b) + Ft)) / (
                #                                     0.164 * Vm + 1.485 * math.sqrt((c * b) + Ft)))
                #                         print("Dynamic load= ", round(Fd, 2))
                #                         break
                #             print("\nFs= ", round(Fs, 2), " > Fd=", round(Fd, 2))
                #             print("\nDesign is safe")
                #             # CHECK FOR WEAR
                d1 = m * z1
                Q = (2 * i) / (i + 1)
                # E1 = float(input("Enter the value of E1: "))
                # E2 = float(input("Enter the value of E2: "))
                BHNavg = (BHN1 + BHN2) / 2
                comstr = (2.8 * BHNavg) - 70
                k = (comstr * comstr * math.sin(pres_ang) * ((1 / E1) + (1 / E2))) / 1.4
                Fw = round(d1 * Q * k * b, 2)
                if Fw > Fd:
                    print("\n Fw=", round(Fw, 2), "> Fd=", round(Fd, 2), "\nDesign is safe")
                else:
                    # while Fw < Fd:
                    #     print("\n Fw=", round(Fw, 2), "< Fd=", round(Fd, 2), "\nDesign is not safe")
                    #     m = input("Enter module to be selected: ")
                    #     d1 = m * z1
                    #     Q = (2 * i) / (i + 1)
                    #     E1 = float(input("Enter the value of E1: "))
                    #     E2 = float(input("Enter the value of E2: "))
                    #     BHNavg = (BHN1 + BHN2) / 2
                    #     comstr = (2.8 * BHNavg) - 70
                    #     k = (comstr * comstr * math.sin(pres_ang) * ((1 / E1) + (1 / E2))) / 1.4
                    #     Fw = d1 * Q * k * b
                    #     break
                    # print("\n Fw=", round(Fw, 2), "> Fd=", round(Fd, 2), "\nDesign is safe")
                    print("\n Fw=", round(Fw, 2), "< Fd=", round(Fd, 2), "\nDesign is NOT safe")
                break
    #         # WHEN GEAR IS WEAKER
    #         if weak2 < weak1:
    #             Mt1 = (9.55 * 1000000 * Pd) / N2
    #             m1 = 1.26 * pow(Mt1 / (Y2 * benstr2 * 10 * z2), 0.33)
    #             print("Module= ", round(m1, 2))
    #             m = int(input("Enter module to be selected: "))
    #             psi = int(input("Enter the values of psi: "))
    #             b = psi * m
    #             print("b=", b)
    #             # TOOTH STRENGTH
    #             Fs = benstr2 * b * m * Y2
    #             print("Fs= ", round(Fs, 2))
    #             # DYNAMIC LOAD
    #             u = int(input(
    #                 "Enter the method to calculate dynamic load\n1. Barth velocity method\n2. Buckingham method"))
    #             if u == 1:
    #                 d2 = m * z2
    #                 Ft = (2 * Mt1) / d2
    #                 Vm = (math.pi * d2 * N2) / 60000
    #                 if gear_qua == 1:
    #                     Cv = (5.5 + math.sqrt(Vm)) / 5.5
    #                 if gear_qua == 2:
    #                     Cv = (3 + math.sqrt(Vm)) / 3
    #                 if gear_qua == 3:
    #                     Cv = (6 + math.sqrt(Vm)) / 6
    #                 Fd = Ft * Cv
    #                 print("Dynamic load= ", round(Fd, 2))
    #                 if u == 2:
    #                     d2 = m * z2
    #                     Ft = (2 * Mt1) / d2
    #                     Vm = (math.pi * d2 * N2) / 60000
    #                     # PRECISION GEARS
    #                     if m <= 4 and gear_qua == 1:
    #                         e = 0.0125
    #                     if m == 5 and gear_qua == 1:
    #                         e = 0.0125
    #                     if m == 6 and gear_qua == 1:
    #                         e = 0.015
    #                     if m == 7 and gear_qua == 1:
    #                         e = 0.017
    #                     if m == 8 and gear_qua == 1:
    #                         e = 0.019
    #                     if m == 9 and gear_qua == 1:
    #                         e = 0.0205
    #                     if m == 10 and gear_qua == 1:
    #                         e = 0.022
    #                     # COMMERCIAL GEARS
    #                     if m <= 4 and gear_qua == 2:
    #                         e = 0.05
    #                     if m == 5 and gear_qua == 2:
    #                         e = 0.056
    #                     if m == 6 and gear_qua == 2:
    #                         e = 0.064
    #                     if m == 7 and gear_qua == 2:
    #                         e = 0.072
    #                     if m == 8 and gear_qua == 2:
    #                         e = 0.08
    #                     if m == 9 and gear_qua == 2:
    #                         e = 0.085
    #                     if m == 10 and gear_qua == 2:
    #                         e = 0.09
    #                     # CAREFULLY CUT GEARS
    #                     if m <= 4 and gear_qua == 3:
    #                         e = 0.025
    #                     if m == 5 and gear_qua == 3:
    #                         e = 0.025
    #                     if m == 6 and gear_qua == 3:
    #                         e = 0.03
    #                     if m == 7 and gear_qua == 3:
    #                         e = 0.035
    #                     if m == 8 and gear_qua == 3:
    #                         e = 0.038
    #                     if m == 9 and gear_qua == 3:
    #                         e = 0.041
    #                     if m == 10 and gear_qua == 3:
    #                         e = 0.044
    #                     c = 11860 * e
    #                     Fd = Ft * ((0.164 * Vm * (c * b + Ft)) / (0.164 * Vm + 1.485 * math.sqrt(c * b + Ft)))
    #                     print("Dynamic load= ", round(Fd, 2))
    #
    #         if Fs > Fd:
    #             print("Design is safe")
    #         else:
    #             while Fs < Fd:
    #                 print("\nFs= ", round(Fs, 2), " < Fd= ", round(Fd, 2), "\nDesign is not safe")
    #                 Mt1 = (9.55 * 1000000 * Pd) / N2
    #                 m = int(input("Enter module to be selected: "))
    #                 psi = int(input("Enter the values of psi"))
    #                 b = psi * m
    #                 print("b=", b)
    #                 # TOOTH STRENGTH
    #                 Fs = benstr2 * b * m * Y2
    #                 print("Fs= ", round(Fs, 2))
    #                 # DYNAMIC LOAD
    #                 u = int(input(
    #                     "Enter the method to calculate dynamic load\n1. Barth velocity method\n2. Buckingham method"))
    #                 if u == 1:
    #                     d2 = m * z2
    #                     Ft = (2 * Mt1) / d2
    #                     Vm = (math.pi * d2 * N2) / 60000
    #                     if gear_qua == 1:
    #                         Cv = (5.5 + math.sqrt(Vm)) / 5.5
    #                     if gear_qua == 2:
    #                         Cv = (3 + math.sqrt(Vm)) / 3
    #                     if gear_qua == 3:
    #                         Cv = (6 + math.sqrt(Vm)) / 6
    #                     Fd = Ft * Cv
    #                     print("Dynamic load= ", round(Fd, 2))
    #                 if u == 2:
    #                     d2 = m * z2
    #                     Ft = (2 * Mt1) / d2
    #                     Vm = (math.pi * d2 * N2) / 60000
    #                     # PRECISION GEARS
    #                     if m <= 4 and gear_qua == 1:
    #                         e = 0.0125
    #                     if m == 5 and gear_qua == 1:
    #                         e = 0.0125
    #                     if m == 6 and gear_qua == 1:
    #                         e = 0.015
    #                     if m == 7 and gear_qua == 1:
    #                         e = 0.017
    #                     if m == 8 and gear_qua == 1:
    #                         e = 0.019
    #                     if m == 9 and gear_qua == 1:
    #                         e = 0.0205
    #                     if m == 10 and gear_qua == 1:
    #                         e = 0.022
    #                     # COMMERCIAL GEARS
    #                     if m <= 4 and gear_qua == 2:
    #                         e = 0.05
    #                     if m == 5 and gear_qua == 2:
    #                         e = 0.056
    #                     if m == 6 and gear_qua == 2:
    #                         e = 0.064
    #                     if m == 7 and gear_qua == 2:
    #                         e = 0.072
    #                     if m == 8 and gear_qua == 2:
    #                         e = 0.08
    #                     if m == 9 and gear_qua == 2:
    #                         e = 0.085
    #                     if m == 10 and gear_qua == 2:
    #                         e = 0.09
    #                     # CAREFULLY CUT GEARS
    #                     if m <= 4 and gear_qua == 3:
    #                         e = 0.025
    #                     if m == 5 and gear_qua == 3:
    #                         e = 0.025
    #                     if m == 6 and gear_qua == 3:
    #                         e = 0.03
    #                     if m == 7 and gear_qua == 3:
    #                         e = 0.035
    #                     if m == 8 and gear_qua == 3:
    #                         e = 0.038
    #                     if m == 9 and gear_qua == 3:
    #                         e = 0.041
    #                     if m == 10 and gear_qua == 3:
    #                         e = 0.044
    #                     c = 11860 * e
    #                     Fd = Ft + ((0.164 * Vm * ((c * b) + Ft)) / (0.164 * Vm + 1.485 * math.sqrt((c * b) + Ft)))
    #                     print("Dynamic load= ", round(Fd, 2))
    #                     break
    #         print("\nFs= ", round(Fs, 2), " > Fd=", round(Fd, 2))
    #         print("\nDesign is safe")
    #         # CHECK FOR WEAR
    #         d1 = m * z1
    #         Q = (2 * i) / (i + 1)
    #         E1 = float(input("Enter the value of E1: "))
    #         E2 = float(input("Enter the value of E2: "))
    #         BHNavg = (BHN1 + BHN2) / 2
    #         comstr = (2.8 * BHNavg) - 70
    #         k = (comstr * comstr * math.sin(pres_ang) * ((1 / E1) + (1 / E2))) / 1.4
    #         Fw = d1 * Q * k * b
    #         if Fw > Fd:
    #             print("\n Fw=", round(Fw, 2), "> Fd=", round(Fd, 2), "\nDesign is safe")
    #         else:
    #             while Fw < Fd:
    #                 print("\n Fw=", round(Fw, 2), "< Fd=", round(Fd, 2), "\nDesign is not safe")
    #                 m = input("Enter module to be selected: ")
    #                 d1 = m * z1
    #                 Q = (2 * i) / (i + 1)
    #                 E1 = float(input("Enter the value of E1: "))
    #                 E2 = float(input("Enter the value of E2: "))
    #                 BHNavg = (BHN1 + BHN2) / 2
    #                 comstr = (2.8 * BHNavg) - 70
    #                 k = (comstr * comstr * math.sin(pres_ang) * ((1 / E1) + (1 / E2))) / 1.4
    #                 Fw = d1 * Q * k * b
    #                 break
    #             print("\n Fw=", round(Fw, 2), "> Fd=", round(Fd, 2), "\nDesign is safe")
    #         break
    #
    else:
        round2 = math.sqrt(i)
        N2 = N1 / round2
        print("N2= ", round(N2, 2))
        i1 = i2 = round2
        N21 = N1 / i1
        N12 = round(N21, 2)
        N22 = round(N12 / i2, 2)
        round2 = round(round2, 2)
        print("For 2nd stage \n P= ", P, "\n N1= ", round(N12, 2), "\n N2=", round(N22, 2), "\n i=",
              round(round2, 2))
        # sf = float(input("Enter value of service factor(Sf): "))
        Pd = P * sf
        print("Design Power (Pd) is: ", Pd)
        # pres_ang = int(input("Select pressure angle in degrees "))
        # gear_qua = int(input(
        #     "Select gear quality \n 1. Precision gears, \n 2. Commercially cut gears< \n 3. First class commercial "
        #     "gears \n"))
        z1 = 18
        print("i=", i1)
        z2 = int((z1 * i1) + 1)
        print("\n z1=", z1, " \n z2= ", z2)
        # LEWIS FORM FACTOR
        Y1 = round((0.154 - (0.912 / z1)) * math.pi, 2)
        print("Lewis form factor of pinion Y1= ", round(Y1, 3))
        Y2 = round((0.154 - (0.912 / z2)) * math.pi, 2)
        print("Lewis form factor of gear Y2= ", round(Y2, 3))
        # MATERIAL SELECTION
        # PINION MATERIAL
    #     pinion = int(input(
    #     "Select the material for pinion \n1. C50 \n2. C55 Mn75\n3. 40Cr1\n4. 35Ni1Cr60 \n5. C45 \n6. 15Ni2Cr1Mo25 "
    #         "\n7. 40Ni2Cr1Mo28\n"))
        if pinion == 1:
            # FoS = int(input("Enter the values of factor of safety: "))
            benstr1 = 380 / FoS1
            print("Bending stress= ", round(benstr1, 2))
            # BHN1 = int(input("Enter Brinell Hardness Number= "))
        if pinion == 2:
            # FoS = int(input("Enter the values of factor of safety: "))
            benstr1 = 400 / FoS1
            print("Bending stress= ", round(benstr1, 2))
            # BHN1 = int(input("Enter Brinell Hardness Number= "))
        if pinion == 3:
            # FoS = int(input("Enter the values of factor of safety: "))
            benstr1 = 875 / FoS1
            print("Bending stress= ", round(benstr1, 2))
            # BHN1 = int(input("Enter Brinell Hardness Number= "))
        if pinion == 4:
            # FoS = int(input("Enter the values of factor of safety: "))
            benstr1 = 875 / FoS1
            print("Bending stress= ", round(benstr1, 2))
            # BHN1 = int(input("Enter Brinell Hardness Number= "))
        if pinion == 5:
            benstr1 = 135
            print("Bending stress= ", round(benstr1, 2))
            # BHN1 = int(input("Enter Brinell Hardness Number= "))
        if pinion == 6:
            benstr1 = 300
            print("Bending stress= ", round(benstr1, 2))
            # BHN1 = int(input("Enter Brinell Hardness Number= "))
        if pinion == 7:
            benstr1 = 380
            print("Bending stress= ", round(benstr1, 2))
            # BHN1 = int(input("Enter Brinell Hardness Number= "))
        # GEAR MATERIAL
    #     gear = int(input(
    #         "Select the material for gear \n1. C50 \n2. C55 Mn75\n3. 40Cr1\n4. 35Ni1Cr60 \n5. C45 \n6. 15Ni2Cr1Mo25 "
    #         "\n7. 40Ni2Cr1Mo28\n"))
        if gear == 1:
            # FoS = int(input("Enter the values of factor of safety: "))
            benstr2 = 380 / FoS2
            print("Bending stress= ", round(benstr2, 2))
            # BHN2 = int(input("Enter Brinell Hardness Number= "))
        if gear == 2:
            # FoS = int(input("Enter the values of factor of safety: "))
            benstr2 = 400 / FoS2
            print("Bending stress= ", round(benstr2, 2))
            # BHN2 = int(input("Enter Brinell Hardness Number= "))
        if gear == 3:
            # FoS = int(input("Enter the values of factor of safety: "))
            benstr2 = 875 / FoS2
            print("Bending stress= ", round(benstr2, 2))
            # BHN2 = int(input("Enter Brinell Hardness Number= "))
        if gear == 4:
            # FoS = int(input("Enter the values of factor of safety: "))
            benstr2 = 875 / FoS2
            print("Bending stress= ", round(benstr2, 2))
            # BHN2 = int(input("Enter Brinell Hardness Number= "))
        if gear == 5:
            benstr2 = 135
            print("Bending stress= ", round(benstr2, 2))
            # BHN2 = int(input("Enter Brinell Hardness Number= "))
        if gear == 6:
            benstr2 = 300
            print("Bending stress= ", round(benstr2, 2))
            # BHN2 = int(input("Enter Brinell Hardness Number= "))
        if gear == 7:
            benstr2 = 380
            print("Bending stress= ", round(benstr2, 2))
            # BHN2 = int(input("Enter Brinell Hardness Number= "))
        BHN = BHN1 - BHN2
        while BHN < 30:
            BHN = BHN1 - BHN2
            print("BHN1-BHN2= ", BHN, "<30")
            # BHN1 = int(input("Enter the value of BHN1:- "))
            # BHN2 = int(input("Enter the value of BHN2:- "))
            BHN = BHN1 - BHN2
            print("BHN1-BHN2= ", BHN, ">=30")
            break
        # SELECTION OF WEAKER ELEMENT
        weak1 = round(benstr1 * Y1, 2)
        weak2 = round(benstr2 * Y2, 2)
        if weak1 < weak2:
            print("Since", "Strength of pinion = ", round(weak1, 2), "<", "Strength of gear = ", round(weak2, 2),
                  "\nPinion is weaker")
        else:
            print("Since", "Strength of gear = ", round(weak2, 2), "<", "Strength of pinion = ", round(weak1, 2),
                  "\nGear is weaker")
        # MODULE
        if weak1 < weak2:
            Mt1 = (9.55 * 1000000 * Pd) / N12
            m1 = round(1.26 * pow(Mt1 / (Y1 * benstr1 * 10 * z1), 0.33), 2)
            print("Module= ", round(m1, 2))
            # m = int(input("Enter module to be selected: "))
            # psi = int(input("Enter the values of psi: "))
            b = psi * m
            print("b=", b)
            # TOOTH STRENGTH
            Fs = round(benstr1 * b * m * Y1, 2)
            print("Fs= ", round(Fs, 2))
            # DYNAMIC LOAD
            # u = int(
            #     input("Enter the method to calculate dynamic load\n1. Barth velocity method\n2. Buckingham method"))
            if u == 1:
                d1 = m * z1
                Ft = (2 * Mt1) / d1
                Vm = math.pi * d1 * N12 / 60000
                if gear_qua == 1:
                    Cv = (5.5 + math.sqrt(Vm)) / 5.5
                if gear_qua == 2:
                    Cv = (3 + math.sqrt(Vm)) / 3
                if gear_qua == 3:
                    Cv = (6 + math.sqrt(Vm)) / 6
                Fd = round(Ft * Cv, 2)
                print("Dynamic load= ", round(Fd, 2))
            if u == 2:
                d1 = m * z1
                Ft = (2 * Mt1) / d1
                Vm = (math.pi * d1 * N12) / 60000
                # PRECISION GEARS
                if m <= 4 and gear_qua == 1:
                    e = 0.0125
                if m == 5 and gear_qua == 1:
                    e = 0.0125
                if m == 6 and gear_qua == 1:
                    e = 0.015
                if m == 7 and gear_qua == 1:
                    e = 0.017
                if m == 8 and gear_qua == 1:
                    e = 0.019
                if m == 9 and gear_qua == 1:
                    e = 0.0205
                if m == 10 and gear_qua == 1:
                    e = 0.022
                # COMMERCIAL GEARS
                if m <= 4 and gear_qua == 2:
                    e = 0.05
                if m == 5 and gear_qua == 2:
                    e = 0.056
                if m == 6 and gear_qua == 2:
                    e = 0.064
                if m == 7 and gear_qua == 2:
                    e = 0.072
                if m == 8 and gear_qua == 2:
                    e = 0.08
                if m == 9 and gear_qua == 2:
                    e = 0.085
                if m == 10 and gear_qua == 2:
                    e = 0.09
                # CAREFULLY CUT GEARS
                if m <= 4 and gear_qua == 3:
                    e = 0.025
                if m == 5 and gear_qua == 3:
                    e = 0.025
                if m == 6 and gear_qua == 3:
                    e = 0.03
                if m == 7 and gear_qua == 3:
                    e = 0.035
                if m == 8 and gear_qua == 3:
                    e = 0.038
                if m == 9 and gear_qua == 3:
                    e = 0.041
                if m == 10 and gear_qua == 3:
                    e = 0.044
                c = 11860 * e
                Fd = round(Ft * ((0.164 * Vm * (c * b + Ft)) / (0.164 * Vm + 1.485 * math.sqrt(c * b + Ft))), 2)
                print("Dynamic load= ", round(Fd, 2))
            if Fs > Fd:
                print("Design is safe")
            else:
                print("Design is NOT Safe!!!")
    #             while Fs < Fd:
    #                 print("\nFs= ", round(Fs, 2), " < Fd= ", round(Fd, 2), "\nDesign is not safe")
    #                 Mt1 = (9.55 * 1000000 * Pd) / N12
    #                 m = int(input("Enter module to be selected: "))
    #                 psi = int(input("Enter the values of psi"))
    #                 b = psi * m
    #                 print("b=", b)
    #                 # TOOTH STRENGTH
    #                 Fs = benstr1 * b * m * Y1
    #                 print("Fs= ", round(Fs, 2))
    #                 # DYNAMIC LOAD
    #                 u = int(input(
    #                     "Enter the method to calculate dynamic load\n1. Barth velocity method\n2. Buckingham method"))
    #                 if u == 1:
    #                     d1 = m * z1
    #                     Ft = (2 * Mt1) / d1
    #                     Vm = (math.pi * d1 * N12) / 60000
    #                     if gear_qua == 1:
    #                         Cv = (5.5 + math.sqrt(Vm)) / 5.5
    #                     if gear_qua == 2:
    #                         Cv = (3 + math.sqrt(Vm)) / 3
    #                     if gear_qua == 3:
    #                         Cv = (6 + math.sqrt(Vm)) / 6
    #                     Fd = Ft * Cv
    #                     print("Dynamic load= ", round(Fd, 2))
    #                 if u == 2:
    #                     d1 = m * z1
    #                     Ft = (2 * Mt1) / d1
    #                     Vm = (math.pi * d1 * N12) / 60000
    #                     # PRECISION GEARS
    #                     if m <= 4 and gear_qua == 1:
    #                         e = 0.0125
    #                     if m == 5 and gear_qua == 1:
    #                         e = 0.0125
    #                     if m == 6 and gear_qua == 1:
    #                         e = 0.015
    #                     if m == 7 and gear_qua == 1:
    #                         e = 0.017
    #                     if m == 8 and gear_qua == 1:
    #                         e = 0.019
    #                     if m == 9 and gear_qua == 1:
    #                         e = 0.0205
    #                     if m == 10 and gear_qua == 1:
    #                         e = 0.022
    #                     # COMMERCIAL GEARS
    #                     if m <= 4 and gear_qua == 2:
    #                         e = 0.05
    #                     if m == 5 and gear_qua == 2:
    #                         e = 0.056
    #                     if m == 6 and gear_qua == 2:
    #                         e = 0.064
    #                     if m == 7 and gear_qua == 2:
    #                         e = 0.072
    #                     if m == 8 and gear_qua == 2:
    #                         e = 0.08
    #                     if m == 9 and gear_qua == 2:
    #                         e = 0.085
    #                     if m == 10 and gear_qua == 2:
    #                         e = 0.09
    #                     # CAREFULLY CUT GEARS
    #                     if m <= 4 and gear_qua == 3:
    #                         e = 0.025
    #                     if m == 5 and gear_qua == 3:
    #                         e = 0.025
    #                     if m == 6 and gear_qua == 3:
    #                         e = 0.03
    #                     if m == 7 and gear_qua == 3:
    #                         e = 0.035
    #                     if m == 8 and gear_qua == 3:
    #                         e = 0.038
    #                     if m == 9 and gear_qua == 3:
    #                         e = 0.041
    #                     if m == 10 and gear_qua == 3:
    #                         e = 0.044
    #                     c = 11860 * e
    #                     Fd = Ft + ((0.164 * Vm * ((c * b) + Ft)) / (0.164 * Vm + 1.485 * math.sqrt((c * b) + Ft)))
    #                     print("Dynamic load= ", round(Fd, 2))
    #                     break
    #         print("\nFs= ", round(Fs, 2), " > Fd=", round(Fd, 2))
    #         print("\nDesign is safe")
            # CHECK FOR WEAR
            d1 = m * z1
            Q = (2 * i) / (i + 1)
            # E1 = float(input("Enter the value of E1: "))
            # E2 = float(input("Enter the value of E2: "))
            BHNavg = (BHN1 + BHN2) / 2
            comstr = (2.8 * BHNavg) - 70
            k = (comstr * comstr * math.sin(pres_ang) * ((1 / E1) + (1 / E2))) / 1.4
            Fw = round(d1 * Q * k * b, 2)
            if Fw > Fd:
                print("\n Fw=", round(Fw, 2), "> Fd=", round(Fd, 2), "\nDesign is safe")
            else:
                print("\n Fw=", round(Fw, 2), "< Fd=", round(Fd, 2), "\nDesign is NOT safe")
    #             while Fw < Fd:
    #                 print("\n Fw=", round(Fw, 2), "< Fd=", round(Fd, 2), "\nDesign is not safe")
    #                 m = input("Enter module to be selected: ")
    #                 d1 = m * z1
    #                 Q = (2 * i) / (i + 1)
    #                 E1 = float(input("Enter the value of E1: "))
    #                 E2 = float(input("Enter the value of E2: "))
    #                 BHNavg = (BHN1 + BHN2) / 2
    #                 comstr = (2.8 * BHNavg) - 70
    #                 k = (comstr * comstr * math.sin(pres_ang) * ((1 / E1) + (1 / E2))) / 1.4
    #                 Fw = d1 * Q * k * b
    #                 break
    #         print("\n Fw=", round(Fw, 2), "> Fd=", round(Fd, 2), "\nDesign is safe")
    #     # WHEN GEAR IS WEAKER
    #     if weak2 < weak1:
    #         Mt1 = (9.55 * 1000000 * Pd) / N22
    #         m1 = 1.26 * pow(Mt1 / (Y2 * benstr2 * 10 * z2), 0.33)
    #         print("Module= ", round(m1, 2))
    #         m = int(input("Enter module to be selected: "))
    #         psi = int(input("Enter the values of psi: "))
    #         b = psi * m
    #         print("b=", b)
    #         # TOOTH STRENGTH
    #         Fs = benstr2 * b * m * Y2
    #         print("Fs= ", round(Fs, 2))
    #         # DYNAMIC LOAD
    #         u = int(
    #             input("Enter the method to calculate dynamic load\n1. Barth velocity method\n2. Buckingham method"))
    #         if u == 1:
    #             d2 = m * z2
    #             Ft = (2 * Mt1) / d2
    #             Vm = (math.pi * d2 * N22) / 60000
    #             if gear_qua == 1:
    #                 Cv = (5.5 + math.sqrt(Vm)) / 5.5
    #             if gear_qua == 2:
    #                 Cv = (3 + math.sqrt(Vm)) / 3
    #             if gear_qua == 3:
    #                 Cv = (6 + math.sqrt(Vm)) / 6
    #             Fd = Ft * Cv
    #             print("Dynamic load= ", round(Fd, 2))
    #         if u == 2:
    #             d2 = m * z2
    #             Ft = (2 * Mt1) / d2
    #             Vm = (math.pi * d2 * N22) / 60000
    #             # PRECISION GEARS
    #             if m <= 4 and gear_qua == 1:
    #                 e = 0.0125
    #             if m == 5 and gear_qua == 1:
    #                 e = 0.0125
    #             if m == 6 and gear_qua == 1:
    #                 e = 0.015
    #             if m == 7 and gear_qua == 1:
    #                 e = 0.017
    #             if m == 8 and gear_qua == 1:
    #                 e = 0.019
    #             if m == 9 and gear_qua == 1:
    #                 e = 0.0205
    #             if m == 10 and gear_qua == 1:
    #                 e = 0.022
    #                 # COMMERCIAL GEARS
    #             if m <= 4 and gear_qua == 2:
    #                 e = 0.05
    #             if m == 5 and gear_qua == 2:
    #                 e = 0.056
    #             if m == 6 and gear_qua == 2:
    #                 e = 0.064
    #             if m == 7 and gear_qua == 2:
    #                 e = 0.072
    #             if m == 8 and gear_qua == 2:
    #                 e = 0.08
    #             if m == 9 and gear_qua == 2:
    #                 e = 0.085
    #             if m == 10 and gear_qua == 2:
    #                 e = 0.09
    #                 # CAREFULLY CUT GEARS
    #             if m <= 4 and gear_qua == 3:
    #                 e = 0.025
    #             if m == 5 and gear_qua == 3:
    #                 e = 0.025
    #             if m == 6 and gear_qua == 3:
    #                 e = 0.03
    #             if m == 7 and gear_qua == 3:
    #                 e = 0.035
    #             if m == 8 and gear_qua == 3:
    #                 e = 0.038
    #             if m == 9 and gear_qua == 3:
    #                 e = 0.041
    #             if m == 10 and gear_qua == 3:
    #                 e = 0.044
    #             c = 11860 * e
    #             Fd = Ft * ((0.164 * Vm * (c * b + Ft)) / (0.164 * Vm + 1.485 * math.sqrt(c * b + Ft)))
    #             print("Dynamic load= ", round(Fd, 2))
    #             if Fs > Fd:
    #                 print("Design is safe")
    #             else:
    #                 while Fs < Fd:
    #                     print("\nFs= ", round(Fs, 2), " < Fd= ", round(Fd, 2), "\nDesign is not safe")
    #                     Mt1 = (9.55 * 1000000 * Pd) / N22
    #                     m = int(input("Enter module to be selected: "))
    #                     psi = int(input("Enter the values of psi"))
    #                     b = psi * m
    #                     print("b=", b)
    #                     # TOOTH STRENGTH
    #                     Fs = benstr2 * b * m * Y2
    #                     print("Fs= ", round(Fs, 2))
    #                     # DYNAMIC LOAD
    #                     u = int(input(
#                         "Enter the method to calculate dynamic load\n1. Barth velocity method\n2. Buckingham method"
    #                     ))
    #                     if u == 1:
    #                         d2 = m * z2
    #                         Ft = (2 * Mt1) / d2
    #                         Vm = (math.pi * d2 * N22) / 60000
    #                         if gear_qua == 1:
    #                             Cv = (5.5 + math.sqrt(Vm)) / 5.5
    #                         if gear_qua == 2:
    #                             Cv = (3 + math.sqrt(Vm)) / 3
    #                         if gear_qua == 3:
    #                             Cv = (6 + math.sqrt(Vm)) / 6
    #                         Fd = Ft * Cv
    #                         print("Dynamic load= ", round(Fd, 2))
    #                     if u == 2:
    #                         d2 = m * z2
    #                         Ft = (2 * Mt1) / d2
    #                         Vm = (math.pi * d2 * N22) / 60000
    #                         # PRECISION GEARS
    #                         if m <= 4 and gear_qua == 1:
    #                             e = 0.0125
    #                         if m == 5 and gear_qua == 1:
    #                             e = 0.0125
    #                         if m == 6 and gear_qua == 1:
    #                             e = 0.015
    #                         if m == 7 and gear_qua == 1:
    #                             e = 0.017
    #                         if m == 8 and gear_qua == 1:
    #                             e = 0.019
    #                         if m == 9 and gear_qua == 1:
    #                             e = 0.0205
    #                         if m == 10 and gear_qua == 1:
    #                             e = 0.022
    #                         # COMMERCIAL GEARS
    #                         if m <= 4 and gear_qua == 2:
    #                             e = 0.05
    #                         if m == 5 and gear_qua == 2:
    #                             e = 0.056
    #                         if m == 6 and gear_qua == 2:
    #                             e = 0.064
    #                         if m == 7 and gear_qua == 2:
    #                             e = 0.072
    #                         if m == 8 and gear_qua == 2:
    #                             e = 0.08
    #                         if m == 9 and gear_qua == 2:
    #                             e = 0.085
    #                         if m == 10 and gear_qua == 2:
    #                             e = 0.09
    #                         # CAREFULLY CUT GEARS
    #                         if m <= 4 and gear_qua == 3:
    #                             e = 0.025
    #                         if m == 5 and gear_qua == 3:
    #                             e = 0.025
    #                         if m == 6 and gear_qua == 3:
    #                             e = 0.03
    #                         if m == 7 and gear_qua == 3:
    #                             e = 0.035
    #                         if m == 8 and gear_qua == 3:
    #                             e = 0.038
    #                         if m == 9 and gear_qua == 3:
    #                             e = 0.041
    #                         if m == 10 and gear_qua == 3:
    #                             e = 0.044
    #                         c = 11860 * e
    #                         Fd = Ft + ((0.164 * Vm * ((c * b) + Ft)) / (
    #                                     0.164 * Vm + 1.485 * math.sqrt((c * b) + Ft)))
    #                         print("Dynamic load= ", round(Fd, 2))
    #                         break
    #                 print("\nFs= ", round(Fs, 2), " > Fd=", round(Fd, 2))
    #                 print("\nDesign is safe")
    #                 # CHECK FOR WEAR
    #                 d1 = m * z1
    #                 Q = (2 * i) / (i + 1)
    #                 E1 = float(input("Enter the value of E1: "))
    #                 E2 = float(input("Enter the value of E2: "))
    #                 BHNavg = (BHN1 + BHN2) / 2
    #                 comstr = (2.8 * BHNavg) - 70
    #                 k = (comstr * comstr * math.sin(pres_ang) * ((1 / E1) + (1 / E2))) / 1.4
    #                 Fw = d1 * Q * k * b
    #                 if Fw > Fd:
    #                     print("\n Fw=", round(Fw, 2), "> Fd=", round(Fd, 2), "\nDesign is safe")
    #                 else:
    #                     while Fw < Fd:
    #                         print("\n Fw=", round(Fw, 2), "< Fd=", round(Fd, 2), "\nDesign is not safe")
    #                         m = input("Enter module to be selected: ")
    #                         d1 = m * z1
    #                         Q = (2 * i) / (i + 1)
    #                         E1 = float(input("Enter the value of E1: "))
    #                         E2 = float(input("Enter the value of E2: "))
    #                         BHNavg = (BHN1 + BHN2) / 2
    #                         comstr = (2.8 * BHNavg) - 70
    #                         k = (comstr * comstr * math.sin(pres_ang) * ((1 / E1) + (1 / E2))) / 1.4
    #                         Fw = d1 * Q * k * b
    #                         break
    #                     print("\n Fw=", round(Fw, 2), "> Fd=", round(Fd, 2), "\nDesign is safe")

    return Pd, z1, z2, Y1, Y2, benstr1, benstr2, BHN, weak1, weak2, m1, b, Fs, Fd, Fw, N12, N22, round2
