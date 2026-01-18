#include <iostream>
#include <cmath> //для функции ABS
using namespace std;
int main() {
    double num1, num2, num3, num4, num5;
    double sumAbs = 0.0;
    const int COUNT = 5;
    cout <<"Введите пять чисел:" <<endl;
    cout <<"Число 1:"; cin >> num1;
    cout <<"Число 2:"; cin >> num2;
    cout <<"Число 3:"; cin >> num3;
    cout <<"Число 4:"; cin >> num4;
    cout <<"Число 5:"; cin >> num5;
    //Вычисляем сумму абсолютных значений
    sumAbs = abs(num1) + abs(num2) + abs(num3) + abs(num4) + abs(num5);
    //Вычисляем среднее значение 
    double average = sumAbs / COUNT;
    cout << "Среднее значение абсолютных значений: " << average << endl;
    return 0;
}