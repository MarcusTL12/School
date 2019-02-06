#include "utilities.h"


int incrementByValueNumTimes(int startValue, int increment, int numTimes) {
	for (int i = 0; i < numTimes; i++) {
		startValue += increment;
	}
	return startValue;
}
int incrementByValueNumTimesRef(int& startValue, int& increment, int& numTimes) {
	for (int i = 0; i < numTimes; i++) {
		startValue += increment;
	}
	return startValue;
}


void swapNumbers(int& a, int& b)
{
	a ^= b;
	b ^= a;
	a ^= b;
}


int randlim(int l, int h)
{
	return rand() % (h - l + 1) + l;
}


void randomizeVector(Vector<int>& v, int n)
{
	v.reserve(n);
	for (int i = 0; i < n; ++i)
		if (i < v.size())
			v[i] = randlim(0, 100);
		else
			v.push_back(randlim(0, 100));
}


void printvec(Vector<int>& v)
{
	cout << '[';

	for (int i = 0; i < v.size(); ++i)
		cout << v[i] << (i == (v.size() - 1) ? "" : ", ");

	cout << "]\n";
}


void sortVector(Vector<int>& v)
{
	for (int i = 1; i < v.size(); ++i)
		for (int j = i; j > 0 && v[j - 1] > v[j]; --j)
			swapNumbers(v[j], v[j - 1]);
}


float medianOfVector(Vector<int>& v)
{
	return v.size() % 2 == 0 ? ((float)(v[v.size() / 2 - 1] + v[v.size() / 2])) / 2.0 : v[v.size() / 2];
}


void randomizeString(string& s, int n, char l, char h)
{
	s.reserve(n);
	for (int i = 0; i < n; ++i)
		if (i < s.size())
			s[i] = randlim(l, h);
		else
			s.push_back(randlim(l, h));
}


static bool isvalid(char c, char l, char h)
{
	return toupper(c) >= toupper(l) && toupper(c) <= toupper(h);
}


void readInputToString(string& s, char l, char h)
{
	bool done = false;

	while (!done)
	{
		cout << "Type characters in the range (" << l << " - " << h << "):\n";

		cin >> s;

		done = true;

		for (const char c : s)
			done &= isvalid(c, l, h);

		if (!done)
			cout << "Invalid characters\n";
	}
}

int countChar(const string& s, char c)
{
	c = toupper(c);
	int ret = 0;
	for (const char i : s)
		ret += (toupper(i) == c) ? 1 : 0;
	return ret;
}






