CC = gcc #permet de creer une variable de type string pour recuperer l asyntaxe gcc m'evitant ainsi de faire appelle de gcc a chaque fois
CFLAGS= -std=c11 -Wall -Wextra -Wpedantic -g -fsanitize=address -fno-omit-frame-pointer -Iinclude	

all:bin/bank-queue-cli ##avant d'executer le all (la premiere condition verifier par le code il faut que banl-queue-cli existe)

bin/bank-queue-cli: src/main.c
	mkdir -p bin
	$(CC) $(CFLAGS) src/main.c -o bin/bank-queue-cli

clean:
	rm -rf bin build 

.PHONY: all clean