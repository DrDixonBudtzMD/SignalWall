@echo off
title SignalWall
echo Starting SignalWall on http://localhost:8080
echo.
echo Keep this window open while using SignalWall.
echo Press CTRL+C to stop the server.
echo.
python -m http.server 8080
pause
