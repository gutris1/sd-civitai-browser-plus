from modules.shared import opts

do_debug_print = getattr(opts, "civitai_debug_prints", False)

def init():
    import warnings, os, json
    from urllib3.exceptions import InsecureRequestWarning
    warnings.simplefilter('ignore', InsecureRequestWarning)

    config_folder = os.path.join(os.getcwd(), "config_states")
    if not os.path.exists(config_folder):
        os.mkdir(config_folder)

    global download_queue, last_version, cancel_status, recent_model, last_url, json_data, json_info, main_folder, previous_inputs, download_fail, sortNewest, isDownloading, old_download, scan_files, from_update_tab, url_list, print, subfolder_json

    cancel_status = None
    recent_model = None
    json_data = None
    json_info = None
    main_folder = None
    previous_inputs = None
    last_version = None
    url_list = {}
    download_queue = []

    subfolder_json = os.path.join(config_folder, "civitai_subfolders.json")
    if not os.path.exists(subfolder_json):
        with open(subfolder_json, 'w') as json_file:
            json.dump({}, json_file)

    from_update_tab = False
    scan_files = False
    download_fail = False
    sortNewest = False
    isDownloading = False
    old_download = False

RST = '\033[0m'
ORANGE = '\033[38;5;208m'
CYAN = "\033[36m"
GREEN = "\033[38;5;46m"
AR = f'{ORANGE}▶{RST}'
TITLE = f'{CYAN}CivitAI Browser++{RST}:'
DEBUG = f'[{GREEN}DEBUG{RST}]'

_print = print

def print(msg):
    _print(msg if "Image Encryption:" in msg else f'{AR} {TITLE} {msg}')

def debug_print(print_message):
    if do_debug_print:
        _print(f'{DEBUG} {TITLE} {print_message}')