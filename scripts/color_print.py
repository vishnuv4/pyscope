from colorama import Fore,Style

def error(string):
    """
    Prints error messages
    """
    print(f"{Fore.RED}ERROR: {string}{Style.RESET_ALL}")

def warning(string):
    """
    Prints warning messages
    """
    print(f"{Fore.YELLOW}WARNING: {string}{Style.RESET_ALL}")