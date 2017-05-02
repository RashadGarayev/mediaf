import os
def version():
	print "_Version_1"
def about():
	print"""
	Usage --------------------------------------
	First install sudo apt-get ffmpeg
	--------------------------------------------
	>>import mediaf
	>>from mediaf import*
	>>mediaf.version()
	_Version_1
	>>mediaf.play("input.mp4")
	"""
def play(infile):
	try:
		os.system("ffplay '{}'".format(str(infile)))
	except SyntaxError:
		print "invalid systax\n {}".format(infile)
		print "Use file in string arg exam : mediaf.play('/home/user/input.mp4')"

