from random import shuffle, randrange, randint
from info import *

def make_maze(h = 16, w = 16):
    vis = [[0] * h + [1] for _ in range(w)] + [[1] * (h + 1)]
#    print "viz"
#    for i in vis:
#        print i
    ver = [["|  "] * h + ['|'] for _ in range(w )] + [[]]
#    print "ver"
#    for j in ver:
#        print j
    hor = [["+--"] * h + ['+'] for _ in range(w + 1)]
#    print "hor"
#    for k in hor:
#        print k

        
        
    def walk(x, y):
        vis[y][x] = 1
        
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)


    As = []
    Bs = []
    walk(randrange( h ), randrange( w ))
    for (a, b) in zip(hor, ver):
        As.append(a)
        Bs.append(b)
#        hold = ''.join(a + ['\n'] + b)
#        print hold


    a = As
    b = Bs
    bool_maze = []
    #convert array of strings to bools
    #new arr will be nearly twice as large
    for j in range(len(a)):
        a_line = a[j]
        b_line = b[j]
        hold_a = []
        hold_b = []
        for i in range(len(a_line)):
            if a_line[i] == '+--':
                #two walls
                hold_a.extend([True, True])
            elif a_line[i] == '+  ':
                #one wall, then blank
                hold_a.extend([True, False])
            elif a_line[i] == '+':
                hold_a.extend([True])
            
        bool_maze.append(hold_a)
            
        for i in range(len(b_line)):
            if b_line[i] == '|  ':
                hold_b.extend([True, False])
            elif b_line[i] == '   ':
                hold_b.extend([False, False])
            elif b_line[i] == '|':
                hold_b.extend([True])
                
        bool_maze.append(hold_b)

    #ensure there is an entrance
    bool_maze[0][1] = False

    print "len(bool_maze) is {}".format(len(bool_maze) )


    #chose an exit
    #TRUE MEANS THERE IS A BLOCK
    #actual width  is equal to len(bool_maze) - 2
    #actual height is equal to len(bool_maze[0]) - 1
    #pick a random height value until it works
    x = len(bool_maze) - 3
    valid = False
    while not valid:
        y = randint(1, len(bool_maze[0]) - 1)
        if not bool_maze[x][y]:
            #found an empty spot
            #open the maze wall right next to it
            bool_maze[x + 1][y] = False
            valid = True


    
    winning_pos = [len(bool_maze) - 1, y]
    print "winning pos is [{0}, {1}]".format(winning_pos[0], winning_pos[1])
    return bool_maze

#key - True means make a block, False means don't make a block
#'+--' -> True,  True
#'|  ' -> True,  False
#'+  ' -> True,  False
#'   ' -> False, False
#'+'   -> True
#'|'   -> True

