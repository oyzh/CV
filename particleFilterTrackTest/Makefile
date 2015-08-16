INCL	=`pkg-config --cflags opencv`
LIBS	=-lm `pkg-config --libs opencv` -lgsl -lgslcblas

all: track

track: track.c particles.o observation.o utils.o
	gcc $(INCL) track.c particles.o observation.o utils.o -o track $(LIBS)

particles.o:particles.c particles.h
	gcc $(INCL) -c particles.c -o particles.o

observation.o:observation.c observation.h
	gcc $(INCL) -c observation.c -o observation.o

utils.o:utils.c utils.h
	gcc $(INCL) -c utils.c -o utils.o	

clean:
	rm -f *~ *.o track
