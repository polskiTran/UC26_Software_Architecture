cmake_minimum_required(VERSION 3.16)
project(Assignment2 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(MathLibrary SHARED
    lib/MathLibrary.cpp
)

target_include_directories(MathLibrary
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/lib
)

# Export all symbols on Windows for a simple shared library
set_target_properties(MathLibrary PROPERTIES
    WINDOWS_EXPORT_ALL_SYMBOLS ON
)

add_executable(Assignment2App
    main.cpp
)

target_link_libraries(Assignment2App
    PRIVATE MathLibrary
)
