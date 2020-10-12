MPICC=mpiicc

OBJ=main.o

TARGET=aproc

$(TARGET): $(OBJ)
	$(MPICC) -o $(TARGET) $(OBJ)

$(OBJ)	: main.c
	$(MPICC) -O3 -c -o $(OBJ) main.c

clean:
	rm -rf $(TARGET) $(OBJ)
