FILENAME='sample'
SOURCE='sample.cpp'
create:
	g++ -O0 -Wall -pedantic -I./ -I./include -I/usr/X11R6/include -o bin/$(FILENAME) $(SOURCE)  -L./lib -lglui -L/usr/X11R6/lib -lglut -lGLU -lGL -lXmu -lXext -lX11 -lXi -lm
debug:
	g++ -O0 -Wall -g -pedantic -I./ -I./include -I/usr/X11R6/include -o bin/$(FILENAME.debug) $(SOURCE)  -L./lib -lglui -L/usr/X11R6/lib -lglut -lGLU -lGL -lXmu -lXext -lX11 -lXi -lm
default:	
	rm bin/sample
