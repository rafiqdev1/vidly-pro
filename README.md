# 🔥 Vidly Pro

**Advanced Media Downloader CLI for Termux**

---

![Banner](https://via.placeholder.com/800x200/FF4500/FFFFFF?text=Vidly+Pro) <!-- Replace with your banner later -->

**Vidly Pro** ek powerful aur user-friendly CLI tool hai jo Termux mein best experience deta hai. YouTube, Instagram, Facebook, TikTok aur bohot saare platforms se high-quality videos aur audio download karo.

## ✨ Features

- **Beautiful Banner Interface** with 🔥 flame animation
- **Video + Audio (MP3)** Download support
- **Quality Selection** — Best, 1080p, 720p, 480p etc.
- **Custom Output Folder** support
- **Playlist Support**
- **Fast & Reliable** downloading
- **Lightweight & Optimized** for Termux
- **Progress Bar** with ETA
- **Metadata** embedding (Title, Thumbnail, etc.)

## 🛠️ Technologies

![Termux](https://img.shields.io/badge/Termux-Compatible-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![CLI](https://img.shields.io/badge/CLI-Tool-blue)

## 📥 Installation

```bash
# Termux mein ye commands run karo:

pkg update && pkg upgrade -y
pkg install python git ffmpeg -y
pip install yt-dlp rich

git clone https://github.com/rafiqdev1/vic.git
cd vic
pip install -r requirements.txt

# Run karne ke liye
python vidly.py
