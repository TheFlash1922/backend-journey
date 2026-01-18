#include <iostream>
using namespace std;

int main(){
    const double JUPITER_YEAR_TO_EARTH_YEAR = 12.0; // 1 юпитерианский год равен 12 земных лет
    double jupiterYears;
    cout <<"Введите количество юпитерианских лет";
    cin >> jupiterYears;
    double earthYears = jupiterYears * JUPITER_YEAR_TO_EARTH_YEAR;
    cout << jupiterYears <<"юпитерианских лет равно" << earthYears <<"земным годам." << endl;
    return 0;
}