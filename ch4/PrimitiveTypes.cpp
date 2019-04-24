#include <iostream>

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

void OneBitsInNumTests(){
	// Test 1
	int result1 = OneBitsInNum(0);
	if (result1 != 0){ printf("\x1b[31m" "OneBitsInNum Test 1 Failed" "\n"); }

	// Test 2
	int result2 = OneBitsInNum(2);
	if (result2 != 1) { printf("\x1b[31m" "OneBitsInNum Test 2 Failed" "\n"); }

	// Test 3
	int result3 = OneBitsInNum(15);
	if (result3 != 4) { printf("\x1b[31m" "OneBitsInNum Test 3 Failed" "\n"); }
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

void OneBitsInNumFastTests(){
	// Test 1
	int result1 = OneBitsInNumFast(0);
	if (result1 != 0){ printf("\x1b[31m" "OneBitsInNumFast Test 1 Failed" "\n"); }

	// Test 2
	int result2 = OneBitsInNumFast(2);
	if (result2 != 1) { printf("\x1b[31m" "OneBitsInNumFast Test 2 Failed" "\n"); }

	// Test 3
	int result3 = OneBitsInNum(15);
	if (result3 != 4) { printf("\x1b[31m" "OneBitsInNumFast Test 3 Failed" "\n"); }
}

int PropogateRightMostBit(int x){
	if (x == 0) return 0;
	return (x | (x - 1));
}

void PropogateRightMostBitTests(){
	// Test 1
	int result1 = PropogateRightMostBit(80);
	if (result1 != 95) { printf("\x1b[31m" "PropogateRightMostBit Test 1 Failed" "\n"); }
	
	// Test 2
	int result2 = PropogateRightMostBit(0);
	if (result2 != 0) { printf("\x1b[31m" "PropogateRightMostBit Test 2 Failed" "\n"); }
}

int Modulo(int x, int y){
	if (x < y){
		return x;
	}
	int z = Modulo(x, y << 1);
	if (z >= y){
		z -= y;
	}
	return z;
}

void ModuloTests(){
	// Test 1
	int result1 = Modulo(3, 3);
	if (result1 != 0) { printf("\x1b[31m" "Modulo Test 1 Failed" "\n"); }
	
	// Test 2
	int result2 = Modulo(77, 64);
	if (result2 != 13) { printf("\x1b[31m" "Modulo Test 2 Failed" "\n"); }

	// Test 3
	int result3 = Modulo(10, 3);
	if (result3 != 1) { printf("\x1b[31m" "Modulo Test 3 Failed" "\n"); }
}

bool PowerOfTwoHa(int x) {
	if (Modulo(x, 2) == 0) return true;
	return false;
}

void PowerOfTwoHaTests(){
	// Test 1
	bool result = PowerOfTwoHa(4);
	if (!result) { printf("\x1b[31m" "PowerOfTwoHa Test 1 Failed" "\n"); }

	// Test 2
	bool result2 = PowerOfTwoHa(5);
	if (result2) { printf("\x1b[31m" "PowerOfTwoHa Test 2 Failed" "\n"); }
}

int main(){
	OneBitsInNumTests();
	OneBitsInNumFastTests();
	PropogateRightMostBitTests();
	ModuloTests();
	PowerOfTwoHaTests();

	return 1;
}
