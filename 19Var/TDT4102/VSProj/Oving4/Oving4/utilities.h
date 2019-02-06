#pragma once
#include <std_lib_facilities.h>

int incrementByValueNumTimes(int startValue, int increment, int numTimes);int incrementByValueNumTimesRef(int& startValue, int& increment, int& numTimes);
void swapNumbers(int& a, int& b);

void randomizeVector(Vector<int>& v, int n);

void printvec(Vector<int>& v);

void sortVector(Vector<int>& v);

float medianOfVector(Vector<int>& v);

void randomizeString(string& s, int n, char l, char h);

void readInputToString(string& s, char l, char h);

int countChar(const string& s, char c);
