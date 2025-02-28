#!/usr/bin/env python3
""" Generate a list of combining characters from the latest UnicodeData.txt """
import sys
import re
import os
import http.client


def fetch_unicode_data(host, path):
    """ Fetch the Unicode data from the given host and path """
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", path)
    response = conn.getresponse()

    if response.status != 200:
        print(f"Failed to retrieve data: {response.status} {response.reason}")
        sys.exit(1)

    return response.read().decode("utf-8").splitlines()


def replace_region(lines, text, begin_marker, end_marker):
    """ Replace the region between the begin and end markers with the given text """
    results = []
    in_table = False
    for line in lines:
        match = re.match(f".*{begin_marker}.*", line)
        if match:
            in_table = True
            results.append(line)
            results.append(text)
        elif in_table:
            match = re.match(f".*{end_marker}.*", line)
            if match:
                in_table = False
                results.append(line)
            else:
                pass
        else:
            results.append(line)
    return results


def create_wide_char_table(lines):
    """ Create a table of wide characters from the given lines """
    ranges = []
    for line in lines:
        match = re.match(r"^(.*?)(?:\.\.(.*?))?\s+;\s+[FW]\s+# .*$", line)
        if match:
            first = int(match.group(1), 16)
            last = int(match.group(2), 16) if match.group(2) else first
            if ranges and ranges[-1]["l"] + 1 == first:
                ranges[-1]["l"] = last
            else:
                ranges.append({"f": first, "l": last})

    pairs = [f"{{ 0x{r['f']:X}, 0x{r['l']:X} }}" for r in ranges]
    columns = 4
    return (
        ",\n".join(
            [
                "    " + ", ".join(pairs[i : i + columns])
                for i in range(0, len(pairs), columns)
            ]
        )
        + "\n"
    )


def create_combining_char_table(lines):
    """ Create a table of combining characters from the given lines """
    chars = []
    for line in lines:
        match = re.match(r"^(.*);.*;Mn;", line)
        if match:
            chars.append(f"0x{match.group(1)}")

    columns = 8
    return (
        ",\n".join(
            [
                "    " + ", ".join(chars[i : i + columns])
                for i in range(0, len(chars), columns)
            ]
        )
        + "\n"
    )


def generate_wide_char_table(lines):
    """ Generate the wide character table from the given lines """
    table = create_wide_char_table(
        fetch_unicode_data(
            "www.unicode.org", "/Public/UCD/latest/ucd/EastAsianWidth.txt"
        )
    )

    return replace_region(
        lines, table, "BEGIN: WIDE CHAR TABLE", "END: WIDE CHAR TABLE"
    )


def generate_combining_char_table(lines):
    """ Generate the combining character table from the given lines """
    table = create_combining_char_table(
        fetch_unicode_data("www.unicode.org", "/Public/UCD/latest/ucd/UnicodeData.txt")
    )

    return replace_region(
        lines, table, "BEGIN: COMBINING CHAR TABLE", "END: COMBINING CHAR TABLE"
    )


def main():
    """ Main function """
    path = f"{os.path.dirname(os.path.abspath(__file__))}/../linenoise.cpp"

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = generate_wide_char_table(lines)
    lines = generate_combining_char_table(lines)

    with open(path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)


if __name__ == "__main__":
    main()
