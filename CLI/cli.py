import argparse
import sys
from rich.console import Console

console = Console()


class CustomHelpFormatter(argparse.RawTextHelpFormatter):
    def format_help(self):
        return super().format_help().rstrip() + "\n\n"


def build_parser():

    examples = """
Usage:

    XSS:
        ./VulnCraft -m xss -c html
            Generate XSS payloads for HTML context

        ./VulnCraft -m xss -c js -e url
            Generate XSS payloads for Javascript context with url encoded
    
    SQLi:
        ./VulnCraft -m sqli -db mysql -t error-based
            Generate SQLI error-based payloads for Mysql Database

        ./VulnCraft -m sqli -db postgresql -t time-based -e url --exp json --o sqli_payloads.json
            Generate SQLI time-based url encoded payloads & save them to a json format file

    Command-Injetion:

        ./VulnCraft -m cmdinj -t linux 
            Generate Command-Injection payloads for Linux Operating System
    """

    parser = argparse.ArgumentParser(
        prog="VulnCraft",
        description="Payload Generator Framework",
        formatter_class=CustomHelpFormatter,
        epilog=examples
    )

    parser.add_argument(
        "--Module",
        "-m",
        choices=["xss", "sqli", "cmdinj"],
        help="Module to generate (required)"
    )

    parser.add_argument(
        "--Context",
        "-c",
        choices=["html", "attribute", "js"],
        help="(XSS) context to target"
    )

    parser.add_argument(
        "--Type",
        "-t",
        choices=[
            "reflected", "stored", "dom",
            "error-based", "union-based",
            "boolean-based", "time-based",
            "linux", "windows"
        ],
        help="(XSS/SQLi/Command Injection) Type/Category/Operating System"
    )

    parser.add_argument(
        "--Database",
        "-db",
        choices=["mysql", "postgresql", "mssql"],
        help="(SQLi) target DB type"
    )

    parser.add_argument(
        "--Encode",
        "-e",
        default="None",
        choices=["url", "base64", "hex"],
        help="Encoding demonstration"
    )

    parser.add_argument(
        "--Obfuscate",
        "-ob",
        default="none",
        choices=["none", "comment-insert", "case-variation", "whitespace", "mixed"],
        help="Obfuscation demonstration"
    )

    parser.add_argument(
        "--Export",
        "-exp",
        default="cli",
        choices=["cli", "json", "txt", "burp"],
        help="Output format"
    )

    parser.add_argument(
        "--Out",
        "-o",
        help="Output file path"
    )

    parser.add_argument(
        "--Explain",
        action="store_true",
        help="Show defensive notes and bypass logic"
    )

    parser.add_argument(
        "--Version",
        "-v",
        action="store_true",
        help="Show tool version"
    )

    return parser
