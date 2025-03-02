import sys
import os
import subprocess
import shutil
from rich.console import Console
from rich.table import Table
from rich.text import Text

# Add parent directory to sys.path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.util import clean_domain_input

console = Console()

def banner():
    console.print("[bold green]=============================================")
    console.print("        hacker.tools.kali - WHOIS Lookup")
    console.print("        Version: v-1.3")
    console.print("        Owner: Yash Tiwari")
    console.print("=============================================[/bold green]\n")

def check_dependencies():
    """Check if the 'whois' command is installed."""
    if not shutil.which("whois"):
        console.print("[bold red][!] 'whois' command not found. Please install it to proceed.[/bold red]")
        sys.exit(1)

def perform_whois_lookup(domain):
    """Perform WHOIS lookup for the given domain using subprocess."""
    try:
        console.print(f"[cyan][*] Performing WHOIS lookup for domain: {domain}[/cyan]")
        result = subprocess.run(["whois", domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
        
        if result.returncode != 0:
            console.print(f"[bold red][!] Failed to perform WHOIS lookup: {result.stderr.strip()}[/bold red]")
            return None
        
        if "Rate limit exceeded" in result.stdout:
            console.print("[bold yellow][!] WHOIS query rate limit exceeded. Try again later.[/bold yellow]")
            return None

        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        console.print(f"[bold red][!] WHOIS lookup timed out for {domain}[/bold red]")
    except FileNotFoundError:
        console.print(f"[bold red][!] 'whois' command not found.[/bold red]")
    except Exception as e:
        console.print(f"[bold red][!] An unexpected error occurred: {e}[/bold red]")
    return None

def display_whois_info(whois_data):
    """Display the WHOIS information in a formatted table."""
    if not whois_data:
        console.print("[bold yellow][!] No WHOIS information found.[/bold yellow]")
        return

    table = Table(show_header=True, header_style="bold white")
    table.add_column("Key", style="bold cyan", justify="left", min_width=20)
    table.add_column("Value", style="white", justify="left", min_width=50)

    # Parsing the WHOIS data and adding it to the table
    for line in whois_data.splitlines():
        if ':' in line:
            parts = line.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip() if len(parts) > 1 else "N/A"
            table.add_row(key, value)

    console.print(table)
    console.print("\n[bold cyan][*] WHOIS lookup completed.[/bold cyan]")

def whois_lookup(target):
    """Perform the WHOIS lookup process for the given target."""
    banner()
    check_dependencies()
    domain = clean_domain_input(target)
    whois_data = perform_whois_lookup(domain)
    display_whois_info(whois_data)

def main(target):
    whois_lookup(target)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        try:
            main(target)
            sys.exit(0)
        except KeyboardInterrupt:
            console.print("\n[bold red][!] Script interrupted by user.[/bold red]")
            sys.exit(0)
        except Exception as e:
            console.print(f"[bold red][!] An unexpected error occurred: {e}[/bold red]")
            sys.exit(1)
    else:
        console.print("[bold red][!] No target provided. Please pass a domain or IP address.[/bold red]")
        sys.exit(1)
