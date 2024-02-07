/*syntax ----- type variableName = value;
type ----- int,double,char,string,bool*/
#include <iostream>
using namespace std;

int main()
{
    // declaring a variable
    int myNum = 15;
    cout << myNum << "\n";
    // declaring the variable separately
    int myNum2;
    myNum2 = 10;
    cout << myNum2 << "\n";

    // addition by saving the sum first and then printing it
    int x = 1;
    int y = 2;
    int sum = x + y;
    cout << sum << "\n";

    // Assigning values first and then printing the sum of numbers directly
    int a = 1, b = 2, c = 6;
    cout << a + b + c;

    const int number = 15; // myNum will always be 15
    // number = 10;                   // error: assignment of read-only variable 'myNum'
    const int minutesPerHour = 60; // use const when you don't want your variable to be changed
    const float PI = 3.14;
    return 0;
}
