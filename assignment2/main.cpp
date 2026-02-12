#include <iostream>
#include "MathLibrary.h"

void MathResult1(int result) {
    std::cout << "Math Result: " << result << std::endl;
}
void MathResult2(int result) {
    std::cout << "Divide by 3: " << result/3 << std::endl;
}
int main() {
    std::cout << "Run MathLibrary with Callbacks..." << std::endl;
    Add(10, 20, MathResult1);
    Multiply(5, 6, MathResult1);
    Add(10, 20, MathResult2);
    Multiply(5, 6, MathResult2);
    return 0;
