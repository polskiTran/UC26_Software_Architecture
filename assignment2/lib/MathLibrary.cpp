#include "MathLibrary.h"
#include <iostream>
using namespace std;

// Math function 1: Addition
void Add(int a, int b, void (*callback)(int)) {
    cout << "\n(*) Adding " << a << " and " << b << endl;
    int result = a + b;
    callback(result);
}

// Math function 2: Subtraction
void Subtract(int a, int b, void (*callback)(int)) {
    cout << "\n(*) Subtracting " << b << " from " << a << endl;
    int result = a - b;
    callback(result);
}

// Math function 3: Multiplication
void Multiply(int a, int b, void (*callback)(int)) {
    cout << "\n(*) Multiplying " << a << " and " << b << endl;
    int result = a * b;
    callback(result);
}

// Math function 4: Division
void Divide(int a, int b, void (*callback)(int)) {
    cout << "\n(*) Dividing " << a << " by " << b << endl;
    int result = a / b;
    callback(result);
}

// Math function 5: Modulo
void Modulo(int a, int b, void (*callback)(int)) {
    cout << "\n(*) Modulo " << a << " by " << b << endl;
    int result = a % b;
    callback(result);
}

// Math function 6: Cube
void Cube(int a, void (*callback)(int)) {
    cout << "\n(*) Cubing " << a << endl;
    int result = a * a * a;
    callback(result);
}

// Math function 7: Square
void Square(int a, void (*callback)(int)) {
    cout << "\n(*) Squaring " << a << endl;
    int result = a * a;
    callback(result);
}
