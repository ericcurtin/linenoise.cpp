cmake_minimum_required(VERSION 3.10)

project("linenoise.cpp")

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wmissing-prototypes -pedantic -Werror")

# Add the executable
add_executable(linenoise
    example.cpp 
    linenoise.cpp 
)

