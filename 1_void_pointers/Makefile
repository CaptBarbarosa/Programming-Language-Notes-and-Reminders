
compile_jacob: jacob_sorber_youtube_example.c
	gcc -o jacob_sorber_youtube_example jacob_sorber_youtube_example.c

run_jacob:
	./jacob_sorber_youtube_example

full_on_jacob_sorber:
	make compile_jacob
	make run_jacob

clean_run_jacob:
	make compile_jacob
	make run_jacob
	rm jacob_sorber_youtube_example

compile_example_1: void_pointer.c
	gcc -o void_pointer void_pointer.c

run_example_1:
	./void_pointer

full_on_example_1:
	make compile_example_1
	make run_example_1

clean_run_example_1:
	make compile_example_1
	make run_example_1
	rm void_pointer

clean_all_exe:
	rm void_pointer jacob_sorber_youtube_example
