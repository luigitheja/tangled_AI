from graphics import *
import random

number_of_points = 7

win = GraphWin(width = 600, height = 600) # create a window
win.setCoords(-500, -500, 500, 500) # set the coordinates of the window; bottom left is (-500, -500) and top right is (500, 500)

#draw the coordiante axes
line = Line(Point(-500,0), Point(500, 0))
line.draw(win)
line = Line(Point(0,-500), Point(0, 500))
line.draw(win)

#to check whether the total number of lines intersecting in the graph
def find_intersection_score(pointlist, linept_list,win):
    print(linept_list)
    intersection_score = 0
    for ln in linept_list:
        never_intersect = True
        for ln1 in linept_list:
            x1= ln[0]
            y1=ln[1]
            x2=ln[2]
            y2=ln[3]
            x3=ln1[0]
            y3=ln1[1]
            x4=ln1[2]
            y4=ln1[3]
            if (ln!= ln1) and  is_intersecting(x1,y1,x2,y2,x3,y3,x4,y4):
                print(ln,ln1)
                intersection_score +=1
                never_intersect = False
        if never_intersect:
            ln = Line(Point(x1,y1),Point(x2,y2))
            ln.setFill('green')
            ln.setWidth(3)
            ln.draw(win)
    return int(intersection_score/2)

#the below two functions are used to check whether two given line segments intersect
def ccw(x1,y1, x2,y2, x3,y3):
    return (y3 - y1) * (x2 - x1) > (y2 - y1) * (x3 - x1)
def is_intersecting(x1,y1,x2,y2,x3,y3,x4,y4):
    # Return true if line segments AB and CD intersect
    if (x1 == x3 and y1 == y3) or (x1 == x4 and y1 == y4) or (x2 == x3 and y2 == y3) or (x2 == x4 and y2 == y4):
        return False
    return ccw(x1,y1, x3,y3, x4,y4) != ccw(x2,y2, x3,y3, x4,y4) and ccw(x1,y1, x2,y2, x3,y3) != ccw(x1,y1, x2,y2, x4,y4)



#select number of given random points within coordinate range and add them to list and draw them as red circles
pointlist = []
for i in range(number_of_points):
    x = random.randint(-200,200)
    y= random.randint(-200,200)
    pt = Point(x, y)
    if pt not in pointlist:
        pointlist.append(pt)
        cir = Circle(pt, 3)
        cir.setFill('red')
        cir.draw(win)

#draw lines between randomly selected points
linelist =[]
linepoint_list = []
for pt in pointlist:
    for pt2 in pointlist:
        linepoints = [pt.x,pt.y,pt2.x,pt2.y]
        #line is drawn only if the random number selected between 1 to 200 is divisible by 4 (to decrease the probability change 4 to any less divisible number)
        if (random.randint(1,200)%4 == 0) and (pt != pt2)  and linepoints not in linepoint_list :
            line = Line(pt,pt2)
            line.draw(win)
            linepoint_list.append([pt.x,pt.y,pt2.x,pt2.y])

#get and print intersection score
i_score = find_intersection_score(pointlist,linepoint_list,win)
print(i_score)
message = Text(Point(-400, -400), str(i_score))
message.draw(win)

#will show you mouse pointer but have to close manually 
win.getMouse() # pause before closing
