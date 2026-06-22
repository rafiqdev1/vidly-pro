#!/usr/bin/env python3
"""
Vidly Pro - Advanced Media Downloader for Termux
"""

import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
from rich import print as rprint
import yt_dlp

console = Console()

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear()
    text = """
    🔥🔥🔥   V I D L Y   P R O   🔥🔥🔥
          Advanced Media Downloader
    """
    console.print(Panel.fit(text, style="bold red", border_style="yellow"))
    rprint("             [bold cyan]Termux Edition[/bold cyan]\n")

def get_format(choice: int):
    formats = {
        1: "bestvideo+bestaudio/best",
        2: "bestvideo[height<=1080]+bestaudio/best",
        3: "bestvideo[height<=720]+bestaudio/best",
        4: "bestvideo[height<=480]+bestaudio/best",
        5: "bestaudio/best"
    }
    return formats.get(choice, "bestvideo+bestaudio/best")

def download(url: str, quality: int, folder: str):
    try:
        os.makedirs(folder, exist_ok=True)

        opts = {
            'format': get_format(quality),
            'outtmpl': f'{folder}/%(title)s.%(ext)s',
            'quiet': False,
            'no_warnings': True,
            'noplaylist': False,
            'postprocessors': []
        }

        if quality == 5:
            opts['postprocessors'].append({
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            })
        else:
            opts['postprocessors'].append({'key': 'FFmpegMetadata'})

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeRemainingColumn(),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Downloading...", total=None)

            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)

            progress.update(task, completed=100)

        rprint(f"\n[bold green]✅ Download Completed![/bold green]")
        if info and 'title' in info:
            rprint(f"[bold white]🎬 {info['title']}[/bold white]")
        rprint(f"[bold yellow]📁 Saved in: {folder}[/bold yellow]")

    except Exception as e:
        rprint(f"[bold red]❌ Error: {e}[/bold red]")

def main():
    while True:
        banner()
        rprint("[bold magenta]1.[/] Download Video / Playlist")
        rprint("[bold magenta]2.[/] Exit\n")

        choice = Prompt.ask("[bold cyan]Select option[/bold cyan]", choices=["1", "2"], default="1")

        if choice == "2":
            rprint("[bold red]Thank you for using Vidly Pro! 👋[/bold red]")
            break

        url = Prompt.ask("[bold green]Paste URL[/bold green]")

        rprint("\n[bold yellow]Quality:[/bold yellow]")
        rprint("1. Best Quality")
        rprint("2. 1080p")
        rprint("3. 720p")
        rprint("4. 480p")
        rprint("5. Audio Only (MP3)")

        q = IntPrompt.ask("Choose quality", default=1)
        folder = Prompt.ask("Save to folder", default="Vidly_Downloads")

        rprint(f"\n[bold blue]Starting download...[/bold blue]\n")
        download(url, q, folder)

        input("\nPress Enter for next download...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        rprint("\n[bold red]Cancelled.[/bold red]")
    except Exception as e:
        rprint(f"[bold red]Error: {e}[/bold red]")
