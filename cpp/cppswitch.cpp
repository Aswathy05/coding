#include <iostream>
using namespace std;
int main()
{
    int day = 2;
    int month = 5;
    switch (month)
    {
    case 1:
        cout << "Monday";
        break;
    case 2:
        cout << "Tuesday";
        break;
    default:
        cout << "There are no months here";
        break;
    }
}