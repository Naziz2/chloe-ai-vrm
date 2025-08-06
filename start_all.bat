@echo off
REM Start TTS server
start "TTS Server" cmd /k python tts_server\app.py
REM Start frontend (Vite)
start "Frontend" cmd /k npm run dev
