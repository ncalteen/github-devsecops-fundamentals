"""This script has intentional vulnerabilities for testing purposes."""


# This function has a vulnerability.
def vulnerable_function():
    """This function has a vulnerability."""
    # Vulnerability: CWE-78: Improper Neutralization of Special Elements used
    # in an OS Command ('OS Command Injection')
    # https://cwe.mitre.org/data/definitions/78.html
    print("Enter your name: ")
    name = input()
    print("Hello, " + name)
