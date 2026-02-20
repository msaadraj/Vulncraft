from pathlib import Path
from datetime import datetime
from rich.console import Console

console = Console()

OUTPUTS_DIR = Path("Outputs")
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)


def write(module, results, out_file: str = None):
    if not results:
        raise ValueError("No results provided for TXT export.")
    if not out_file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_file = OUTPUTS_DIR / f"export_{timestamp}.txt"
    else:
        out_file = OUTPUTS_DIR / out_file
    with open(out_file, "w", encoding="utf-8") as f:
        for p in results:
            f.write("=" * 60 + "\n")
            f.write(f"ID: {p.get('id')}\n")

            if module.lower() == "xss":
                f.write(f"Context: {p.get('context')}\n")
                f.write(f"Type: {p.get('type')}\n\n")
            elif module.lower() == "sqli":
                f.write(f"Database: {p.get('db')}\n")
                f.write(f"Category: {p.get('category')}\n\n")

            f.write("Payload:\n")
            f.write(p.get("payload", "") + "\n\n")

            if p.get("explanation"):
                f.write("Explanation:\n")
                f.write(p["explanation"] + "\n\n")

            if p.get("defensive_notes"):
                f.write("Defensive Notes:\n")
                f.write(p["defensive_notes"] + "\n\n")

    console.print(f"[bold green][+][/bold green] TXT export written to [bold yellow]{out_file}[/bold yellow]\n")
