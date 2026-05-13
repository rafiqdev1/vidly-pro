#!/bin/bash
echo "🚀 Installing Vidly Pro..."

pkg update -y && pkg upgrade -y
pkg install python ffmpeg -y
pip install -r requirements.txt

chmod +x vidly.py
cp vidly.py $PREFIX/bin/vidly
chmod +x $PREFIX/bin/vidly

echo "✅ Vidly Pro installed successfully!"
echo "Now you can use it anywhere with command: vidly"
echo "Example: vidly https://youtube.com/watch?v=..."
