#include "std_lib_facilities.h"
#include "loan_drawer.h"

constexpr char æ = 145, Æ = 146, å = 134, Å = 143, ø = 155, Ø = 157;

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


//Del 3

//Counts digits in positive integer
int digits(int i)
{
	if (i == 0) return 1;
	if (i < 0) return 1 + digits(-i);
	return (int)log10(i) + 1;
}


void printRange(char c, int amt)
{
	cout << setfill(c) << setw(amt - 1) << c << setfill(' ');
}


//b)
void printMultTable(int w, int h)
{
	Vector<int> widths(w);
	for (int i = 0; i < w; ++i)
		widths[i] = digits((i + 1) * h);

	char hLine = 196;
	char vLine = 179;
	char cross = 197;

	cout << '\n' << setw(widths[0] + 1) << '*';

	for (int i = 0; i < w; ++i)
		cout << ' ' << vLine << setw(widths[i] + 1) << (i + 1);
	cout << '\n';


	for (int j = 0; j < h; ++j)
	{
		printRange(hLine, widths[0] + 3);
		for (int i = 0; i < w; ++i)
		{
			cout << cross;
			printRange(hLine, widths[i] + 3);
		}

		cout << '\n' << setw(widths[0] + 1) << j;

		for (int i = 0; i < w; ++i)
			cout << ' ' << vLine << setw(widths[i] + 1) << ((i + 1) * (j + 1));
		cout << '\n';
	}

	cout << '\n';
}


void multTable()
{
	int w, h;
	cout << "Width: ";
	cin >> w;
	cout << "Height: ";
	cin >> h;
	printMultTable(w, h);
}


//Del 4
//a)
double discriminant(double a, double b, double c)
{
	return b * b - 4 * a * c;
}


//b)
void printRealRoots(double a, double b, double c)
{
	double disc{ discriminant(a, b, c) };

	if (disc < 0)
		cout << "Ligningen har 0 reelle nullpunkt.\n";
	else if (disc == 0)
		cout << "x = " << (-b / (2 * a)) << '\n';
	else
		cout << "x = " << ((-b + sqrt(disc)) / (2 * a))
		<< ", x = " << ((-b - sqrt(disc)) / (2 * a)) << '\n';
}


//c)
void solveQuadraticEquation()
{
	double a, b, c;
	cout << "Skriv koefficientene: a b c\n";
	cin >> a >> b >> c;
	printRealRoots(a, b, c);
}


//Del 5
template<typename T>
void printVector(const Vector<T>& vec)
{
	cout << '[';
	for (const T& e : vec)
		cout << e << ", ";
	cout << "]\n";
}


//a)
Vector<int> calculateSeries(int total, double rente, int years)
{
	double avdrag = total / years;
	Vector<int> ret(years);
	for (int i = 0; i < years; ++i)
	{
		ret[i] = (int)(avdrag + (total * (rente / 100.0)));
		total -= avdrag;
	}
	ret.back() += total;
	return ret;
}


//b)
Vector<int> calculateAnnuity(int total, double rente, int years)
{
	Vector<int> ret(years, (int)(total * (rente / 100.0) / (1 - pow(1 + rente / 100, -years))));
	return ret;
}


void printLoan(int total, double rente, int years)
{
	Vector<int> ser = calculateSeries(total, rente, years);
	Vector<int> ann = calculateAnnuity(total, rente, years);

	constexpr int colwidth = 14;
	const auto sep = setw(colwidth);

	cout << sep << string{ Å, 'r' } << sep << "Annuitet" << sep << "Serie" << sep << "Differanse\n";
	int sumSer = 0, sumAnn = 0;
	for (int i = 0; i < years; ++i)
	{
		cout << sep << i + 1 << sep << ann[i] << sep << ser[i] << sep << ann[i] - ser[i] << '\n';
		sumSer += ser[i];
		sumAnn += ann[i];
	}

	cout << sep << "Total" << sep << sumAnn << sep << sumSer << sep << sumAnn - sumSer << '\n';

	drawPlot(ann, ser, total, rente);
}


void testLoan()
{
	cout << "(Totalsum) (rente) (antall avdrag)\n";
	int total, years;
	double rente;
	cin >> total >> rente >> years;
	printLoan(total, rente, years);
}


//Menu
void testFunctions()
{
	unsigned amtchoice = 8;
	unsigned choice = -1;
	do
	{
		cout << "Velg funksjon:\n"
			<< "0) Avslutt\n"
			<< "1) Summer to tall\n"
			<< "2) Summer flere tall\n"
			<< "3) Konverter NOK til EUR\n"
			<< "4) Oddetall\n"
			<< "5) Sekunder til lesbar tid\n"
			<< "6) Gangetabell\n"
			<< "7) Andregradsligning\n"
			<< "8) L" << å << "n\n"
			<< "Angi valg (0 - " << amtchoice << "):\n";
		cin >> choice;

		switch (choice)
		{
		case 0:
			cout << "Shutting down\n";
			break;
		case 1:
			inputIntegersAndPrintSum();
			break;
		case 2:
			inputIntegersUsingLoopAndPrintSum();
			break;
		case 3:
			nokToEur();
			break;
		case 4:
			for (int i = 0; i <= 15; ++i)
				cout << i << " er et " << (isOdd(i) ? "odde" : "par") << "tall\n";
			break;
		case 5:
			printHumatReadableTime(inputInteger());
			break;
		case 6:
			multTable();
			break;
		case 7:
			solveQuadraticEquation();
			break;
		case 8:
			testLoan();
			break;
		default:
			cout << "Not valid function\n";
			break;
		}
	} while (choice != 0);
}


int main() {
	testFunctions();
}

