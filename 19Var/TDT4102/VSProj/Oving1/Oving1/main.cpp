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

//c)
int fibonacci(int n)
{
	int a = 0;
	int b = 1;
	cout << "Fibonacci numbers:\n";
	for (int x = 0; x <= n; ++x)
	{
		cout << x << " " << b << "\n";
		int temp = b;
		b += a;
		a = temp;
	}
	cout << "----\n";
	return b;
}

//d)
int squareNumberSum(int n)
{
	int totalSum = 0;

	for (int i = 0; i < n; ++i)
	{
		totalSum += i * i;
		cout << i * i << '\n';
	}

	cout << totalSum << '\n';

	return totalSum;
}

//e)
void triangleNumbersBelow(int n)
{
	int acc = 1, num = 2;

	cout << "Triangle numbers below " << n << ":\n";

	while (acc < n)
	{
		cout << acc << '\n';
		acc += num;
		num++;
	}

	cout << '\n';
}

//f)
bool isPrime(int n)
{
	for (int i = 2; i < n; ++i)
	{
		if (n % i == 0)
		{
			return false;
		}
	}

	return true;
}

//g)
void naivePrimeNumberSearch(int n)
{
	for (int num = 2; num < n; ++num)
	{
		if (isPrime(num))
		{
			cout << num << " is a prime\n";
		}
	}
}

//h)
int findGreatestDivisor(int n)
{
	for (int div = n - 1; div > 0; --div)
	{
		if (n % div == 0)
		{
			return div;
		}
	}
}


int main()
{
	cout << "oppgave a)\n";
	cout << maxOfTwo(5, 6) << '\n';

	cout << "oppgave c)\n";
	cout << fibonacci(10) << '\n';

	cout << "oppgave d)\n";
	cout << squareNumberSum(6) << '\n';

	cout << "oppgave e)\n";
	triangleNumbersBelow(100);

	cout << "oppgave f-g)\n";
	naivePrimeNumberSearch(100);

	cout << "oppgave h)\n";
	cout << findGreatestDivisor(113);
}