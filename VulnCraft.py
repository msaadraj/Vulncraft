from CLI.cli import build_parser

from modules.xss import generate_xss_payloads
from modules.sqli import generate_sqli_payloads
from modules.cmdinj import generate_cmdinj_payloads

from exporters import (burp_export, json_export, txt_export)
from encoders import (base64, hex, url)
from obfuscation import (comment_insertion, whitespace_abuse)

from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.align import Align

import sys
import pyfiglet
from rich.progress import track, Progress, BarColumn, TextColumn, TimeElapsedColumn
import time
import math

VERSION = "0.1.0"
console = Console()

def main():
    banner = r"""
 __   __  __   __  ___      __    _  _______  ______    _______  _______  _______ 
|  | |  ||  | |  ||   |    |  |  | ||       ||    _ |  |   _   ||       ||       |
|  |_|  ||  | |  ||   |    |   |_| ||       ||   | ||  |  |_|  ||    ___||_     _|
|       ||  |_|  ||   |    |       ||       ||   |_||_ |       ||   |___   |   |  
|       ||       ||   |___ |  _    ||      _||    __  ||       ||    ___|  |   |  
 |     | |       ||       || | |   ||     |_ |   |  | ||   _   ||   |      |   |  
  |___|  |_______||_______||_|  |__||_______||___|  |_||__| |__||___|      |___|  
    """

    def rainbow(text):
        result = ""
        for i, char in enumerate(text):
            r = int(127 * (math.sin(i * 0.1) + 1))
            g = int(127 * (math.sin(i * 0.1 + 2) + 1))
            b = int(127 * (math.sin(i * 0.1 + 4) + 1))
            result += f"\033[38;2;{r};{g};{b}m{char}"
        return result + "\033[0m"

    for line in banner.splitlines():
        print(rainbow(line))

    print()
  
    banner_width = max(len(line) for line in banner.splitlines())

    parser = build_parser()
    args = parser.parse_args()

    if args.Version:
        print(f"VulnCraft version {VERSION} ")
        sys.exit(0)

    items = list(vars(args).items())

    content = ""
    for i, (k, v) in enumerate(items):
        content += f"[bold yellow]{k}:[/bold yellow] {v}"
        
        if i != len(items) - 1:
            content += "\n"


    panel = Panel(
        content,
        title="[bold red]PAYLOAD GENERATOR FRAMEWORK[/bold red]",
        subtitle="[bold yellow]ITSOLERA TEAM THETA | v1.0 [/bold yellow]",
        width=banner_width,
    )
    console.print(panel)
    
    print()
    for task in track(range(10), description="[green][*][/green] Generating Payloads "):
        time.sleep(0.2)
        
    print(" ")
    if args.Module == "xss":
        generate_xss_payloads(args.Module, args.Context, args.Type, args.Encode, args.Obfuscate, args.Export, args.Out, args.Explain)
    if args.Module == "sqli":
        generate_sqli_payloads(args.Module, args.Database, args.Type, args.Encode, args.Obfuscate, args.Export, args.Out, args.Explain)
    if args.Module == "cmdinj":
        generate_cmdinj_payloads(args.Module, args.Type, args.Export, args.Out, args.Explain, args.Encode)


if __name__ == "__main__":
    try:
        main()
    except:
        exit(0)
