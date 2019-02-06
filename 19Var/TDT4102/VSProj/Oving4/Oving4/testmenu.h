#pragma once
#include <std_lib_facilities.h>
#include <functional>


struct Test
{
	string name;
	function<void()> test;
};


void testMenu(Vector<Test>& tests);
