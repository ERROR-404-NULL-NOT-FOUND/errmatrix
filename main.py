from random import randint
from time import sleep
import os
height,width=os.popen('stty size', 'r').read().split()
height=int(height)
width=int(width)
trail_len=20
chars='ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ12345678901234567890-=*_+|:<>"-=*_+|:<>"-=*_+|:<>"-=*_+|:<>'
nodes={
	0:{
		'y':0,
		'x':randint(0,width),
	}
}
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
def char(x:int,y:int):
	for i in range(len(nodes)):
		if nodes[i]['y']==y and nodes[i]['x']==x:
			return "\u001b[37m"+chars[overflow(x*y)]
		elif nodes[i]['y']>y and y>nodes[i]['y']-trail_len and nodes[i]['x']==x:
			return "\u001b[32m"+chars[overflow(x*y)]
	return ' '
def draw():
	output=''
	for y in range(height):
		for x in range(width):
			output+=char(x,y)
		output+="\n"
	os.system('clear')
	print(output)
def refresh():
	height,width=os.popen('stty size', 'r').read().split()
	height=int(height)
	width=int(width)
def main():
	while 1:
		refresh()
		draw()
		randomize()
		sleep(0.05)
main()
