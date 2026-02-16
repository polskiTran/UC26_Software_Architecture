#include <iostream>
#include "MathLibrary.h"

void MathResult1(int result) {
    std::cout << "  (>) Math Result: " << float(result) << std::endl;
}
void MathResult2(int result) {
    std::cout << "  (>) Divide by 3: " << float(result)/3 << std::endl;
}
int main() {
    std::cout << "Run MathLibrary with Callbacks MathResult1..." << std::endl;
    // MathResult1
    Add(10, 20, MathResult1);
    Subtract(10, 20, MathResult1);
    Multiply(5, 6, MathResult1);
    Divide(10, 2, MathResult1);
    Modulo(10, 3, MathResult1);
    Cube(5, MathResult1);
    Square(6, MathResult1);

    // MathResult2
    std::cout << "\n----------------------------------------------" << std::endl;
    std::cout << "Run MathLibrary with Callbacks MathResult2..." << std::endl;
    Add(10, 20, MathResult2);
    Multiply(5, 6, MathResult2);
    Divide(10, 2, MathResult2);
    Modulo(10, 3, MathResult2);
    Cube(5, MathResult2);
    Square(6, MathResult2);
    return 0;
}
