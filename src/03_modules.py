"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("\nsys.argv arguments: \n", "\n".join(sys.argv))

# Print out the OS platform you're using:
# YOUR CODE HERE
print("\nOS platform:\n", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("\nPython version:\n",sys.version_info)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("\nProcess ID:\n",os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("\nCurrent Working Directory:\n",os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("\nCurrent User Logged In:\n",os.getlogin())