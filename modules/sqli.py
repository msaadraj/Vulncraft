import yaml
import os
from exporters import burp_export, json_export, txt_export
from encoders import base64, hex, url
from obfuscation import comment_insertion, whitespace_abuse
from obfuscation import case_variation
from rich.console import Console

console = Console()
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__),"..", "templates", "sqli_templates.yaml")

def load_templates():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def apply_encoding(payload, encode_type):
    if encode_type == "url":
        return url.encode(payload)
    if encode_type == "base64":
        return base64.encode(payload)
    if encode_type == "hex":
        return hex.encode(payload)
    return payload

def apply_obfuscation(payload, obf_type):
    if obf_type == "comment-insert":
        payload = comment_insertion.apply(payload)
        return payload
    if obf_type == "case-variation":
        payload = case_variation.apply(payload)
        return payload
    if obf_type == "mixed":
        payload = case_variation.apply(payload)
        payload = comment_insertion.apply(payload)
        return payload
    if obf_type == "whitespace":
        print("Obfuscation mode Whitespace not allowed in module SQLi")
        exit(0)
    return payload

def print_cli(payloads, explain=False):
    for p in payloads:
        console.print("═" * 82, style="dim")
        console.print(f"\n[bold cyan]ID:[/bold cyan] {p.get('id')}")
        console.print(f"[bold magenta]Database:[/bold magenta] {p.get('db')}")
        console.print(f"[bold yellow]Category:[/bold yellow] {p.get('category')}")
        console.print(f"\n[bold green]Payload:[/bold green]"f"[white] {p.get('payload')}[/white]\n")
        if explain:
            console.print(f"[bold blue]Explanation: [/bold blue]"f"[italic]{p.get('explanation', '')}[/italic]")
            console.print(f"\n[bold red]Defensive Notes: [/bold red]"f"[italic]{p.get('defensive_notes', '')}[/italic]")
            print()
    
def generate_sqli_payloads(module, database_type, category, encode, obfuscate, export_format, out_file, explain):

    templates = load_templates()
    results = []

    for item in templates:
        if database_type and item.get("db") != database_type:
            continue
        if category and item.get("category") != category:
            continue
        payload = item.get("payload")
        payload = apply_encoding(payload, encode)
        payload = apply_obfuscation(payload, obfuscate)
        result = {
            "id": item.get("id"),
            "db": item.get("db"),
            "category": item.get("category"),
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
