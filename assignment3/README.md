```bash
# generate `./build`
cmake -S . -B build

# compile code
cmake --build build

# run test
# on macos/linux
/build/run_tests
# on win
.\build\Debug\run_tests.exe
```