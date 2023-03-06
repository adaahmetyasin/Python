print("This program computes coordinates in open traverse series.")#I told what program does(from Lecture Notes 
#An open traverse is a polygon that begins at a point with known coordinates and finishes at a position with unknown coordinates.
a_0628=str(input("Please enter the point ID of first known point:"))
b_0628=str(input("Please enter the point ID of second known point:"))
c_0628=int(input("Please enter the number of unknown traverse point:"))
d_0628=str(input("Please enter the point ID of first unknown point:"))
e_0628=str(input("Please enter the point ID of second unknown point:"))
f_0628=str(input("Please enter the point ID of third unknown point:"))
g_0628=float(input("Please enter the traverse angle of second known point(grad):"))
h_0628=float(input("Please enter the traverse angle of first unknown point(grad):"))
i_0628=float(input("Please enter the traverse angle of second unknown point(grad):"))
j_0628=float(input("Please enter the horizontal distance between second known point and first unknown point(m):"))
k_0628=float(input("Please enter the horizontal distance between first unknown point and second unknown point(m):"))
l_0628=float(input("Please enter the horizontal distance between second unknown point and third unknown point(m):"))
m_0628=float(input("Please enter the X coordinates of first known point(m):"))
n_0628=float(input("Please enter the X coordinates of second known point(m):"))
p_0628=float(input("Please enter the Y coordinates of first known point(m):"))
r_0628=float(input("Please enter the Y coordinates of second known point(m):"))
#I asked to users information(from Lecture  Notes2.2 and Lecture Notes3.1)
import math #from Lecture Notes2.2
tAB_0628=math.atan(((r_0628-p_0628)/(n_0628-m_0628))/(200/math.pi))#I calculated azimuth angle between A and B point(from Lecture Notes2.2).
#we need to know which quarter that azimuth angle is in.
if (r_0628-p_0628)>0 and (n_0628-m_0628)>0:
    print("The azimuth angle is in first quadrant. You can continue.")#I gave information to user.
elif (r_0628-p_0628)>0 and (n_0628-m_0628)<0:
    print("The azimuth angle is in second quadrant.Necessary mathematical operations will be done.")#I gave the information to user.
    tAB_0628=200-tAB_0628 #The mathemathical operation of finding azimuth angle in second quadrant.
elif (r_0628-p_0628)<0 and (n_0628-m_0628)<0:
    print("The azimuth angle is in third quadrant.Necessary mathematical operations will be done.")#I gave the information to user.
    tAB=200+tAB_0628 #The mathemathical operation of finding azimuth angle in second quadrant.
elif (r_0628-p_0628)<0 and (n_0628-m_0628)>0:
    print("The azimuth angle is in fourth quadrant.Necesaary mathematical operations will be done.")#I gave the information to user.
    tAB=200+tAB_0628 #The mathemathical operation of finding azimuth angle in second quadrant.