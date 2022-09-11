iPhone12 = [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]
Xiaomi_Mi11 = [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]
Samsung_Galaxy_21 = [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]
#Посчитать и вывести суммарное количество продаж для каждого товара
totalsumiPhone12 = 0
for sum_iPhone12 in iPhone12:
    totalsumiPhone12 += sum_iPhone12
print("Total sales for iPhone12 is:", totalsumiPhone12)
totalsumXiaomi_Mi11 = 0
for sum_Xiaomi_Mi11 in Xiaomi_Mi11:
    totalsumXiaomi_Mi11 += sum_Xiaomi_Mi11
print("Total sales for Xiaomi_Mi11 is:", totalsumXiaomi_Mi11)
totalsumSamsung_Galaxy_21 = 0
for sum_Samsung_Galaxy_21 in Samsung_Galaxy_21:
    totalsumSamsung_Galaxy_21 += sum_Samsung_Galaxy_21
print("Total sales for Samsung_Galaxy_21 is:", totalsumSamsung_Galaxy_21)
#Посчитать и вывести среднее количество продаж для каждого товара
avg_sales_iPhone12 = totalsumiPhone12 / len(iPhone12)
print(f"average sales for iPhone12 is: {avg_sales_iPhone12}")
avg_Xiaomi_Mi11 = totalsumXiaomi_Mi11 / len(Xiaomi_Mi11)
print(f"average sales for Xiaomi_Mi11 is: {avg_Xiaomi_Mi11}")
avg_Samsung_Galaxy_21 = totalsumSamsung_Galaxy_21 / len(Samsung_Galaxy_21)
print(f"average sales for Xiaomi_Mi11 is: {avg_Samsung_Galaxy_21}")
# Посчитать и вывести суммарное количество продаж всех товаров
sum_of_all_sales = totalsumiPhone12+totalsumXiaomi_Mi11+totalsumSamsung_Galaxy_21
print(f"sum sales for all phones is: {sum_of_all_sales}")
#Посчитать и вывести среднее количество продаж всех товаров
avg_sales_of_all_phones = avg_sales_iPhone12 + avg_Xiaomi_Mi11 + avg_Samsung_Galaxy_21
print(f"average sales  for all phones is: {avg_sales_of_all_phones}")