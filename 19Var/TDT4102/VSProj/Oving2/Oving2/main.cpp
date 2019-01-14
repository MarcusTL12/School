#include "std_lib_facilities.h";

//Del 1

//a)
void inputAndPrintInteger()
{
	int a;
	cout << "Skriv inn et tall: ";
	cin >> a;
	cout << "Du skrev: " << a << '\n';
}


//b)
int inputInteger()
{
	int a;
	cout << "Skriv inn et tall: ";
	cin >> a;
	return a;
}


//c)
void inputIntegersAndPrintSum()
{
	int a = inputInteger();
	int b = inputInteger();
	cout << "Sum: " << a + b << '\n';
}


//e)
bool isOdd(int num)
{
	return num % 2;
}


//f)
void printHumatReadableTime(int sec)
{
	cout << (sec / (60 * 60)) << " timer, " <<
		((sec / 60) % 60) << " minutter og " <<
		(sec % 60) << " sekunder\n";
}


//Del 2

//a)
void inputIntegersUsingLoopAndPrintSum()
{
	int sum = 0;
	int n = 0;
	do
	{
		sum += n;
		n = inputInteger();
	} while (n != 0);

	cout << "Sum: " << sum << '\n';
}


//c)
double inputDouble()
{
	double a;
	cout << "Skriv inn et tall: ";
	cin >> a;
	return a;
}


//d)
void nokToEur()
{
	double kurs = 9.79;
	double nok = 0;
	while ((nok = inputDouble()) <= 0);
	cout << setprecision(2) << fixed;
	cout << nok << " NOK = " << (nok / kurs) << " EUR\n";
}


//Menu
void testFunctions()
{
	unsigned amtchoice = 3;
	unsigned choice;
	do
	{
		cout << "Velg funksjon:\n"
			<< "0) Avslutt\n"
			<< "1) Summer to tall\n"
			<< "2) Summer flere tall\n"
			<< "3) Konverter NOK til EUR\n"
			<< "Angi valg (0 - " << amtchoice << "):\n";
		cin >> choice;

		switch (choice)
		{
		case 0:
			cout << "Shutting down\n";
			break;
		case 1:
			cout << "Hallais\n";
			break;
		default:
			cout << "Not valid function\n";
			break;
		}
	} while (choice != 0);
}


int main() {
	//cout << "Del 1:\n";

	//cout << "a)\n";
	//inputAndPrintInteger();

	//cout << "b)\n";
	//int a = inputInteger();
	//cout << "Du skrev: " << a << '\n';

	//cout << "c)\n";
	//inputIntegersAndPrintSum();

	//cout << "e)\n";
	//for (int i = 0; i <= 15; ++i)
	//	cout << i << " er et " << (isOdd(i) ? "odde" : "par") << "tall\n";

	//cout << "f)\n";
	//printHumatReadableTime(10000);


	//cout << "Del 2:\n";
	
	//cout << "a)\n";
	//inputIntegersUsingLoopAndPrintSum();

	//cout << "c)\n";
	//cout << inputDouble() << '\n';

	//cout << "d)\n";
	//nokToEur();

	testFunctions();
}

