MPICC=mpiicc

OBJ=main.o

TARGET=aproc
$(OBJ)	:
	$(MPICC) -O3 -o main.c

$(TARGET): $(OBJ)
	$(MPICC) -o $(TARGET) $(OBJ)
clean:
	rm -rf $(TARGET) $(OBJ)
