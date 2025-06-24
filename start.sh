#!/bin/bash

# Use default port if not set
PORT=${PORT:-10000}

# Run rembg server on the correct port
exec rembg s --host 0.0.0.0 --port $PORT --log-level info
