import yaml
import os
from exporters import burp_export, json_export, txt_export
from rich.console import Console

console = Console()

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__),"..", "templates", "cmdinj_templates.yaml")

def load_templates():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def print_cli(payloads, explain=False):
    for p in payloads:
        console.print("═" * 82, style="dim")
        console.print(f"\n[bold cyan]ID:[/bold cyan] {p.get('id')}")
        console.print(f"[bold magenta]Operating System: [/bold magenta] {p.get('os')}")
        console.print(f"[bold yellow]Type:[/bold yellow] {p.get('type')}")
        console.print(f"\n[bold green]Payload:[/bold green]"f"[white] {p.get('payload')}[/white]")
        if explain:
            console.print(f"\n[bold blue]Explanation: [/bold blue]"f"[italic]{p.get('explanation')}[/italic]")
            console.print(f"[bold red]Defensive Notes: [/bold red]"f"[italic]{p.get('defensive_notes')}[/italic]")
        print()

def generate_cmdinj_payloads(module, operating_system, export_format, out_file, explain, encode):

    if encode != "None":
        print("Encode mode not allowed in module Comand-Injection\n")
        exit(0)

    templates = load_templates()
    results = []

    for item in templates:
        
        if operating_system and item.get("os") != operating_system:
            continue

        payload = item.get("payload")
        result = {
            "id": item.get("id"),
            "os": item.get("os"),
            "type": item.get("type"),
            "payload": payload,
        }
        if explain:
            result["explanation"] = item.get("explanation")
            result["defensive_notes"] = item.get("defensive_notes")
        results.append(result)
   
    if export_format == "cli":
        print_cli(results, explain)
        console.print("═" * 82, style="dim")
        print("")
    elif export_format == "json":
        json_export.write(results, out_file)

    elif export_format == "txt":
        txt_export.write(module, results, out_file)

    elif export_format == "burp":
        burp_export.write(results, out_file)
