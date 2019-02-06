#include "tests.h"
#include "utilities.h"
#include <std_lib_facilities.h>
#include <unordered_set>


void testCallByValue()
{
	int v0 = 5;
	int increment = 2;
	int iterations = 10;
	int result = incrementByValueNumTimes(v0, increment, iterations);
	cout << "v0: " << v0
		<< " increment: " << increment
		<< " iterations: " << iterations
		<< " result: " << result << endl;
}void testCallByReference()
{
	int v0 = 5;
	int increment = 2;
	int iterations = 10;
	int result = incrementByValueNumTimesRef(v0, increment, iterations);
	cout << "v0: " << v0
		<< " increment: " << increment
		<< " iterations: " << iterations
		<< " result: " << result << endl;
}void testSwap(){	int a = 5, b = 7;	cout << "a = " << a << ", b = " << b << "\nSwapping...\n";	swapNumbers(a, b);	cout << "a = " << a << ", b = " << b << '\n';}

void testVectorSorting()
{
	Vector<int> percentages;

	int n;
	cout << "How many values to sort: ";
	cin >> n;

	randomizeVector(percentages, n);

	printvec(percentages);

	cout << "Sorting...\n";
	
	sortVector(percentages);

	printvec(percentages);

	cout << "Median: " << medianOfVector(percentages) << '\n';
}


void testString()
{
	string grades;

	readInputToString(grades, 'A', 'F');

	Vector<int> gradeCount(6, 0);

	for (int i = 0; i < 6; ++i)
		gradeCount[i] += countChar(grades, 'F' - i);

	float avg = 0;

	for (int i = 0; i < 6; ++i)
		avg += i * gradeCount[i];

	avg /= grades.size();

	cout << "Average grade: " << setprecision(1) << fixed << avg << '\n';
}


static int checkCharactersAndPosition(string& code, string& guess)
{
	int ret = 0;
	for (int i = 0; i < code.size(); ++i)
		ret += code[i] == guess[i] ? 1 : 0;
	return ret;
}


static int checkCharacters(string& code, string& guess)
{
	unordered_set<char> chars;
	for (char c : guess)
		chars.insert(c);

	for (char c : code)
		chars.insert(c);

	int ret = 0;
	for (char c : chars)
		ret += min(countChar(code, c), countChar(guess, c));

	return ret;
}


void playMastermind()
{
	//kunne brukt const om size og letters ble initializet fra input ved startup
	constexpr int size = 4, letters = 6;

	string code, guess;

	randomizeString(code, size, 'A', 'A' + (letters - 1));

	bool done = false;

	int lives = 10;

	while (!done)
	{
		cout << "Lives left: " << lives << '\n';
		bool corrguess = false;
		while (!corrguess)
		{
			cout << "Make a guess (" << size << " letters, A - " << (char)('A' + (letters - 1)) << "):\n";
			cin >> guess;
			corrguess = guess.size() == size;
			if (!corrguess)
				cout << "invalid numer of characters, try again:\n";
		}

		int corr = checkCharacters(code, guess);
		int corrpos = checkCharactersAndPosition(code, guess);


		if (corrpos == size)
		{
			cout << "Correct!\n";
			done = true;
		}
		else if (lives <= 0)
		{
			cout << "Out of lives :(\n";
			done = true;
		}
		else
		{
			cout << "Correct letters: " << corr << '\n';
			cout << "Letters in correct position: " << corrpos << '\n';
		}
		--lives;
	}
}

