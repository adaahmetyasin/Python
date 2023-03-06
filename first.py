print("This program computes coordinates in open traverse series.")#I told what program does(from Lecture Notes 2.2)
#An open traverse is a polygon that begins at a point with known coordinates and finishes at a position with unknown coordinates.
a_0628=str(input("Please enter the point ID of first known point:"))#I asked to users name of point(from Lecture  Notes2.2 and Lecture Notes3.1)
b_0628=str(input("Please enter the point ID of second known point:"))#I asked to users name of point(from Lecture  Notes2.2 and Lecture Notes3.1)
c_0628=int(input("Please enter the number of unknown traverse point:"))#I asked to users number of points(from Lecture  Notes2.2 and Lecture Notes3.1)
d_0628=str(input("Please enter the point ID of first unknown point:"))#I asked to users name of point(from Lecture  Notes2.2 and Lecture Notes3.1)
e_0628=str(input("Please enter the point ID of second unknown point:"))#I asked to users name of point(from Lecture  Notes2.2 and Lecture Notes3.1)
f_0628=str(input("Please enter the point ID of third unknown point:"))#I asked to users name of point(from Lecture  Notes2.2 and Lecture Notes3.1)
g_0628=float(input("Please enter the traverse angle of second known point(grad):"))#I asked to users angle of point.I am going to use it to calculate azimuth.(from Lecture  Notes2.2 and Lecture Notes3.1)
h_0628=float(input("Please enter the traverse angle of first unkown point(grad):"))#I asked to users angle of point.I am going to use it to calculate azimuth.(from Lecture  Notes2.2 and Lecture Notes3.1)
i_0628=float(input("Please enter the traverse angle of second unknown point(grad):"))#I asked to users angle of point.I am going to use it to calculate azimuth.(from Lecture  Notes2.2 and Lecture Notes3.1)
j_0628=float(input("Please enter the distance between second known point and first unknown point(m):"))#I asked to users distance between to points.I am going to use it to calculate change of X and Y values.(from Lecture  Notes2.2 and Lecture Notes3.1)
k_0628=float(input("Please enter the distance between first unknown point and second unknown point(m):"))#I asked to users distance between to points.I am going to use it to calculate change of X and Y values.(from Lecture  Notes2.2 and Lecture Notes3.1)
l_0628=float(input("Please enter the distance between second unknown point and third unknown point(m):"))#I asked to users distance between to points.I am going to use it to calculate change of X and Y values.(from Lecture  Notes2.2 and Lecture Notes3.1)
m_0628=float(input("Please enter the X coordinates of first known point(m):"))#I asked to users coordinates of point.I am going to use it to calculate azimuth.(from Lecture  Notes2.2 and Lecture Notes3.1)
n_0628=float(input("Please enter the X coordinates of second known point(m):"))#I asked to users coordinates of point.I am going to use it to calculate azimuth and new value of X.(from Lecture  Notes2.2 and Lecture Notes3.1)
p_0628=float(input("Please enter the Y coordinates of first known point(m):"))#I asked to users coordinates of point.I am going to use it to calculate azimuth.(from Lecture  Notes2.2 and Lecture Notes3.1)
r_0628=float(input("Please enter the Y coordinates of second known point(m):"))#I asked to users coordinates of point.I am going to use it to calculate azimuth and new value of Y.(from Lecture  Notes2.2 and Lecture Notes3.1)
import math #I imported math library to use mathematic operations.(from Lecture Notes2.2)
tAB_0628=math.atan((abs(r_0628-p_0628)/abs(n_0628-m_0628))/(200/math.pi))#I calculated azimuth angle between A and B point(from Lecture Notes2.2). I did (200/math.pi) math operation because I have to calculate degree in grad.
#We need to know which quarter that azimuth angle is in because we will do math operation according to the quarter.
if r_0628-p_0628>0 and n_0628-m_0628>0: #I learn the quarter by checking whether it meets the condition.(from Lecture Notes6.1)
    print("The azimuth angle is in first quadrant. You can continue.")#I gave information to user.
elif r_0628-p_0628>0 and n_0628-m_0628<0: #I learn the quarter by checking whether it meets the condition.(from Lecture Notes6.1)
    print("The azimuth angle is in second quadrant.Necessary mathematical operations will be done.")#I gave the information to user.
    tAB_0628=200-tAB_0628 #The mathemathical operation of finding azimuth angle in second quadrant.
elif r_0628-p_0628<0 and n_0628-m_0628<0: #I learn the quarter by checking whether it meets the condition.(from Lecture Notes6.1)
    print("The azimuth angle is in third quadrant.Necessary mathematical operations will be done.")#I gave the information to user.
    tAB_0628=200+tAB_0628 #The mathemathical operation of finding azimuth angle in second quadrant.
elif r_0628-p_0628 <0 and n_0628-m_0628>0: #I learn the quarter by checking whether it meets the condition.(from Lecture Notes6.1)
    print("The azimuth angle is in fourth quadrant.Necesaary mathematical operations will be done.")#I gave the information to user.
    tAB_0628=400-tAB_0628 #The mathemathical operation of finding azimuth angle in fourth quadrant.
print("Azimuth angle of between A and B points is",format(tAB_0628,".4f"))#I printed to azimuth angle.I am going to use it to calculate other azimuth angle.
Z_0628=g_0628+tAB_0628 #I calculated to azimuth angle of first unknown point using first azimuth angle.
if Z_0628<200: #I check whether it meets the condition.(from Lecture Notes6.1)
    print("Azimuth angle of between B and 1 points is less than 200 grad.")#I gave the information to users.
    Z_0628=Z_0628+200
    print("The azimuth angle is",format(Z_0628,".4f"))#I printed to azimuth angle.I am going to use it to calculate other azimuth angle.
elif Z_0628>200 and Z_0628<600: #I check whether it meets the condition.(from Lecture Notes6.1)
    print("Azimuth angle of between B and 1 points is greater than 200 grad ans less than 600 grad.")#I gave the information to users.
    Z_0628=Z_0628-200
    print("The azimuth angle is",format(Z_0628,".4f"))#I printed to azimuth angle.I am going to use it to calculate other azimuth angle.
elif Z_0628>600: #I check whether it meets the condition.(from Lecture Notes6.1)
    print("Azimuth angle of between B and 1 points is greater than 600 grad.",format(Z_0628-600,".4f"))#I gave the information to users.
    Z_0628=Z_0628-600
    print("The azimuth angle is",format(Z_0628,".4f"))#I printed to azimuth angle.I am going to use it to calculate other azimuth angle.
Y_0628=Z_0628+h_0628 #I calculated to azimuth angle of second unknown point using second azimuth angle.
if Y_0628<200: #I check whether it meets the condition.(from Lecture Notes6.1)
    print("Azimuth angle of between 1 and 2 points is less than 200 grad.")
    Y_0628=Y_0628+200
    print("The azimuth angle is",format(Y_0628,".4f"))
elif Y_0628>200 and Y_0628<600: #I check whether it meets the condition.(from Lecture Notes6.1)
    print("Azimuth angle of between 1 and 2 points is greater than 200 grad and less than 600 grad.")
    Y_0628=Y_0628-200
    print("The azimuth angle is",format(Y_0628,".4f"))
elif Y_0628>600: #I check whether it meets the condition.(from Lecture Notes6.1)
    print("Azimuth angle of between 1 and 2 points is greater than 600 grad.")
    Y_0628=Y_0628-600
    print("Azimuth angle of between 1 and 2 points is",format(Y_0628,".4f"))
V_0628=Y_0628+i_0628 ##I calculated to azimuth angle of second unknown point using third azimuth angle.
if V_0628<200: #I check whether it meets the condition.(from Lecture Notes6.1)
    print("Azimuth angle of between 2 and 3 points is less than 200 grad.")
    V_0628=V_0628+200
    print("The azimuth angle is",format(V_0628,".4f"))
elif V_0628>200 and V_0628<600: #I check whether it meets the condition.(from Lecture Notes6.1)
    print("Azimuth angle of between 2 and 3 points is greater than 200 grad ans less than 600 grad.")
    V_0628=V_0628-200
    print("The azimuth angle is",format(V_0628,".4f"))
elif V_0628>600: #I check whether it meets the condition.(from Lecture Notes6.1)
    print("Azimuth angle of between 2 and 3 points is greater than 600 grad.")
    V_0628=V_0628-600
    print("The azimuth angle is",format(V_0628,".4f"))
"""I found the azimuth angles of unknown points. I'm going to use them to calculate the change of Y and X values."""
import math #I imported math library to use mathematic operations.(from Lecture Notes2.2)
DY1_0628=j_0628*math.sin(Z_0628/(200/math.pi))#Change of Y between second known point and first unknown point is the product of distance between second known point and first unknown point and sinus of  first unknown point's azimuth angle.
print("Change of first Y is",format(DY1_0628,".4f"))
DY2_0628=k_0628*math.sin(Y_0628/(200/math.pi))#Change of Y between first unknown point and second unknown point is the product of distance between first unknown point and second unknown point and sinus of  second unknown point's azimuth angle.
print("Change of second Y is",format(DY2_0628,".4f"))
DY3_0628=l_0628*math.sin(V_0628/(200/math.pi))#Change of Y between second unknown point and third unknown point is the product of distance between second unknown point and third unknown point and sinus of  third unknown point's azimuth angle.
print("Change of third Y is",format(DY3_0628,".4f"))
DX1_0628=j_0628*math.cos(Z_0628/(200/math.pi))#Change of X between second known point and first unknown point is the product of distance between second known point and first unknown point and sinus of  first unknown point's azimuth angle.
print("Change of first X is",format(DX1_0628,".4f"))
DX2_0628=k_0628*math.cos(Y_0628/(200/math.pi))#Change of X between first unknown point and second unknown point is the product of distance between first unknown point and second unknown point and sinus of  second unknown point's azimuth angle.
print("Change of second X is",format(DX2_0628,".4f"))
DX3_0628=l_0628*math.cos(V_0628/(200/math.pi))#Change of X between second known point and first unknown point is the product of distance between second known point and first unknown point and sinus of  first unknown point's azimuth angle.
print("Change of third X is",format(DX3_0628,".4f"))
"""I use these values calculating coordinates of Y and X"""
Y1_0628=DY1_0628+r_0628 #The Y value of first unknown point.
print("First Y value is",format(Y1_0628,".4f"))
Y2_0628=DY2_0628+r_0628 #The Y value of second unknown point.
print("Second Y value is",format(Y2_0628,".4f"))
Y3_0628=DY3_0628+r_0628 #The Y value of third unknown point.
print("Third Y value is",format(Y3_0628,".4f"))
X1_0628=DX1_0628+n_0628 #The X value of first unknown point.
print("First X value is",format(X1_0628,".4f"))
X2_0628=DX2_0628+n_0628 #The X value of second unknown point.
print("Second X value is",format(X2_0628,".4f"))
X3_0628=DX3_0628+n_0628 #The X value of third unknown point.
print("Third X value is",format(X3_0628,".4f"))
"""I'm going to create a chart using prettytable method."""
# from prettytable import  PrettyTable #I am going to use this creating first table

# t_0628=PrettyTable(['Point ID','Point ID','Azimuth','Delta Y','Delta X']) #I wrote the column heading.I'm going to add rows.

list = [
    
]