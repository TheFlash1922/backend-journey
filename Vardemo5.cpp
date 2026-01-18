#include <iostream>
using namespace std;
int main()
{
    int ivar;//Объявление переменной типа Int
    double dvar; //объявление переменной с плавающей точкой 
    ivar = 100;
    dvar = 100.0;
    cout << "Исходное значение ivar:"<< ivar << "\n";
    cout << "Исходное значение dvar:"<< dvar << "\n";
    cout <<"\n";
    ivar = ivar / 3;
    dvar = dvar / 3.0;
    cout << "ivar после деления:" <<ivar <<"\n";
    cout << "dvar после деления:" <<dvar <<"\n";
    return 0;
}