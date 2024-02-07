#include <iostream>
using namespace std;
#include <string>
int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        int len = s.length();
        if (len <= 10)
        {
            cout << s << "\n";
        }
        else
        {
            cout << s[0] << len - 2 << s[len - 1] << "\n";
        }
    }
    return 0;
}