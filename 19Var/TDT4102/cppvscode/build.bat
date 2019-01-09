@echo off
g++ -D WIN32 -Igraphlib -I../cppvscode -c *.cpp
g++ -o test.exe *.o graphlib.l
del *.o
