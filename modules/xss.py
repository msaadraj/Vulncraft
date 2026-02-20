import yaml
import os
from exporters import burp_export, json_export, txt_export
from encoders import base64, hex, url
from obfuscation import comment_insertion, whitespace_abuse
from rich.console import Console

console = Console()


TEMPLATE_PATH = os.path.join(os.path.dirname(__file__),"..", "templates", "xss_templates.yaml")

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
        return comment_insertion.apply(payload)
    if obf_type == "whitespace":
        return whitespace_abuse.apply(payload)
    if obf_type == "mixed":
        payload = comment_insertion.apply(payload)
        payload = whitespace_abuse.apply(payload)
        return payload
    if obf_type == "case-variation":
        exit(0)

    return payload


def print_cli(payloads, explain=False):
    for p in payloads:
        console.print("═" * 82, style="dim")
        console.print(f"\n[bold cyan]ID:[/bold cyan] {p.get('id')}")
        console.print(f"[bold magenta]Context:[/bold magenta] {p.get('context')}")
        console.print(f"[bold yellow]Type:[/bold yellow] {p.get('type')}")
        console.print(f"\n[bold green]Payload: [/bold green][white]{p.get('payload')}[/white]\n")
        if explain:
            console.print(f"[bold blue]Explanation: [/bold blue][italic]{p.get('explanation', '')}[/italic]")
            console.print(f"\n[bold red]Defensive Notes: [/bold red][italic]{p.get('defensive_notes', '')}[/italic]")
            print()

def generate_xss_payloads(module, context, payload_type, encode, obfuscate, export_format, out_file, explain):

    templates = load_templates()
    results = []

    for item in templates:
        if context and item.get("context") != context:
            continue
        if payload_type and item.get("type") != payload_type:
            continue
        
        payload = item.get("payload")
        payload = apply_encoding(payload, encode)
        payload = apply_obfuscation(payload, obfuscate)
        result = {
            "id": item.get("id"),
            "context": item.get("context"),
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
        

