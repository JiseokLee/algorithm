#include <stdio.h>

int main(void) {
	int num1, num2;
	scanf("%d %d", &num1, &num2);
	
	if(num1 % 2 == 0) {
		if(num2 % 2 == 0) {
			printf("礎熱+礎熱=礎熱");
		} else {
			printf("礎熱+�汝�=�汝�");
		}
	} else {
		if(num2 % 2 == 0) {
			printf("�汝�+礎熱=�汝�");
		} else {
			printf("�汝�+�汝�=礎熱");
		}
	}
	
	return 0;
}
