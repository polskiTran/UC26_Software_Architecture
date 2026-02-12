- Install `cmake` on linux
```bash
sudo apt install cmake
```

- Build with CMake
```bash
# Reads CMakeLists.txt, detects your system/compilers, finds dependencies, and generates native build files (e.g., Makefiles) in the build folder. This keeps source code clean via out-of-source builds.
cmake -S . -B build

# Invokes the native build tool (e.g., Make, Ninja, MSBuild) on the build directory to compile and link the project. It abstracts platform differences, so the same command works across Windows, Linux, and macOS.
cmake --build build
```

- Run the built executable
```bash
cd assignment2/

./build/Assignment2App
```
