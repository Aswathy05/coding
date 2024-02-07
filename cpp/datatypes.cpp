#include <iostream>
#include <string> // to include strings in your code
using namespace std;

int main()
{
    // Creating variables
    int myNum = 5;             // Integer (whole number)
    float myFloatNum = 5.99;   // Floating point number
    double myDoubleNum = 9.98; // Floating point number
    char myLetter = 'D';       // Character
    bool myBoolean = true;     // Boolean
    string myString = "Hello"; // String

    // Print variable values
    cout << "int: " << myNum << "\n";
    cout << "float: " << myFloatNum << "\n";
    cout << "double: " << myDoubleNum << "\n";
    cout << "char: " << myLetter << "\n";
    cout << "bool: " << myBoolean << "\n";
    cout << "string: " << myString << "\n";

    // e or E is used to indicate the power of 10
    float f1 = 35e3;
    double d1 = 12E4;
    cout << f1;
    cout << d1;
    return 0;
}
