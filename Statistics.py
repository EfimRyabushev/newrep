inputint = open(int_data_random.txt)
inputfloat = open(float_data_random.txt)

dataint = list (map (int, inputint.read()))
datafloat = list (map (float, inputfloat.read()))

lenint = len(dataint)
lenfloat = len(datafloat)
#Среднее арифметическое действительных чисел
midarifm = sum (datafloat) / lenfloat
print (midarifm)

#Среднее квадратичное отклонение.
counter = 0
for i in datafloat
   counter += i ** 2
sigma = (counter / lenfloat - midarifm ** 2) ** 0.5
print (sigma)

#max и min
maximum = max (datafloat)
minimum = min (datafloat)
indexmaximum = datafloat.index(maximum)
indexminimum = datafloat.index(minimum)
print (maximum, indexmaximum)
print (minimum, indexminimum)



 
