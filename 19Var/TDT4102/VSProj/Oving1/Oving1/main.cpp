#include "std_lib_facilities.h"


//a)
template <typename T>
T maxOfTwo(T a, T b)
{
	if (a > b)
	{
		cout << "A is greater than B\n";
		return a;
	}
	else
	{
		cout << "B is greater than or equal to A\n";
		return b;
	}
}


int fibonacci(int n)
{
	int a = 0;
	int b = 1;
	cout << "Fibonacci numbers:\n";
	for (int x = 0; x <= n; ++x)
	{
		cout << x << " " << b;
		int temp = b;
		b += a;
		a = temp;
	}
	cout << "----\n";
	return b;
}


int main()
{
	cout << "Oppgave a)\n";
	cout << maxOfTwo(5, 6) << '\n';
}