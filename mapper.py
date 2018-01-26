#!/usr/bin/python
import curses
import sys
from time import sleep

log = open('log', 'w')

try:

    def mapper(screen):


        # cell types
        unknown = 0
        empty = 1
        block = 2
        # cell characters
        colors = ('?', ' ', 'X')

        if curses.has_colors() and curses.can_change_color():
            log.write('Colors Initialized!')
            curses.init_color(0,0,300,500)
            # color codes
            colors = (2, 8, 9)

        # cm
        map_size = 1000
        car_len = 5
        car_width = 7

        area_map = list()
        for x in xrange(map_size):
            area_map.append(list())
            for y in xrange(map_size):
                area_map[x].append(colors[unknown])

        screen_size = screen.getmaxyx()
        screen_size = (screen_size[0] - 2, screen_size[1] - 2)

        map_center = (map_size / 2, map_size / 2)
        start_location = map_center
        location = start_location

        def make_box(loc, h, w, color=colors[block]):
            # setup test objects
            for x in xrange(w):
                for y in xrange(h):
                    area_map[loc[0] + x][loc[1] + y] = color

        make_box((map_center[0] + 10, map_center[1] + 10), 5, 5)
        make_box((map_center[0] - 20, map_center[1] - 20), 10, 20)

        # draw car
        make_box((map_center[0] - car_len / 2, map_center[1] - car_width / 2), car_len, car_width, 'B')

        while True:
            # draw map
            dx = 0
            log.write('screen_size1 / -2' + str(screen_size[1] / -2) + '\n')
            for x in xrange(screen_size[1] / -2, screen_size[1] / 2):
                dy = 0
                for y in xrange(screen_size[0] / -2, screen_size[0] / 2):
                    dy += 1
                    log.write('screen_size ' + str(screen_size) + '\n')
                    log.write('dy,dx ' + str(dy) + ',' + str(dx) + '\n')

                    log.write('loc0 + x,loc1 + y ' + str(location[0] + x) + ',' + str(location[1] + y) + '\n')
                    log.write('map[loc0+x,loc1+y] ' + str(area_map[ location[0] + x ][location[1] + y]) + '\n\n')

                    screen.addch(dy, dx, area_map[ location[0] + x ][ location[1] + y ])
                dx += 1

            screen.refresh()
            sleep(1)



    curses.wrapper(mapper)
finally:
    log.close()
