#!/usr/bin/env python3
"""
Vidly Pro - Advanced Media Downloader for Termux
"""

import argparse
import os
import sys
import yt_dlp

def show_banner():
    print("=" * 60)
    print("              VIDLY PRO v1.0")
    print("     Advanced Media Downloader for Termux")
    print("=" * 60)
    print()

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
    
    print(f"\nDownloading: {url}")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Download Completed Successfully!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

def main():
    show_banner()
    
    parser = argparse.ArgumentParser(description="Vidly Pro")
    parser.add_argument("url", nargs="?", help="Video URL")
    parser.add_argument("-q", "--quality", choices=["best", "1080", "720"], default="best")
    parser.add_argument("-a", "--audio", action="store_true", help="Audio only")
    parser.add_argument("-o", "--output", default="Downloads")
    
    args = parser.parse_args()
    
    if not args.url:
        parser.print_help()
        sys.exit(1)
    
    download(args.url, args.quality, args.output, args.audio)

if __name__ == "__main__":
    main()
