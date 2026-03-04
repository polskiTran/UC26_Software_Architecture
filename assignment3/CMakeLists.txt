cmake_minimum_required(VERSION 3.14)
project(uc26-software-architecture-assignment3)

# 1. cpp settings
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 2. fetch gtest from github repo
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# --for Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# 3. lib for the code
add_library(cart_lib INTERFACE)
target_include_directories(cart_lib INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})

# 4. create test .exe
add_executable(run_tests CartTest.cpp)

# 5. link gtest and code to the test executable
target_link_libraries(run_tests
    cart_lib
    GTest::gtest_main # Links gtest and provides a default main() function
)

# 6. enable testing in CMake
include(GoogleTest)
gtest_discover_tests(run_tests)
