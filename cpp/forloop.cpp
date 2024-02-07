/* syntax

for (statement 1; statement 2; statement 3) {
  // code block to be executed
}

Statement 1 is executed (one time) before the execution of the code block.

Statement 2 defines the condition for executing the code block.

Statement 3 is executed (every time) after the code block has been executed. */

#include <iostream>
using namespace std;
int main()
{
    for (int i = 0; i < 5; i++)
    {
        cout << i << "\n";
    }

    // nested loop
    for (int i = 1; i <= 2; ++i) // outer loop
    {
        cout << "outer: " << i << "\n";
        for (int j = 1; j <= 3; ++j) // inner loop
        {
            cout << "inner: " << j << "\n";
        }
        cout << "\n";
    }

    // foreach loop
    /*

    SYNTAX:
     for (type variableName : arrayName) {
     code block to be executed
    }

    */

    int myNumbers[5] = {1, 2, 3, 4, 5};
    for (int i : myNumbers)
    {
        cout << i << "\n";
    }
    return 0;
}

// i++ ------> increments the value after the loop
// ++i ------> increments the value before the loop
