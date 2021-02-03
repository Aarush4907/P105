import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics 
count = []
sum1 = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum1.append(dice1+dice2)
    count.append(i)
mean = sum(sum1)/len(count)
print(mean) 
std_deviation=statistics.stdev(sum1)
median=statistics.median(sum1)
mode=statistics.mode(sum1)
print(mode)
print(median)
print(std_deviation)
