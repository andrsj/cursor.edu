// Lab_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "LogCon.h"
#include <iostream>
#include <string>

using namespace std;


string TextFormat (bool x)
{
	if (x == true) 
	return "  T  ";
	else
	return "  F  ";
}


/*char SymbolFormat (bool x)
{
	if (x == true)
	return 'T';
	else
	return 'F';
}
*/

int _tmain(int argc, _TCHAR* argv[])
{
	bool a,b,c,y1,y2,y3,y4,y5,y6,y7;
	string text1,text2,text3,text4,text5,text6,text7,ctext,btext,atext;
	cout << "|  A  |  B  |  C  | !B  |A^!B | !() |()vC | AvB |()vC | END |" << endl;
	cout << "-------------------------------------------------------------" << endl;
	// 3 3 3 3 5 3 5 3 5 3
				 

	for (int i=0; i<8 ;i++)
	{
		a = i      & 0xF1;
		b = (i>>1) & 0xF1;
		c = (i>>2) & 0xF1;

				 /*
				 y1 = !b;
				 y2 = a&&y1;
				 y3 = !y2;
				 y4 = y3||c;
				 y5 = a||b;
				 y6 = y5||c;
				 y7 = y4^y6;
				 */
		atext = TextFormat(a);
		btext = TextFormat(b);
		ctext = TextFormat(c);
		y1 = LogConFuncs::MyLogConFuncs::NOT(b);      //  !b
		text1 = TextFormat(y1);
		y2 = LogConFuncs::MyLogConFuncs::AND(a,y1);   //  a && !b
		text2 = TextFormat(y2);
		y3 = LogConFuncs::MyLogConFuncs::NOT(y2);     //  !( a && !b )
		text3 = TextFormat(y3);
		y4 = LogConFuncs::MyLogConFuncs::OR(y3,c);    //  !( a && !b ) ^ c
		text4 = TextFormat(y4);
		y5 = LogConFuncs::MyLogConFuncs::OR(a,b);     //  a || b
		text5 = TextFormat(y5);
		y6 = LogConFuncs::MyLogConFuncs::OR(y5,c);    //  (a || b) || c
		text6 = TextFormat(y6);
		y7 = LogConFuncs::MyLogConFuncs::XOR(y4,y6);  //  (!( a && !b ) ^ c) xor (a || b) || c
		text7 = TextFormat(y7);
		//cout << "|" << ctext << "|" << btext << "|" << atext << "|" << text1 << "|" << text2 << "|" << text3 << "|" << text4 << "|" << text5 << "|" << text6 << "|" << text7 << "|" << endl;
		cout << "|" << atext << "|" << btext << "|" << ctext << "|" << text1 << "|" << text2 << "|" << text3 << "|" << text4 << "|" << text5 << "|" << text6 << "|" << text7 << "|" << endl;

	}

	cout << "__________________________________________________________________" << endl;
	cout << "__________________________________________________________________" << endl;
	cout << "__________________________________________________________________" << endl;

	cout << "|  A  |  B  | !A  | AND | OR  | IMP | EQU | XOR |" << endl; 
	cout << "-------------------------------------------------" << endl;

	for (int i=0; i<4 ;i++)
	{
		a = i      & 0xF1;
		b = (i>>1) & 0xF1;

		atext = TextFormat(a);
		btext = TextFormat(b);

		y1 = LogConFuncs::MyLogConFuncs::NOT(a);
		text1 = TextFormat(y1);
		y2 = LogConFuncs::MyLogConFuncs::AND(a,b);
		text2 = TextFormat(y2);
		y3 = LogConFuncs::MyLogConFuncs::OR(a,b);
		text3 = TextFormat(y3);
		y4 = LogConFuncs::MyLogConFuncs::IMP(a,b);
		text4 = TextFormat(y4);
		y5 = LogConFuncs::MyLogConFuncs::EQU(a,b);
		text5 = TextFormat(y5);
		y6 = LogConFuncs::MyLogConFuncs::XOR(a,b);
		text6 = TextFormat(y6);

		//cout  << "|" << btext << "|" << atext << "|" << text1 << "|" << text2 << "|" << text3 << "|" << text4 << "|" << text5 << "|" << text6 << "|" << endl;
		cout  << "|" << atext << "|" << btext << "|" << text1 << "|" << text2 << "|" << text3 << "|" << text4 << "|" << text5 << "|" << text6 << "|" << endl;
	}

	return 0;


	/*for (bool a: {false,true})
	{
		for (bool b: {false,true})
		{
			y1 = !a;
			y2 = a&&b;
			y3 = a||b;
			y4 = a<=b;
			y5 = a==b;
			y6 = a^b;
			cout << a << b << y1 << y2 << y3 << y4 << y5 << y6 << endl;
		}
	}	
	*/
	/* for(a=1; a>=0; a--)
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
	}   */
	/*
	y1 = LogConFuncs::MyLogConFuncs::AND(b,c);
	cout << "B ^ C = " << y1 << endl;
	y2 = LogConFuncs::MyLogConFuncs::OR(a,c);
	cout << "A v C = " << y2 << endl;
	y3 = LogConFuncs::MyLogConFuncs::IMP(y1,y2);
	cout << "(B^C)->(AvC) = " << y3 << endl; 
	return 0;  
	*/
}

