
# Usage: You can do "make output" and it checks whether or not main.c and include_example.h has changed. If yes it compiles 

.PHONY: output clear run clear_run

output: main.c include_example.h # Anytime main.c or include_example.h changes it does the following:
	gcc -o main main.c -pthread

clear:
	rm main

run:
	make output
	./main

clear_run:
	make output
	./main
	rm main
