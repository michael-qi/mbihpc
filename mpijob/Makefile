MPICC=mpiicc

OBJ=main.o

TARGET=aproc
$(OBJ)	:
	$(MPICC) -O3 -c -o $(OBJ) main.c

$(TARGET): $(OBJ)
	$(MPICC) -o $(TARGET) $(OBJ)
clean:
	rm -rf $(TARGET) $(OBJ)
