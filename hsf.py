#a function to calculate slope and intercept given two points
def slope_intercept (point_1, point_2):
    try:
        slope = (point_1[0] - point_2[0])/(point_1[1] - point_2[1])
        intercept = point_1[0] - slope * point_1[1]
    except:
        slope = "infinite"
        intercept = "infinite"

    return slope, intercept

#define boundary line
A = (22.37751667 , 113.9022667) #LAT (Y), LON (X)
B = (22.37335 , 113.9022667)
C = (22.37335 , 113.8982667)
D = (22.38998333 , 113.8850833)
E = (22.38996667 , 113.8691167)
F = (22.39665 , 113.8691167)
G = (22.39668333 , 113.8883333)

def B_1 (LAT, LON): #becoz it is vertical or nearly vertical, we have three cases
    slope, intercept = slope_intercept(F, E)
    if slope == "infinite":
        if LON > F[1]:
            return True
    elif slope > 0:
        if LAT - slope * LON - intercept < 0:
            return True
    elif slope < 0:
        if LAT - slope * LON - intercept > 0:
            return True

def B_2 (LAT, LON):
    slope, intercept = slope_intercept(F, G) #becoz it is nearly a horizontal line. slope doesnt matter
    if LAT - slope * LON - intercept > 0:
        return True

def B_3_left (LAT): #it is a vertical line
    if  LAT  < G[1]:
        return True

def B_3_right (LAT): #it is a vertical line
    if  LAT  > G[1]:
        return True

def B_4 (LAT, LON): #becoz it is nearly a horizontal line. slope doesnt matter
    slope, intercept = slope_intercept(C, B)
    if LAT - slope * LON - intercept > 0:
        return True

def B_5 (LAT, LON): #becoz it is nearly a horizontal line. slope doesnt matter
    slope, intercept = slope_intercept(E, D)
    if LAT - slope * LON - intercept < 0:
        return True

def B_6 (LAT, LON): #it is clearly a negative slope line
    slope, intercept = slope_intercept(D, C)
    if LAT - slope * LON - intercept < 0:
        return True

def B_7 (LAT, LON): #becoz it is vertical or nearly vertical, we have three cases
    slope, intercept = slope_intercept(A, B)
    if slope == "infinite":
        if LON > A[1]:
            return True
    elif slope > 0:
        if LAT - slope * LON - intercept < 0:
            return True
    elif slope < 0:
        if LAT - slope * LON - intercept > 0:
            return True

def B_8 (LAT, LON): #clearly have negative slope
    slope, intercept = slope_intercept(A, G)
    if LAT - slope * LON - intercept > 0:
        return True

#defined not traveling through the zone
def notInZone(LAT, LON):

    #initialize boundary value and deviation value as false
    B1 = False
    B2 = False
    B3_left = False
    B3_right = False
    B4 = False
    B5 = False
    B6 = False
    B7 = False
    B8 = False
    deviation = False

    #check passing boundary line
    B1 = B_1 (LAT, LON)

    B2 = B_2 (LAT, LON)

    B3_left = B_3_left (LON)

    B3_right = B_3_right (LON)

    B4 = B_4 (LAT, LON)

    B5 = B_5 (LAT, LON)

    B6 = B_6 (LAT, LON)

    B7 = B_7 (LAT, LON)

    B8 = B_8 (LAT, LON)

    #check deviation
    if B1 == True and B2 == True and B3_left == True: #deviation in area 1
        deviation = True

    if B1 == True and B4 == True and B5 == True and B6 == True: #deviation in area 2
        deviation = True

    if B3_right == True and B4 == True: #deviation in area 3
        if B7 == True or B8 == True:
            deviation = True

    return deviation

#define enter the SCZ
def enteredZone (LAT, LON):
    B1 = False
    B4 = False

    #check passing boundary line
    B1 = B_1 (LAT, LON)

    B4 = B_4 (LAT, LON)


    if B1 == True  and B4 == True and notInZone(LAT, LON) == False:
        return True
    else:
        return False