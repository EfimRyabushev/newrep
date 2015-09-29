import random

outputint = open ('int_data_random.txt', 'w')
outputfloat = open ('float_data_random.txt', 'w')

datafloat = [str (random.random()) for i in range(1000000)]
dataint = [str (random.randint(1, 100)) for i in range(1000000)]
outputint.write(' '.join(dataint))
outputfloat.write(' '.join(datafloat))


