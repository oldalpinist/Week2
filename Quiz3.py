iPhone12 = [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]
Xiaomi_Mi11 = [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]
Samsung_Galaxy_21 = [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]
print(iPhone12)
print(Xiaomi_Mi11)
print(Samsung_Galaxy_21)
sumOfiPhone12 = sum(iPhone12)
sumOfXiaomi_Mi11 = sum(Xiaomi_Mi11)
sumOfSamsung_Galaxy_21 = sum(Samsung_Galaxy_21)
print("Total sales for iPhone12:", sumOfiPhone12)
print("Total sales for Xiaomi_Mi11:", sumOfXiaomi_Mi11)
print("Total sales for sumOfSamsung_Galaxy_21:", sumOfSamsung_Galaxy_21)
Average_value_iPhone12 = sumOfiPhone12/len(iPhone12)
print ("Average value sales of the iPhone12:", Average_value_iPhone12)
Average_value_Xiaomi_Mi11 = sumOfXiaomi_Mi11/len(Xiaomi_Mi11)
print ("Average value sales of the Xiaomi_Mi11:", Average_value_Xiaomi_Mi11)
Average_Samsung_Galaxy_21 = sumOfSamsung_Galaxy_21/len(Samsung_Galaxy_21)
print ("Average value sales of the Samsung_Galaxy_21:", Average_Samsung_Galaxy_21)
sumofallphones = sumOfiPhone12+sumOfXiaomi_Mi11+sumOfSamsung_Galaxy_21
print ("Total sales for all phones:", sumofallphones)
Average_value_allphones = Average_value_iPhone12+Average_value_Xiaomi_Mi11+Average_Samsung_Galaxy_21
print ("Average value sales of the allphones:", Average_value_allphones)


