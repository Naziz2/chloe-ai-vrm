#!/bin/bash
echo "Static site deployment - no build needed"
echo "Files in current directory:"
ls -la
echo "Checking for demo.html:"
if [ -f "demo.html" ]; then
    echo "✓ demo.html found"
else
    echo "✗ demo.html not found"
    exit 1
fi
echo "Deployment ready!"
