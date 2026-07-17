# Ouroboros + synthadoc bootstrapping script
# Installs and reviews provided skills +
# Sets up MCP connection +
# Sets up synthadoc engine and wiki +
import os
import sys
import json
import time
import shutil
import requests
from pathlib import Path
from datetime import datetime

BASE_URL = 'http://localhost:8765'
OUROBOROS_APP_ROOT = Path.home() / 'Ouroboros'

# Ensure we are runnging script from venv
try:
    assert 'venv' in sys.executable
except AssertionError:
    print('Venv not found. Please run the script from venv.')
    sys.exit(1)


print('=' * 50, ' BOOTSTRAP START ', '=' * 50)
# Copy skills into Ouroboros skills folder
src = Path("skills")
dst = OUROBOROS_APP_ROOT / "data" / "skills" / "external"

for item in src.iterdir():
    target = dst / item.name
    print(f'Copying {target.name}...')

    if item.is_dir():
        shutil.copytree(item, target, dirs_exist_ok=True)
    else:
        shutil.copy2(item, target)

print('=' * 50, ' SKILLS COPIED ', '=' * 50)

# Set up Synthadoc
# Prepare config
provider = input('Input provider (openrouter/cloudru): ')
model = input('Input model: ')

if provider not in ('openrouter', 'cloudru'):
    raise ValueError('Invalid provider')

FMT_DICT = {
    'mdl': model,
    'prvdr': 'openai',
    'burl':'https://foundation-models.api.cloud.ru/v1' if provider == 'cloudru' else 'https://openrouter.ai/api/v1'
}

with open('wiki-config.toml.example', 'r', encoding='utf8') as f:
    config = f.read()

config_folder = Path('wikis/pm-wiki/.synthadoc')
config_folder.mkdir(exist_ok=True)

full_config_path = config_folder / Path('config.toml')

with open(full_config_path, 'w+', encoding='utf8') as configfile:
    configfile.write(config.format(**FMT_DICT))

global_config_entry = {
    "path": str(Path(os.getcwd()).joinpath('wikis', 'pm-wiki')),
    "demo": "null",
    "installed": datetime.strftime(datetime.now(), '%d-%m-%Y'),
    "port": 7070
}

wikis_path = Path.home().joinpath('.synthadoc', 'wikis.json')

if wikis_path.exists() and not wikis_path.stat().st_size == 0:
    with open(wikis_path, 'r', encoding='utf8') as global_config_file_r:
        global_config = json.load(global_config_file_r)
else:
    global_config = {}

global_config['pm-wiki'] = global_config_entry

with open(wikis_path, 'w', encoding='utf8') as global_config_file_w:
    json.dump(global_config, global_config_file_w)

os.system('synthadoc serve -w pm-wiki --background')

print('=' * 50, ' SYNTHADOC CONFIG SET ', '=' * 50)

# Set up MCP connection
server_config = [
    {
      "id": "synthadoc",
      "name": "synthadoc",
      "enabled": True,
      "transport": "sse",
      "url": "http://localhost:7070/mcp/sse",
      "auth_header": "Authorization",
      "auth_token": "",
      "allowed_tools": []
    }
]
mcp_config_path = OUROBOROS_APP_ROOT.joinpath('data', 'settings.json')
if mcp_config_path.exists() and not mcp_config_path.stat().st_size == 0:
    with open(mcp_config_path, 'r', encoding='utf8') as mcp_config_file_r:
        mcp_config = json.load(mcp_config_file_r)
else:
    mcp_config = {}

mcp_config['MCP_SERVERS'] = server_config

with open(mcp_config_path, 'w', encoding='utf8') as mcp_config_file_w:
    json.dump(mcp_config, mcp_config_file_w, ensure_ascii=False, indent=4)

print('=' * 50, ' SYNTHADOC MCP SET ', '=' * 50)
          
# Enable skills
resp = requests.post(f"{BASE_URL}/api/tasks", json={
    "message": "Install and enable all of skills",
    "title": "Skill enabling",
    "description": "Skill enabling"
})
if resp.status_code == 200:
    task_id = resp.json()["task_id"]
else:
    print(f'Error setting task for skill enabling. Error message: {resp.json()["error"]}')
    sys.exit(1)

while True:
    resp = requests.get(f'{BASE_URL}/api/tasks/{task_id}')
    if resp.json()['status'] == 'running':
        print('Current status: ' + resp.json()['status'])
        time.sleep(5)
    elif resp.json()['status'] == 'failed':
        print('=' * 50, ' FAILED TO INSTALL SKILLS ', '=' * 50)
        sys.exit(1)
    else:
        tg_token = input("Input tg token: ")
        requests.post(f"{BASE_URL}/api/settings", json={"TELEGRAM_BOT_TOKEN": "tg_token" })
        print('=' * 50, ' SETUP COMPLETE ', '=' * 50) 
        sys.exit(0)