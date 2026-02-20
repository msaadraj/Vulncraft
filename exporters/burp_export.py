from pathlib import Path
from datetime import datetime
from rich.console import Console

console = Console()

OUTPUTS_DIR = Path("Outputs")
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)  


def write(results, out_file: str = None):
    if not results:
        raise ValueError("No results provided for Burp export.")

    if not out_file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_file = OUTPUTS_DIR / f"burp_{timestamp}.txt"
    else:
        out_file = OUTPUTS_DIR / out_file

    with open(out_file, "w", encoding="utf-8") as f:
        for p in results:
            payload = p.get("payload")
            if payload:
                f.write(payload + "\n")
    console.print(f"[bold green][+][/bold green] Burp payload list written to [bold yellow]{out_file}[/bold yellow]\n")

