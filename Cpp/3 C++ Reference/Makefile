CXX = g++
CXXFLAGS = -Wall -Wextra -O2
TARGETS = 0_easy_example.exe 1_different_functions.exe
SRCS = 0_easy_example.cpp 1_different_functions.cpp
all: $(TARGETS)


0_easy_example.exe: 0_easy_example.cpp
	$(CXX) $(CXXFLAGS) -o 0_easy_example.exe 0_easy_example.cpp


1_different_functions.exe: 1_different_functions.cpp
	$(CXX) $(CXXFLAGS) -o 1_different_functions.exe 1_different_functions.cpp


0: 0_easy_example.exe
	./0_easy_example.exe


1: 1_different_functions.exe
	./1_different_functions.exe


clean_all:
	rm -f $(TARGETS)
.PHONY: all 0 1 clean_all

