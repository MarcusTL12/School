#include <std_lib_facilities.h>
#include "cannonball.h"

double acclY()
{
	return -9.81;
}

double velY(double initVelocityY, double time)
{
	return initVelocityY + acclY() * time;
}

double posX(double initPosition, double initVelocity, double time)
{
	return initPosition + initVelocity * time;
}

double posY(double initPosition, double initVelocity, double time)
{
	return initPosition + initVelocity * time + acclY() * time * time / 2;
}

void printTime(double time)
{
	int h = (int)(time / (60 * 60));
	int m = ((int)(time / 60) % 60);
	double s = time - 60 * (m + 60 * h);

	if (h != 0)
		cout << h << " hours, " << m << " minutes and ";
	else if (m != 0)
		cout << m << " minutes and ";

	cout << setprecision(2) << fixed << s << " seconds\n";
}

double flightTime(double initVelocity)
{
	return -2 * initVelocity / acclY();
}
