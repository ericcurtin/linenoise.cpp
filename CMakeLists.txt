cmake_minimum_required(VERSION 3.10)

project("linenoise.cpp")

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wmissing-prototypes -Wtype-limits -Wmissing-noreturn -Wcast-qual -Wno-unused-function -Wno-array-bounds -Wextra-semi -Wunused-result -pedantic -Werror")

# Add the executable
add_executable(llama-run-cli
    llama-run-cli.cpp
    linenoise.cpp 
)

