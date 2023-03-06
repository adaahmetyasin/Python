import random

n = random.randint(0,6)

studentID = [101,102,103,104,105,106,107]
name = ["Ahmet","Ezgi","Fatih","Murat","Hande","Rasim","Deniz"]
midterm = [70,85,65,45,50,35,90]
final = [85,100,45,55,60,75,70]

print("{} takes {} from midterm and {} from final exams. Overall point is calculated as {}.".format(name[n],midterm[n],final[n],int(midterm[n]*2/5 + final[n]*3/5)))