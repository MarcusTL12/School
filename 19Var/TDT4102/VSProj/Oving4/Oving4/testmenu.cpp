#include "testmenu.h"

void testMenu(Vector<Test>& tests)
{
	int choice;

	do
	{
		cout << "Choose test:\n" << "(0): Exit\n";

		for (int i = 0; i < tests.size(); ++i)
			cout << '(' << i + 1 << "): " << tests[i].name << '\n';

		cin >> choice;

		if (choice == 0)
			cout << "Exiting...\n";
		else if (choice < 0 || choice > tests.size())
			cout << "Invalid choice, Try again\n";
		else
			tests[choice - 1].test();

	} while (choice != 0);
}
