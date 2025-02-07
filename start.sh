#!/usr/bin/bash
source .venv/bin/activate
python -m streamlit run main.py --server.port $PORT