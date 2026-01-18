#include <iostream>
using namespace std;
int main(){
    const double GRAVITY_RATIO = 0.17; //КОэффициент силы тяжести на нуле
    cout <<"Таблица перевода земных футов в лунные эквиваленты:" <<endl;
    cout <<"---------------------" <<endl;

for (int earthPounds = 1; earthPounds <= 100; earthPounds++){
    double moonPounds = earthPounds * GRAVITY_RATIO;
    cout <<earthPounds<<"земных фунтов ="<<moonPounds<<"лунных фунтов"<<endl;

    //После каждых 25 фунтов выводим пустую строку
    if (earthPounds%25==0){
        cout << endl; // пустая строка
    }
}
return 0;
}