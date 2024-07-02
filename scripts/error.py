import sys
from colorama import Fore,Style

def fatal(string):
    """
    Prints error messages
    """
    print(f"{Fore.RED}ERROR: {string}{Style.RESET_ALL}")
    sys.exit()

def warning(string):
    """
    Prints warning messages
    """
    print(f"{Fore.YELLOW}WARNING: {string}{Style.RESET_ALL}")