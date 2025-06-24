from urllib3.exceptions import InsecureRequestWarning
from modules.paths_internal import config_states_dir
from modules.shared import opts
from pathlib import Path
import datetime
import warnings
import json
import os

def init():    
    warnings.simplefilter('ignore', InsecureRequestWarning)
    Path(config_states_dir).mkdir(exist_ok=True)

    global download_queue, last_version, cancel_status, recent_model, last_url, json_data, json_info, main_folder, previous_inputs, download_fail, sortNewest, isDownloading, old_download, scan_files, from_update_tab, url_list, _print, subfolder_json

    cancel_status = None
    recent_model = None
    json_data = None
    json_info = None
    main_folder = None
    previous_inputs = None
    last_version = None
    url_list = {}
    download_queue = []

    subfolder_json = Path(config_states_dir) / 'civitai_subfolders.json'
    C = 'created_at'
    if not subfolder_json.exists():
        data = {C: datetime.datetime.now().timestamp()}
        subfolder_json.write_text(json.dumps(data, indent=4), encoding='utf-8')
    else:
        data = json.loads(subfolder_json.read_text(encoding='utf-8'))
        if C not in data:
            data[C] = datetime.datetime.now().timestamp()
            subfolder_json.write_text(json.dumps(data, indent=4), encoding='utf-8')

    from_update_tab = False
    scan_files = False
    download_fail = False
    sortNewest = False
    isDownloading = False
    old_download = False

RST = '\033[0m'
ORANGE = '\033[38;5;208m'
RED = '\033[38;5;196m'
CYAN = "\033[36m"
BLUE = '\033[38;5;39m'
GREEN = "\033[38;5;46m"
AR = f'{ORANGE}▶{RST}'
TITLE = f'{CYAN}CivitAI Browser++{RST}:'
DEBUG = f'[{GREEN}DEBUG{RST}]'

do_debug_print = getattr(opts, 'civitai_debug_prints', False)

def debug_print(print_message):
    if do_debug_print: print(f'{DEBUG} {TITLE} {print_message}')

def _print(msg):
    print(msg if 'Image Encryption:' in msg else f'{AR} {TITLE} {msg}')