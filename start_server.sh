#!/bin/bash
# Legacy script — use deploy.py instead
exec python3 "$(dirname "$0")/deploy.py" ${1:-80}
