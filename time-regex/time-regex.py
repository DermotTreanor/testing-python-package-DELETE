import re
import time

def show_combined_docs():
    """Show the documentation for both the 're' and 'time' module."""
    print("\033[31m" + re.__doc__ + "\033[0m")
    print("\033[34m" + time.__doc__ + "\033[0m")

def main():
    print("Combining the 're' module with the 'time' module. Here are their descriptions.")

if __name__ == '__main__':
    main()