#include <iostream>
using namespace std;
int main(){
    int a,b,c;
    a=2;
    b=3;
    if(a<b) cout <<"a меньше чем b\n";
    //это предложение ничего не выведет на экран
    if (a==b) cout <<"это вы не увидите\n";
    cout <<"\n";
    c=a-b;//c содержит -1
    cout <<"c содержит -1\n";
    if (c>=0) cout << "c неотрицательно\n";
    if (c<0) cout <<"c отрицательно\n";
    cout <<"\n";
    c=b-a;//с теперь содержит 1
    cout <<"c содержит 1\n";
    if(c>0) cout <<"c неотрицательно\n";
    if(c<0) cout <<"c отрицательно\n";
    return 0;
}