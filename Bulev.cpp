#include <iostream>
using namespace std;
int main(){
    bool b;
    b=false;
    cout<<"b равно"<<b<<"\n";
    cout << "b равно"<<b<<"\n";
    //булево значение может управлять предложением if
    if(b) cout <<"Это выполняется.\n";
    b=false;
    if(b) cout <<"Это не выполняется.\n";
    //результатом действия оператора отношения является значение true/false
    cout <<"10>9 есть"<<(10>9)<<"\n";
    return 0;

}