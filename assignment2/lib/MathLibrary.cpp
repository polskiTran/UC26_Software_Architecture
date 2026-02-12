#include "MathLibrary.h"

// Math function 1: Addition
void Add(int a, int b, void (*callback)(int)) {
    int result = a + b;
    callback(result);
}

// Math function 2: Subtraction
void Subtract(int a, int b, void (*callback)(int)) {
    int result = a - b;
    callback(result);
}

// Math function 3: Multiplication
void Multiply(int a, int b, void (*callback)(int)) {
    int result = a * b;
    callback(result);
}

// Math function 4: Division
void Divide(int a, int b, void (*callback)(int)) {
    int result = a / b;
    callback(result);
}

// Math function 5: Modulo
void Modulo(int a, int b, void (*callback)(int)) {
    int result = a % b;
    callback(result);
}

// Math function 6: Power
void Power(int a, int b, void (*callback)(int)) {
    int result = pow(a, b);
    callback(result);
}

// Math function 7: Square
void Square(int a, void (*callback)(int)) {
    int result = a * a;
    callback(result);
}
