MKL_FLAGS=-I/s/parsons/l/sys/intel/mkl/include/ -L/s/parsons/l/sys/intel/compilers_and_libraries_2018.0.128/linux/mkl/lib/intel64  -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core  -L/s/parsons/l/sys/intel/lib/intel64 -liomp5 -lm

SIZE=10
N=5000
CC=gcc

D%:TMM-wrapper.c TMM.c blockformat.c blockmult.c
	$(CC) $^ -o $@ -O3 $(MKL_FLAGS) -DSIZE=$(SIZE) $(EXTRA_FLAGS)

check: TMM-wrapper.c TMM.o blockformat.o blockmult.c
	$(CC) $^ -o TMM.check -O3 $(MKL_FLAGS) -DCHECKING -DSIZE=$(SIZE)

correctness: clean
	g++ blockformat.c -c  -DSIZE=$(SIZE) -O3 -o blockformat.o -Wfatal-errors
	g++ TMM.c -o TMM.o -O3 $(MKL_FLAGS) -DSIZE=$(SIZE) -c
	g++ testStuff.cpp -o TMM.check TMM.o blockformat.o $(MKL_FLAGS) -DCHECKING
TMM.o:TMM.c
	$(CC) $^ -o $@ -O3 $(MKL_FLAGS) -DSIZE=$(SIZE) $(EXTRA_FLAGS) -c


runTMM:  D$(SIZE) 
	$$(./mkl_setup.sh) ; \
	./$< $(N) $(N) $(N) $(N)


runcheck: check
	$$(./mkl_setup.sh) ; \
	./TMM.check 4 4 4 4

testBlockFormat:testBlockFormat.c blockformat.o
	$(CC) $^  -o $@ -DTEST_SIZE=31

blockformat.o: blockformat.c
	$(CC) $< -c  -DSIZE=$(SIZE) -O3 -o $@ -Wfatal-errors

blockmult.o: blockmult.c
	$(CC) $< -c -DSIZE=$(SIZE) -O3 -o $@ -Wfatal-errors
clean:
	rm -f ./*.o TMM D*
