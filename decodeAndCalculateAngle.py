import math

# This is the test data to test from
raw_data_after_inital_conversion = "c65aec2ac3df09e0ec04c2aa0e37ec3bc2720e19"

#Step 0: This is the parent fucntion which handles everything
def functionHandler (data):
    arr = toClassify(data);
    face = findGroundFace(arr)[0]
    return (calculateAngle(arr, face))

#Step 1: Check is it ACC type (begins c6), GYRO Type (begins c7) or EMG (begins e8), and switch
def toClassify (data):
    if (data.startswith('c6')):
        return decodeCTypeData("ACC", data)
    elif (data.startswith('c7')):
        return decodeETypeData("GYRO", data)
    elif (data.startswith('e8')):
        return decodeETypeData("EMG", data)
    else:
        return("ERROR: Illegal Data Format")

#Step 2: Decoding C-Type Data
def decodeCTypeData(sType, data):
    #Step 2.1: Divide the string into 4-lenght chunck parts
    n = 4
    chunks = [data[i:i+n] for i in range(0, len(data), n)]

    #Index Values for the Array: 0 -> Sensor Type, 1, 2, 3 -> X1, Y1, Z1 (respectively); 4, 5, 6 -> X2, Y2, Z2 (respectively); 7, 8, 9 -> X3, Y3, Z3 (respectively);
    decArray = [sType]
    for x in chunks[1:]:
        #Step 2.2: Convert to Hexadecimal Base-16 to Decimal Base-10 
        d = int(x, base=16)
        #Step 2.3: Perform " > 32767 " task
        if (d > 32767):
            d = d - 65536
        #Step 2.4: Convery data to miligrams (mg)
        d = d / 16
        #Step 2.5: Add this data to 'decArray' Array
        decArray.append(d);   
    #Step 2.6: Return decArray
    return decArray

#Step 3: (PENDING) Alririthm for E-Type Data
def decodeETypeData(sType, data):
    return ("Work in Progress...")

#Step 4: Determine the face towards ground (closest to '981'). 
# Return an array:
# [index] -> description
# 0 -> face that is facing the ground
# 1 -> indexes for x, y & z that is facing the ground
# 2 -> index 2 -> axises that is facing the ground
def findGroundFace (Arrdata):
    if (not(Arrdata[0] == "ACC")):
        return ("Error: Illegal Data Format")
    else:
        tempoArray = []
        for x in Arrdata[1:]:
            tempoArray.append(x)
        closestValueIndex = min(range(len(tempoArray)), key = lambda i: abs(abs(tempoArray[i])-(981)))
        if (closestValueIndex >= 0 and closestValueIndex <=2):
            return ([1, [1, 2, 3], "X1, Y1, Z1"])
        elif (closestValueIndex >= 3 and closestValueIndex <=5):
            return ([2, [4, 5, 6], "X2, Y2, Z2"])
        else:
            return ([3, [7, 8, 9], "X3, Y3, Z3"])


#Step 5: Calculating the Angle (angle = cos-inverse  [( acc y) / ( SQRT(acc x2 +acc y2 +acc z2) )]
def calculateAngle (dataArray, face):
    if (face == 1):
        return (math.acos (abs(dataArray[2]) / (math.sqrt((dataArray[1] * dataArray[1]) + (dataArray[2] * dataArray[2]) + (dataArray[3] * dataArray[3])))))
    elif (face == 2):
        return (math.acos (abs(dataArray[5]) / (math.sqrt((dataArray[4] * dataArray[4]) + (dataArray[5] * dataArray[5]) + (dataArray[6] * dataArray[6])))))
    else:
        return (math.acos (abs(dataArray[8]) / (math.sqrt((dataArray[7] * dataArray[7]) + (dataArray[8] * dataArray[8]) + (dataArray[9] * dataArray[9])))))



print (functionHandler (raw_data_after_inital_conversion))
