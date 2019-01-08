#include <iostream>

#define LOG(x) std::cout << x
#define ENDL() std::cout << std::endl


int main()
{
	int a = 0;
	
	std::cin >> a;
	
	LOG(a);
}
