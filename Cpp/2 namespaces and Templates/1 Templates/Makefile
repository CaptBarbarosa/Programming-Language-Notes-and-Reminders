CXX = g++
CXXFLAGS = -Wall -Wextra -O2
TARGET1 = 1st_example.exe
TARGET2 = 2_class_Example.exe
SRC1 = 1st_example.cpp
SRC2 = 2_class_Example.cpp

all: $(TARGET1) $(TARGET2)

$(TARGET1): $(SRC1)
	$(CXX) $(CXXFLAGS) -o $(TARGET1) $(SRC1)

$(TARGET2): $(SRC2)
	$(CXX) $(CXXFLAGS) -o $(TARGET2) $(SRC2)

1: $(TARGET1)
	./$(TARGET1)

2: $(TARGET2)
	./$(TARGET2)

clean_all:
	rm -f $(TARGET1) $(TARGET2)
.PHONY: all 1 2 clean_all

