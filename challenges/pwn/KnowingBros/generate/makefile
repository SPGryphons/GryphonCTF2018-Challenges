NAME = knowingbros
CC = gcc
CFLAGS = -m32

all:
	$(CC) ${NAME}.c $(CFLAGS) -o ../service/${NAME}
	cp ../service/$(NAME) ../distrib/
	cp $(NAME).c ../distrib/$(NAME).c
clean:
	rm -f ../service/${NAME}
	rm -f ../distrib/${NAME}
	rm -f ../distrib/$(NAME).c
