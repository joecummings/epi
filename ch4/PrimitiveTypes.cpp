#include <iostream>
#include <string>

// Check each bit for a one until zero
int OneBitsInNum(int x){
	int numOnes = 0;
	const unsigned char mask = 1;
	while (x != 0) {
		if ((mask & x) == 1){
			numOnes++;
		}
		x = x >> 1;
	}
	return numOnes;
}

// Isolate lowest bit, remove it, repeat until zero
int OneBitsInNumFast(int x){
	int numOnes = 0;
	int y = x & ~(x - 1);
	while (y != 0){
		numOnes++;
		y = y ^ x;
	}
	return numOnes;
}

void OneBitsInNumTests(){
	// Test 1
	int result1 = OneBitsInNum(0);
	int result12 = OneBitsInNumFast(0);
	if (result1 != 0){ throw "OneBitsInNum Test 1 Failed"; }
	if (result12 != 0){ throw "OneBitsInNumFast Test 1 Failed"; }

	// Test 2
	int result2 = OneBitsInNum(2);
	int result22 = OneBitsInNumFast(2);
	if (result2 != 1) { throw "OneBitsInNum Test 2 Failed"; }
	if (result22 != 1) { throw "OneBitsInNumFast Test 2 Failed"; }

	// Test 3
	int result3 = OneBitsInNum(15);
	int result32 = OneBitsInNum(15);
	if (result3 != 4) { throw "OneBitsInNum Test 3 Failed"; }
	if (result32 != 4) {throw "OneBitsInNumFast Test 3 Failed"; }
}

int PropogateRightMostBit(int x){
	if (x == 0) return 0;
	return (x | (x - 1));
}

void PropogateRightMostBitTests(){
	// Test 1
	int result1 = PropogateRightMostBit(80);
	if (result1 != 95) { throw "PropogateRightMostBit Test 1 Failed"; }
	
	// Test 2
	int result2 = PropogateRightMostBit(0);
	if (result2 != 0) { throw "PropogateRightMostBit Test 2 Failed"; }
}

int Modulo(int x, int y){
	return 0;
}

void ModuloTests(){
	// Test 1
	int result1 = Modulo(1, 1);
	if (result1 != 0) { throw "Modulo Test 1 Failed"; }
	
	// Test 2
	int result2 = Modulo(77, 64);
	if (result2 != 13) { printf("\x1b[31m" "Modulo Test 2 Failed" "\n"); }
}

int main(){
	OneBitsInNumTests();
	PropogateRightMostBitTests();
	ModuloTests();

	return 1;
}
