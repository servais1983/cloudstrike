#!/usr/bin/env python3

import argparse
from core import enum, checker, ai_analyzer
from core.utils import run_script_yaml

def main():
    parser = argparse.ArgumentParser(prog="cloudstrike", description="Pentest Cloud CLI - Kali Linux")
    subparsers = parser.add_subparsers(dest="command")

    enum_cmd = subparsers.add_parser("enum")
    enum_cmd.add_argument("--provider", required=True, choices=["aws", "gcp", "azure"])

    check_cmd = subparsers.add_parser("check")
    check_cmd.add_argument("--provider", required=True)

    ai_cmd = subparsers.add_parser("cloud-ai")
    ai_cmd.add_argument("--provider", required=True)

    run_cmd = subparsers.add_parser("run")
    run_cmd.add_argument("file")

    args = parser.parse_args()

    if args.command == "enum":
        enum.run(args.provider)
    elif args.command == "check":
        checker.run(args.provider)
    elif args.command == "cloud-ai":
        ai_analyzer.run(args.provider)
    elif args.command == "run":
        run_script_yaml(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
