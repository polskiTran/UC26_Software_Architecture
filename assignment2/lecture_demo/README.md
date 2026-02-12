Compile and link static library
```shell
clang++ ConsoleStatic.cpp StaticLib.cpp -o ConsoleStatic

./ConsoleStatic
```

Compile and link dynamic library
```shell
clang++ -dynamiclib -o DynamicLib.dylib DynamicLib.cpp -std=c++17

clang++ -o ConsoleDynamic ConsoleDynamic.cpp -I. ./DynamicLib.dylib -Wl,-rpath,@executable_path 

./ConsoleDynamic
```

or, alternative
```shell
clang++ -dynamiclib -o libDynamic.dylib DynamicLib.cpp -std=c++17

clang++ -o ConsoleDynamic ConsoleDynamic.cpp -I. -L. -lDynamic -Wl,-rpath,@executable_path
```
