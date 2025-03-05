#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/select.h>

#include <memory>
#include <string>

#include "linenoise.h"

int main(int, char **) {
    while (1) {
        static const char *                         prompt_prefix = "> ";
        std::unique_ptr<char, decltype(&std::free)> line(const_cast<char *>(linenoise(prompt_prefix)), free);
        if (!line) {
            break;
        }

        std::string user_input = line.get();
        if (user_input.empty()) {
            continue;
        }
        /* Do something with the string. */
        printf("\033[33mecho: '%s'\033[0m\n", line.get());
        linenoiseHistoryAdd(line.get()); /* Add to the history. */
    }

    return 0;
}

