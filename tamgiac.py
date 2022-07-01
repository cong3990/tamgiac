#============================ASSIGNMENT 1=============================
from math import sqrt, acos, degrees
from sympy import symbols, Eq, solve


# Ask user to input coordinates of A, B, C
# def toado():
#     coords = [None] * 6
#     index = ["Ax", "Ay", "Bx", "By", "Cx", "Cy"]
#
#     # If coordinate is not a number, ask user to input again
#     for x in range(6):
#         while coords[x] == None:
#             try:
#                 coords[x] = float(input(f"Enter coordinate of {index[x]}:\n"))
#             except:
#                 print("Please enter a number.")
#                 continue
#             else:
#                 break
#     return coords


# TODO 1: check if A, B, C make a triangle (Using slopes formula method)
"""
If Slope of AB = slope of BC = slope of AC, then A, B and C are collinear points

Source: https://www.urbanpro.com/gre/how-to-determine-if-points-are-collinear#:~:text
=Three%20points%20are%20collinear%20if,are%20said%20to%20be%20collinear
"""
def kiemtra_tamgiac(input):
    # Assign input coordinates
    Ax = input[0]
    Ay = input[1]
    Bx = input[2]
    By = input[3]
    Cx = input[4]
    Cy = input[5]

    # Slope of AB
    AB_x = Bx - Ax
    AB_y = By - Ay
    slopeAB = AB_y / AB_x

    # Slope of AC
    AC_x = Cx - Ax
    AC_y = Cy - Ay
    slopeAC = AC_y / AC_x

    # Slope of BC
    BC_x = Cx - Bx
    BC_y = Cy - By
    slopeBC = BC_y / BC_x

    # Check if 3 points are collinear, if they are, they cannot form triangle, return False
    if slopeAB == slopeAC == slopeBC:
        return False
    else:
        return True


# TODO 2: Get sides' lengths and angles of triangle
def goccanh_tamgiac(input):
    # Assign input coordinates
    Ax = input[0]
    Ay = input[1]
    Bx = input[2]
    By = input[3]
    Cx = input[4]
    Cy = input[5]

    # Calculate lengths of AB, BC, AC
    AB = sqrt((Bx - Ax)**2 + (By - Ay)**2)
    BC = sqrt((Cx - Bx)**2 + (Cy - By)**2)
    AC = sqrt((Cx - Ax)**2 + (Cy - Ay)**2)

    # Calculate A, B, C angles (sum of 3 angles in a triangle is 180)
    angle_A = round(degrees(acos((AB**2 + AC**2 - BC**2) / (2*AB*AC))), 2)
    angle_B = round(degrees(acos((AB**2 + BC**2 - AC**2) / (2*AB*BC))), 2)
    angle_C = round(180 - angle_A - angle_B, 2)

    dodai_va_goc = [round(AB, 2), round(BC, 2), round(AC, 2), angle_A, angle_B, angle_C]
    return dodai_va_goc


# TODO 3: Check what type the triangle is: Equilateral(Deu), Right and Isosceles(Vuong can), Right(Vuong), Obtuse and Isosceles(Tu can), Obtuse(Tu), Isosceles(Can), or Normal
def xet_tamgiac(input):
    angle_type = None
    here = ["A", "B", "C"]
    # Get lengths from goccanh_tamgiac function
    lengths = goccanh_tamgiac(input)[0:3]
    # Get angles from goccanh_tamgiac function
    angles = goccanh_tamgiac(input)[3:]

    # If triangle is Equilateral, return the conclusion
    if angles[0] == angles[1] == angles[2]:
        return "ABC la tam giac deu"
    # Check if triangle is Isosceles
    if lengths[0] == lengths[1] or lengths[1] == lengths[2] or lengths[0] == lengths[2]:
        angle_type = "Isosceles"

    # Check if triangle is Obtuse, Right
    for x in range(3):
        # If Obtuse
        if angles[x] > 90:
            # and Isosceles
            if angle_type == "Isosceles":
                return f"ABC la tam giac tu va can tai dinh {here[x]}"
            # If only Obtuse
            else:
                return f"ABC la tam giac tu tai dinh {here[x]}"

        # If Right
        elif angles[x] == 90:
            # and Isosceles
            if angle_type == "Isosceles":
                return f"ABC la tam giac vuong can tai dinh {here[x]}"
            # If only Right
            else:
                return f"ABC la tam giac vuong tai dinh {here[x]}"

    # If not Obtuse or Right, check if it's a normal triangle or Isosceles
    for x in range(3):
            # If only Isosceles
            if angle_type == "Isosceles":
                return f"ABC la tam giac can tai dinh {here[x]}"
            # Just a normal triangle
            else:
                return "ABC la tam giac thuong"


# TODO 4: Calculate area of the triangle
def dientich_tamgiac(input):
    # Get sides' lengths of the triangle
    lengths = goccanh_tamgiac(input)[0:3]

    # Assign sides' lengths to variables
    a = lengths[0]
    b = lengths[1]
    c = lengths[2]

    # Apply Heron formula: area = sqrt(p*(p-a)*(p-)*(p-c)) with p = (1/2)*(a +b +c)
    p = (1/2) * (a + b + c)
    area = round(sqrt(p * (p - a) * (p - b) * (p - c)), 2)

    return area


# TODO 5: Calculate altitudes (apply area formula: S = (1/2) * BC * dcA)
def duongcao_tamgiac(input):
    # Get sides' lengths of the triangle
    lengths = goccanh_tamgiac(input)

    # Get area of the triangle
    area = dientich_tamgiac(input)

    # Assign sides' lengths to variables
    AB = lengths[0]
    BC = lengths[1]
    AC = lengths[2]

    # Calculate Altitudes from area and sides' lengths
    dcA = round(2 * area / BC, 2)
    dcB = round(2 * area / AC, 2)
    dcC = round(2 * area / AB, 2)
    duong_cao = [dcA, dcB, dcC]

    return duong_cao


# TODO 6: Get Centroid and Orthorcenter

def tam_tamgiac(input):
    # Assign input coordinates
    Ax = input[0]
    Ay = input[1]
    Bx = input[2]
    By = input[3]
    Cx = input[4]
    Cy = input[5]

    # Get centroid(trong tam)'s coordinate
    Gx = round((Ax + Bx + Cx) / 3, 2)
    Gy = round((Ay + By + Cy) / 3, 2)

    # Use sympy to solve equations to get orthocenter coordinates
    Hx, Hy = symbols("Hx Hy")

    # AH and BH altitudes equations
    AH = Eq((Cx - Bx)*(Hx - Ax) + (Cy - By)*(Hy - Ay), 0)
    BH = Eq((Ax - Cx)*(Hx - Bx) + (Ay - Cy)*(Hy - By), 0)

    # Results of euqations is a dictionary
    # solve take 2 arguments, equation(s)(AH, BH) and variable(s)(Hx, Hy) needed to find
    orthocenter = solve((AH, BH), (Hx, Hy))

    trongtam_tructam = [Gx, Gy, round(orthocenter[Hx], 2), round(orthocenter[Hy], 2)]
    return trongtam_tructam


# TODO 7: Calculate lengths from 3 apexes to centroid
def trungtuyen_tamgiac(input):
    # Assign input coordinates
    Ax = input[0]
    Ay = input[1]
    Bx = input[2]
    By = input[3]
    Cx = input[4]
    Cy = input[5]

    # Get centroid's coordinate
    trong_tam = tam_tamgiac(input)[0:2]
    Gx = trong_tam[0]
    Gy = trong_tam[1]

    # Calculate lengths of AG, BG, CG
    AG = round(sqrt((Gx - Ax)**2 + (Gy - Ay)**2), 2)
    BG = round(sqrt((Gx - Bx) ** 2 + (Gy - By) ** 2), 2)
    CG = round(sqrt((Gx - Cx) ** 2 + (Gy - Cy) ** 2), 2)

    trungtruyen = [AG, BG, CG]
    return trungtruyen


def giaima_tamgiac(input):
    # Check if input coordinates is a list of 6 numbers
    try:
        Ax = float(input[0])
        Ay = float(input[1])
        Bx = float(input[2])
        By = float(input[3])
        Cx = float(input[4])
        Cy = float(input[5])
    except ValueError:
        print("Input number only. Please check your input. ")
    except IndexError:
        print("Not enough information for coordinates. Please check your input.")
    except TypeError:
        print("Input is a list ([]) of 6 numbers. Make sure your input is in list format: [Ax, Ay, Bx, By, Cx, Cy].")

    if len(input) > 6:
        print("Only 6 numbers for coordinates needed. Please check your input.")
        return

    # Print points' coordinates
    print('\033[1m' + f"Toa do 3 diem can xet:\nA({input[0]}, {input[1]}) \nB({input[2]}, {input[3]}) \nC({input[4]}, {input[5]})" + '\033[0m')

    # Check if A, B, C form a triangle
    tamgiac = kiemtra_tamgiac(input)
    if tamgiac == True:
        print("A, B, C hop thanh mot tam giac")
    else:
        print("A, B, C khong hop thanh mot tam giac")
        return

    # Get sides' lengths and angles
    goccanh = goccanh_tamgiac(input)
    print('\033[1m' + "\n1. So do co ban cua tam giac" + '\033[0m')
    print(f"Chieu dai canh AB: {goccanh[0]}")
    print(f"Chieu dai canh BC: {goccanh[1]}")
    print(f"Chieu dai canh CA: {goccanh[2]}")
    print(f"Goc A: {goccanh[3]} \nGoc B: {goccanh[4]}  \nGoc C: {goccanh[5]}")

    # Triangle type
    print("\n" + xet_tamgiac(input))

    # Triangle area
    dientich = dientich_tamgiac(input)
    print('\033[1m' + f"\n2. Dien tich cua tam giac ABC: {dientich}" + '\033[0m')

    # Lengths of Altitudes and from apexes to centroid
    duongcao = duongcao_tamgiac(input)
    trungtuyen = trungtuyen_tamgiac(input)

    print('\033[1m' + "\n3. So do nang cao tam giac ABC" + '\033[0m')
    print(f"Do dai duong cao tu dinh A: {duongcao[0]}")
    print(f"Do dai duong cao tu dinh B: {duongcao[1]}")
    print(f"Do dai duong cao tu dinh C: {duongcao[2]}")
    print(f"Khoang cach den trong tam tu dinh A: {trungtuyen[0]}")
    print(f"Khoang cach den trong tam tu dinh B: {trungtuyen[1]}")
    print(f"Khoang cach den trong tam tu dinh C: {trungtuyen[2]}")

    # Centroid and orthocenter coordinates
    diem_dac_biet = tam_tamgiac(input)
    print('\033[1m' + "\n4. Toa do mot so diem dac biet cua tam giac ABC: " + '\033[0m')
    print(f"Toa do trong tam: [{diem_dac_biet[0]}, {diem_dac_biet[1]}]")
    print(f"Toa do truc tam: [{diem_dac_biet[2]}, {diem_dac_biet[3]}]")


# coords = toado()
giaima_tamgiac([1, 1, 2, 2, 3, 1])