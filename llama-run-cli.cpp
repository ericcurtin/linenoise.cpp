#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/select.h>

#include <string>

#include "linenoise.h"

struct c_str {
    const char * data = nullptr;

    ~c_str() { free((void *) data); }
};

int main(int, char **) {
    while (1) {
        static const char * prompt_prefix = "> ";
        c_str               line;
        line.data = linenoise(prompt_prefix);
        if (line.data == NULL) {
            break;
        }

        std::string user_input = line.data;
        if (user_input.empty()) {
            continue;
        }
        /* Do something with the string. */
        printf("\033[33mecho: '%s'\033[0m\n", line.data);
        linenoiseHistoryAdd(line.data); /* Add to the history. */
    }

    return 0;
}
