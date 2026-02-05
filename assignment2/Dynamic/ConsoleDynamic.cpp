#include <iostream>
#include "DynamicLib.h"
int main()
{
    int a = 10, b = 20;
    int result = Add(a, b);
    std:: cout << "The result of Add(" << a << ", " << b << ") is: " << result << std:: endl ;
    std:: cout << "Press Enter to exit..." ;
    std:: cin.get ();
    return 0;
}
