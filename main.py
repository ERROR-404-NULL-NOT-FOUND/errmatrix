"""

Made by ERROR 404: NULL NOT FOUND
Please do not use my code without permission
This program includes the GPL licence
Github: https://github.com/ERROR-404-NULL-NOT-FOUND/errmatrix

"""

import curses
from random import randint
from time import sleep
import sys
#If on linux, get terminal size. Else, set the width & height to 10 
global height,width
height=10
width=10
chars='ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ12345678901234567890-=*_+|:<>"-=*_+|:<>"-=*_+|:<>"-=*_+|:<>'
global speed
global trail_len
trail_len=20
speed = 96
global color
global col_num
char_set = { #Credit: unimatrix for the character set

    'a': 'qwertyuiopasdfghjklzxcvbnm',
    'A': 'QWERTYUIOPASDFGHJKLZXCVBNM',
    'c': 'абвгдежзиклмнопрстуфхцчшщъыьэюя',
    'C': 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
    'e': '☺☻✌♡♥❤⚘❀❃❁✼☀✌♫♪☃❄❅❆☕☂★',
    'g': 'αβγδεζηθικλμνξοπρστυφχψως',
    'G': 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ',
    'k': 'ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ',
    'm': 'ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ1234567890'
         '1234567890-=*_+|:<>"-=*_+|:<>"-=*_+|:<>"-=*_+|:<>"',
    'n': '1234567890',
    'o': 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
         '`-=~!@#$%^&*()_+[]{}|\;\':",./<>?"',
    'p': '',
    'P': '',
    'r': 'mcclllxxxxvvvvviiiiii',
    'R': 'MCCLLLXXXXVVVVVIIIIII',
    's': '-=*_+|:<>"',
    'S': '`-=~!@#$%^&*()_+[]{}|\;\':",./<>?"',}

nodes={
	0:{
		'y':0,
		'x':randint(0,width),
	}
}

def init():
	global color
	curses.init_pair(1,curses.COLOR_BLACK,-1)
	curses.init_pair(2,curses.COLOR_BLUE,-1)
	curses.init_pair(3,curses.COLOR_CYAN,-1)
	curses.init_pair(4,curses.COLOR_MAGENTA,-1)
	curses.init_pair(5,curses.COLOR_RED,-1)
	curses.init_pair(6,curses.COLOR_WHITE,-1)
	curses.init_pair(7,curses.COLOR_GREEN,-1)
	curses.init_pair(8,curses.COLOR_YELLOW,-1)
	color=curses.color_pair(7)

def arg_handler():
	args=sys.argv
	global chars
	global speed
	global trail_len
	global col_num
	col_num=7
	for i in range(len(args)):
		if args[i] == '-l':
			chars=char_set[args[i+1]]
			i+=1
			pass
		elif args[i] == '-s':
			speed=int(args[i+1])
			i+=1
			pass
		elif args[i]=='-t':
			trail_len=int(args[i+1])
			i+=1
			pass
		elif args[i]=='-c':
			if args[i+1] == 'green':
				col_num=7
			elif args[i+1] == 'yellow':
				col_num=8
			elif args[i+1] == 'red':
				col_num=5
			elif args[i+1] == 'magenta':
				col_num=4
			elif args[i+1] == 'cyan':
				col_num=3
			elif args[i+1] == 'blue':
				col_num=2
			elif args[i+1] == 'white':
				col_num=6
			elif args[i+1] == 'black':
				col_num=1
		elif args[i]=='-h':
			print('''
			Usage
				errmatrix [-c character set] [-s speed] [-t trail length]
			Optional arguments
				
				-l CHARCTER_LIST Select the character list to use. Default=m

				-s SPEED  Integer up to 100. 0 uses a one-second delay before
                       refreshing, 100 uses none. Use negative numbers for
                       even lower speeds. Default=96
				
				-t TRAIL_LEN Integer with no maximum value. Determines the length of node trails in characters.

			Character list: (Credit: unimatrix)
				
				a   Lowercase alphabet
				A   Uppercase alphabet
				c   Lowercase Russian Cyrillic alphabet
				C   Uppercase Russian Cyrillic alphabet
				e   A few common emoji ( ☺☻✌♡♥❤⚘❀❃❁✼☀✌♫♪☃❄❅❆☕☂★ )
				g   Lowercase Greek alphabet
				G   Uppercase Greek alphabet
				k   Japanese katakana (half-width)
				m   Default 'Matrix' set, equal to 'knnssss'
				n   Numbers 0-9
				o   'Old' style non-unicode set, like cmatrix. Equal to 'AaSn'
				p   Klingon pIqaD (requires 'Horta' family font)*
				P   Klingon pIqaD (requires 'Klingon-pIqaD' or 'Code2000' family font)*
				r   Lowercase Roman numerals ( mcclllxxxxvvvvviiiiii )
				R   Uppercase Roman numerals ( MCCLLLXXXXVVVVVIIIIII )
				s   A subset of symbols actually used in the Matrix films ( -=*_+|:<>" )
				S   All common keyboard symbols ( `-=~!z#$%^&*()_+[]{}|\;':",./<>?" )
				u   Custom characters selected using -u switch
			''')
			exit()

def clear_nodes():
	for i in range(len(nodes)):
		if nodes[i]['y']>height+trail_len:
			return i
	return(len(nodes))

def randomize():
	for i in range(len(nodes)):
		nodes[i]['y']=nodes[i]['y']+1
	nodes[clear_nodes()]={
		'y':0,
		'x':randint(0,width),
	}

def overflow(i):
	while i>=len(chars):
		i-=len(chars)
	return i

def char_num(char):
	for i in range(len(chars)):
		if chars[i]==char:
			return i

def char(x:int,y:int,stdscr):
	for i in range(len(nodes)):
		if nodes[i]['y']==y and nodes[i]['x']==x:
			stdscr.insstr(y,x,chars[overflow(x*y)],curses.color_pair(6))
			return 0
		elif nodes[i]['y']>y and y>nodes[i]['y']-trail_len and nodes[i]['x']==x:
			stdscr.insstr(y,x,chars[overflow((x+y)*(x+y))],color)
			return 0
	stdscr.insch(y,x,' ')
	

def draw(stdscr):
	for y in range(height):
		for x in range(width):
			char(x,y,stdscr)
	stdscr.refresh()
	sleep(1-float("0."+str(speed)))

def main(stdscr):
	global height,width
	global col_num
	global color
	curses.start_color()
	height,width=stdscr.getmaxyx()
	curses.curs_set(0)
	curses.use_default_colors()
	init()
	color=curses.color_pair(col_num)
	while 1:
		randomize()
		draw(stdscr)
		#print(draw())

#if __name__=="__main__":
arg_handler()
curses.wrapper(main)
