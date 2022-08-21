#!/bin/python3

# exercise 11 from chapter 4 of "Python Programming" by John Zelle

# this program allows the user to draw a house in 5 clicks using the graphics.py module

import graphics
from graphics import *

def clickhouse():
    win = GraphWin("Draw a House")
    # construct house frame by getting lower left and upper right corners
    ll_frame = win.getMouse()
    ur_frame = win.getMouse()
    house_frame = Rectangle(ll_frame, ur_frame)
    # draw house frame
    house_frame.draw(win)
    # construct door proportional to the house
    # get house width
    house_width = ur_frame.getX() - ll_frame.getX()
    door_center = win.getMouse()
    door_width = house_width / 5
    # divide door width in 2 to help determine x-coords for lower left and upper right corners
    # create upper right corner
    half_dwidth = door_width / 2
    ur_xcoord = door_center.getX() + half_dwidth
    ur_ycoord = door_center.getY()
    ur_door = Point(ur_xcoord, ur_ycoord)
    # create lower left corner
    ll_xcoord = door_center.getX() - half_dwidth
    ll_ycoord = ll_frame.getY()
    ll_door = Point(ll_xcoord, ll_ycoord)
    # draw door
    door = Rectangle(ll_door, ur_door)
    door.draw(win)
    # calculate width of window relative to door
    win_width = door_width / 2
    # get center of window
    win_center = win.getMouse()
    # get half of win_width to calculate distance from center
    half_wwidth = win_width / 2
    # calculate upper right corner of window
    ur_win = Point((win_center.getX() + half_wwidth), (win_center.getY() + half_wwidth))
    ll_win = Point((win_center.getX() - half_wwidth), (win_center.getY() - half_wwidth))
    window = Rectangle(ll_win, ur_win)
    window.draw(win)
    # get peak of roof
    peak = win.getMouse()
    # draw right side of roof
    rroof = Line(peak, ur_frame)
    # calculate upper left corner of house frame
    ul_frame = Point(ll_frame.getX(), ur_frame.getY())
    # draw left side of roof
    lroof = Line(peak, ul_frame)
    # draw in window
    rroof.draw(win)
    lroof.draw(win)


    # prevent sudden closure of graphics window 
    win.getMouse()

if __name__ == "__main__":
    clickhouse()

