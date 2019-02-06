#include <std_lib_facilities.h>
#include "tests.h"
#include "testmenu.h"

//Oppgave 1

/*
a)
5 siden v0 er passet by value og endringer derfor ikke påvirker v0
*/



int main()
{
	srand((unsigned)time(nullptr));

	Vector<Test> tests{
		{ "Test pass by value", testCallByValue },
		{ "Test pass by reference", testCallByReference },
		{ "Test swap numbers", testSwap },
		{ "Test vector sorting", testVectorSorting },
		{ "Test string", testString },
		{ "Play mastermind", playMastermind }
	};

	testMenu(tests);
}

