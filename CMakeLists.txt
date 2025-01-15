cmake_minimum_required(VERSION 3.10)

project("linenoise.cpp")

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the executable
add_executable(MyProject 
    example.cpp 
    linenoise.cpp 
)

