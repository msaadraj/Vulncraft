import json
from pathlib import Path
from datetime import datetime
from rich.console import Console

console = Console()

OUTPUTS_DIR = Path("Outputs")
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)  


def write(results, out_file: str = None):
    if results is None:
        raise ValueError("No results provided for JSON export.")
    if not out_file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_file = OUTPUTS_DIR / f"export_{timestamp}.json"
    else:
        out_file = OUTPUTS_DIR / out_file
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    console.print(f"[bold green][+][/bold green] JSON export written to [bold yellow]{out_file}[/bold yellow]\n")
