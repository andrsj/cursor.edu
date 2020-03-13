// Boolean function.cpp : main project file.

#include "stdafx.h"
#include <iostream>


using namespace System;
using namespace std;

int main ()
{
	int a, b, c, y1, y2, y3, y4, y5, y6, y7;

	printf("A  |B  |!A |A^B|AvB|A->B|A~B|AxorB|\n");
	printf("-----------------------------------\n");
	for(a=1; a>=0; a--)
	{
		for(b=1; b>=0; b--)
		{
			y1 = !a;
			y2 = a&&b;
			y3 = a||b;
			y4 = a<=b;
			y5 = a==b;
			y6 = a^b;
			printf(" %i | %i | %i | %i | %i | %i  | %i |  %i  |\n", a, b, y1, y2, y3, y4, y5, y6);
		}
	}

    printf("\n\n\n");
    printf("a  |b  |c  |y1 |y2  |y3 |y4  |y5 |y6  |y7 |\n");
	printf("a  |b  |c  |!b |A^!B|!()|()vC|AvB|()vC|end|\n");
    printf("-------------------------------------------\n");
	for(a=1; a>=0; a--)
    {
		for(b=1; b>=0; b--)
        {
             for(c=1; c>=0; c--)
             {
                 //y = ( (!x1 && x2) || (x1 && !x2) ) && (x3 || x1 && x2);

				 //NOT A | A AND B | A OR B | A->B | A~B | A XOR B |
				 //  !a  |  A && B | A || B | A<=B | A=B | A ^ B   |
				 y1 = !b;
				 y2 = a&&y1;
				 y3 = !y2;
				 y4 = y3||c;
				 y5 = a||b;
				 y6 = y5||c;
				 y7 = y4^y6;
                 printf(" %i | %i | %i | %i | %i  | %i | %i  | %i | %i  | %i | \n", a, b, c, y1, y2, y3, y4, y5, y6, y7);
             };
        };
    };

    
    system ("pause");
    return 0;
}