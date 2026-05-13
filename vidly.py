#!/usr/bin/env python3
"""
Vidly Pro - Advanced Media Downloader for Termux
"""

import argparse
import os
import sys
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
import yt_dlp

console = Console()

def show_banner():
    console.print("[bold green]============================================================[/bold green]")
    console.print("[bold green]                 VIDLY PRO v1.0[/bold green]")
    console.print("[bold green]       Advanced Media Downloader for Termux[/bold green]")
    console.print("[bold green]============================================================[/bold green]\n")

def download(url, quality="best", output="Downloads", audio_only=False):
    os.makedirs(output, exist_ok=True)
    
    ydl_opts = {
        'outtmpl': f'{output}/%(title)s.%(ext)s',
        'quiet': False,
    }
    
    if audio_only:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}],
        })
    elif quality == "720":
        ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best'
    elif quality == "1080":
        ydl_opts['format'] = 'bestvideo[height<=1080]+bestaudio/best'
    
    try:
        with Progress(SpinnerColumn(), TextColumn("[cyan]{task.description}")) as progress:
            progress.add_task("Downloading...", total=None)
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        
        console.print("[bold green]✅ Download Completed Successfully![/bold green]")
    except Exception as e:
        console.print(f"[bold red]❌ Error: {e}[/bold red]")

def main():
    show_banner()
    
    parser = argparse.ArgumentParser(description="Vidly Pro - Advanced Media Downloader")
    parser.add_argument("url", nargs="?", help="YouTube or supported site URL")
    parser.add_argument("-q", "--quality", choices=["best", "1080", "720"], default="best", help="Video quality")
    parser.add_argument("-a", "--audio", action="store_true", help="Download audio only (MP3)")
    parser.add_argument("-o", "--output", default="Downloads", help="Output directory")
    
    args = parser.parse_args()
    
    if not args.url:
        parser.print_help()
        sys.exit(1)
    
    download(args.url, args.quality, args.output, args.audio)

if __name__ == "__main__":
    main()
