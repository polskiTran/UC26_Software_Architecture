#ifndef MathLibrary_h
#define MathLibrary_h

#pragma once

void Add(int a, int b, void (*callback)(int));

void Subtract(int a, int b, void (*callback)(int));

void Multiply(int a, int b, void (*callback)(int));

void Divide(int a, int b, void (*callback)(int));

void Cube(int a, void (*callback)(int));

void Square(int a, void (*callback)(int));

void Modulo(int a, int b, void (*callback)(int));

#endif // MathLibrary_h
