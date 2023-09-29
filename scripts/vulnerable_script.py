"""This script has intentional vulnerabilities for testing purposes."""


# This function accepts an arbitrary regular expression and uses it to
# search for a pattern in a string. It returns the first match object
# found.
def search(pattern, string):
    import re

    return re.search(pattern, string)
