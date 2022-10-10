import math
import random
import time

Grid_Size = [100, 100]
Location = [50, 50]
Movement_Angle = 135
Y_Bound = [0, 100]
X_Bound = [0, 100] 

Travel_Variation_Angle = 45
Half_Travel_Variation = round(Travel_Variation_Angle/2, 2)
Travel_Distance = 10

random.seed(a=None, version = 2)

def triangle_Calc(angle, trav_dist):
	angle_in_rad = round(math.radians(angle), 2)
	y_adj = round(trav_dist*math.sin(angle_in_rad), 2)
	x_adj = round(trav_dist*math.cos(angle_in_rad), 2)
	return y_adj, x_adj
	

while(True):
	Angle_Adjust_Percentage = round((random.random()), 2)
	Left_or_Right = random.randint(1, 2) #1 for left, 2 for right


	if Left_or_Right == 1:
		Movement_Angle += round((Half_Travel_Variation*Angle_Adjust_Percentage), 2)
	else:
		Movement_Angle += round((Half_Travel_Variation*Angle_Adjust_Percentage)*(-1), 2)
	Movement_Angle = round(Movement_Angle, 2)
	
	
	if Movement_Angle >= 360:
		Movement_Angle = Movement_Angle%360
	elif Movement_Angle < 0:
		Movement_Angle = 360+Movement_Angle

	
	if Movement_Angle > 270:
		Calc_Angle = round((Movement_Angle-360)*(-1), 2)
		y_adjust, x_adjust = triangle_Calc(Calc_Angle, Travel_Distance)
		y_adjust *= -1
	elif Movement_Angle > 180:
		Calc_Angle = round((Movement_Angle-180), 2)
		y_adjust, x_adjust = triangle_Calc(Calc_Angle, Travel_Distance)
		y_adjust *= -1
		x_adjust *= -1
	elif Movement_Angle > 90:
		Calc_Angle = round((180-Movement_Angle), 2)
		y_adjust, x_adjust = triangle_Calc(Calc_Angle, Travel_Distance)
		x_adjust *= -1
	else:
		Calc_Angle = Movement_Angle
		y_adjust, x_adjust = triangle_Calc(Calc_Angle, Travel_Distance)
		

	Location[0] = round(Location[0] + x_adjust, 2)
	Location[1] = round(Location[1] + y_adjust, 2)

	print(Movement_Angle, Location[0], Location[1])

	time.sleep(1)