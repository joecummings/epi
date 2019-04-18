#include <iostream>

int OneBitsInNum(int x){
	int numOnes = 0;
	unsigned char mask = 1;
	while (x != 0) {
		if (mask |= x == 1){
			numOnes++;
		}
	}
	return numOnes;
}

int main(){
	return 1;
}
