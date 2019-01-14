#include "std_lib_facilities.h"

static int copies{ 0 };

struct TestPoint
{
	double x, y;

	TestPoint() : x(0), y(0) {}

	TestPoint(double x, double y)
		: x(x), y(y)
	{
	}

	TestPoint(const TestPoint& other)
		: x(other.x), y(other.y)
	{
		++copies;
		cout << "Copied!\n";
	}
};


ostream& operator<<(ostream& strm, const TestPoint& p)
{
	strm << '(' << p.x << ", " << p.y << ')';
	return strm;
}


int main()
{
	int a = 3;
	int& b = a;

	Vector<char> v;

	Vector<double> r;
	r.reserve(100);

	for (int i = 0, lastCap = 1; i < 10000; ++i)
	{
		v.push_back(i);
		if (v.capacity() > lastCap)
		{
			r.push_back(((double)v.capacity()) / ((double)lastCap));
			lastCap = v.capacity();
		}
	}

	for (double& d : r)
		cout << d << '\n';
}