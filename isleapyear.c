#include<stdio.h>
#include<stdlib.h>
int main(int argc, char* argv[]) { 
	char*p;
    long year = strtol(argv[1],&p,10);
	if (year % 400 == 0) {
        printf ("%d was a leap year",year);
    }
	else if (year % 100 == 0){
	    printf ("%d was not a leap year",year);
	}
	else if (year % 4 == 0) {
	    printf ("%d was a leap year",year);
	}
	else{
	    printf ("%d was not a leap year",year);
	}
}