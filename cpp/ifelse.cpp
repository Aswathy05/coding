// shortcut syntax:  variable = (condition) ? expressionTrue : expressionFalse;
#include <iostream>
#include <string>
using namespace std;
int main()
{
    int x, y;
    cin >> x >> y;
    if (x < y)
    {
        cout << "yes";
    }
    else
    {
        cout << "no";
    }

    // shortcut syntax
    string result = (x < y) ? "yes" : "no";
    cout << result;
    return 0;
}
