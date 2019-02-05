#include <std_lib_facilities.h>
#include "cannonball.h"


bool testDeviation(const double& a, const double& b, const double& tol = pow(10, -10))
{
	return abs(a - b) < tol;
}


void testCannonball()
{
	Vector<Vector<double>> testvals(6);
	testvals[0] = Vector<double>(3, 0);
	testvals[1] = Vector<double>(3, -9.81);
	testvals[2] = Vector<double>(3, 50);
	testvals[3] = { 25, .475, -24.05 };
	testvals[4] = { 0, 125, 250 };
	testvals[5] = { 0, 31.84, 2.375 };
	

	double ts[]{ 0.0, 2.5, 5.0 };

	double velX = 50, initVelY = 25;

	auto cw = setw(10), cw1 = setw(6);
	cout << setprecision(2) << fixed;

	cout << cw1 << ' ';
	for (const double& t : ts)
	{
		ostringstream temp;
		temp << setprecision(2) << fixed << "T = " << t;
		cout << cw << temp.str();
	}

	cout << '\n';

	cout << left << cw1 << "acclX";
	for (const double& t : ts)
		cout << right << cw << 0;

	cout << '\n';

	cout << left << cw1 << "acclY";
	for (const double& t : ts)
		cout << right << cw << acclY();

	cout << '\n';

	cout << left << cw1 << "velX";
	for (const double& t : ts)
		cout << right << cw << velX;

	cout << '\n';

	cout << left << cw1 << "velY";
	for (const double& t : ts)
		cout << right << cw << velY(initVelY, t);

	cout << '\n';

	cout << left << cw1 << "posX";
	for (const double& t : ts)
		cout << right << cw << posX(0, velX, t);

	cout << '\n';

	cout << left << cw1 << "posY";
	for (const double& t : ts)
		cout << right << cw << posY(0, initVelY, t);

	cout << '\n';
}


void stuff(int& a)
{
	cout << ++a << '\n';
}


int main() {
	//testCannonball();

	int q = 5;

	stuff(q);

	keep_window_open();
}

