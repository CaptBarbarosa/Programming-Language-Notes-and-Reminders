CXX = g++
CXXFLAGS = -Wall -Wextra -O2
TARGET = 1st_example.exe
SRC = 1st_example.cpp


all: $(TARGET)


$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)


1: $(TARGET)
	./$(TARGET)


clean_all:
	rm -f $(TARGET)
.PHONY: all 1 clean_all

