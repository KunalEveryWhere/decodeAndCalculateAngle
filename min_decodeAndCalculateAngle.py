#OG: 0.09894371032714844 ms
#ver1: 0.08273124694824219 ms

import pyjion; pyjion.enable()

import math
import time


# This is the test data to test from
raw_data_after_inital_conversion = "c65aec2ac3df09e0ec04c2aa0e37ec3bc2720e19"
start = time.time()

#Step 0: This is the parent fucntion which handles everything
def functionHandler (data):
    if (data.startswith('c6') or data.startswith('c7')):
        chunks = [data[i:i+4] for i in range(0, len(data), 4)]
        decArray = ['ACC'] if data.startswith('c6') else ['GYRO']
        print("Fold 1 : ", (time.time() - start)* 10**3 , "ms")

        #This segment can be optimized further (begin)
        for x in chunks[1:]:
            d = int(x, base=16)
            d = (d - 65536) if d > 32767 else d
            d /= 16
            decArray.append(d)
        #This segment can be optimized further (end)
        
        print("Fold 2 : ", (time.time() - start)* 10**3 , "ms")
        closestValueIndex = min(range(len(decArray[1:])), key = lambda i: abs(abs(decArray[1:][i])-(981)))
        if (closestValueIndex >= 0 and closestValueIndex <=2):
            return (math.acos (abs(decArray[2]) / (math.sqrt((decArray[1] * decArray[1]) + (decArray[2] * decArray[2]) + (decArray[3] * decArray[3])))))
        elif (closestValueIndex >= 3 and closestValueIndex <=5):
            print("Fold 3 : ", (time.time() - start)* 10**3 , "ms")
            return (math.acos (abs(decArray[5]) / (math.sqrt((decArray[4] * decArray[4]) + (decArray[5] * decArray[5]) + (decArray[6] * decArray[6])))))
        else:
            return (math.acos (abs(decArray[8]) / (math.sqrt((decArray[7] * decArray[7]) + (decArray[8] * decArray[8]) + (decArray[9] * decArray[9])))))
    elif (data.startswith('e8')):
        return ("EMG Data, [under progress]")
    else:
        return("ERROR: Illegal Data Format")
    

print (functionHandler (raw_data_after_inital_conversion))
print("Fold 4 (overall): ", (time.time() - start)* 10**3 , "ms")
