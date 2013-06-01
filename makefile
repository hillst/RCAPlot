FILENAME='PCAPlot'
SOURCE='src/PCAPlot.cpp'
all:
	g++ -O0 -Wall -pedantic -I./ -I./include -I/usr/X11R6/include -o bin/$(FILENAME) $(SOURCE)  -L./lib -lglui -L/usr/X11R6/lib -lglut -lGLU -lGL -lXmu -lXext -lX11 -lXi -lm
debug:
	g++ -O0 -Wall -g -pedantic -I./ -I./include -I/usr/X11R6/include -o bin/$(FILENAME.debug) $(SOURCE)  -L./lib -lglui -L/usr/X11R6/lib -lglut -lGLU -lGL -lXmu -lXext -lX11 -lXi -lm
clean:	
	rm bin/$(FILENAME) bin/$(FILENAME)
