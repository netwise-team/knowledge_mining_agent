# Ouroboros + synthadoc bootstrapping script
import os
import sys
import json
import time
import requests
from pathlib import Path
from datetime import datetime


BASE_URL = 'http://localhost:8765'

# Set up Synthadoc
def synthadoc_setup():
    print('=' * 50, ' START SYNTADOC SETUP ', '=' * 50)
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

    os.makedirs(wikis_path.parent, exist_ok=True)
    with open(wikis_path, 'w', encoding='utf8') as global_config_file_w:
        json.dump(global_config, global_config_file_w)

    os.system('synthadoc serve -w pm-wiki --background')
    print('=' * 50, ' SYNTHADOC CONFIG SET ', '=' * 50)

# Set up MCP connection
def mcp_setup():
    server_config = {
        "id": "synthadoc",
        "name": "synthadoc",
        "enabled": True,
        "transport": "sse",
        "url": "http://localhost:7070/mcp/sse",
        "auth_header": "Authorization",
        "auth_token": "",
        "allowed_tools": []
    }

    mcp_config_resp = requests.get(f'{BASE_URL}/api/settings')
    if mcp_config_resp.status_code != 200:
        print('Failed to fetch current settings. Is Ouroboros running?')
        return True

    mcp_config = mcp_config_resp.json()['MCP_SERVERS']
    mcp_config.append(server_config)

    payload = {'MCP_SERVERS': mcp_config}
    set_mcp_server_resp = requests.post(f'{BASE_URL}/api/settings', json=payload)
    if set_mcp_server_resp.status_code == 200:
        print('Syntadoc MCP setup complete')
    else:
        print(set_mcp_server_resp.json()['error'])
        return True
    enable_mcp_clint_resp = requests.post(f'{BASE_URL}/api/settings', json={"MCP_ENABLED": True})
    if enable_mcp_clint_resp.status_code == 200:
        print('MCP Client enabled')
    else:
        print(f"Error enabling MCP client: {enable_mcp_clint_resp.json()['error']}")
        return True
    
    print('=' * 50, ' SYNTHADOC MCP ONLINE ', '=' * 50)
    return False
          
# Enable skills
def enable_skills():

    skills_route = Path('skills').resolve()

    set_repo_resp = requests.post(f'{BASE_URL}/api/settings', json={'OUROBOROS_SKILLS_REPO_PATH': str(skills_route)})

    if set_repo_resp.status_code != 200:
        print('Failed to set repo path. Is Ouroboros enabled?')
        return True
    
    print('=' * 50, ' SKILLS INSTALLED ', '=' * 50) 

    resp = requests.post(f"{BASE_URL}/api/tasks", json={
        "message": "Install, review and enable all of skills you found. IF there are any blockers - fix it.",
        "title": "Skill enabling",
        "description": "Skill enabling"
    })
    if resp.status_code == 200:
        task_id = resp.json()["task_id"]
    else:
        print(f'Error setting task for skill enabling. Error message: {resp.json()["error"]}')
        return True

    while True:
        resp = requests.get(f'{BASE_URL}/api/tasks/{task_id}')
        if resp.json()['status'] == 'running':
            print('Current status: ' + resp.json()['status'])
            time.sleep(5)
        elif resp.json()['status'] == 'failed':
            print('=' * 50, ' FAILED TO ENABLE SKILLS ', '=' * 50)
            return True
        else:
            tg_token = input("Skills installation launched successfully. Input Telegram token: ")
            requests.post(f"{BASE_URL}/api/settings", json={"TELEGRAM_BOT_TOKEN": f"{tg_token}" })
            print('=' * 50, ' SKILLS ENABLED ', '=' * 50) 
            return False

if __name__ == '__main__':
     # Ensure we are runnging script from venv
    try:
        assert 'venv' in sys.executable
    except AssertionError:
        print('Venv not found. Please run the script from venv.')
        sys.exit(1)
    
    if not os.getenv('OPENAI_API_KEY'):
        print('OpenAI key is not set. Please set OPENAI_API_KEY before bootstrapping. Shutting down...')
        sys.exit(1)
    
    ops = [synthadoc_setup, mcp_setup, enable_skills]

    GREETING = """
Welcome to Knowledge Mining Agent bootstrap utility!
Choose operation:
1. Setup Sythadoc
2. Add Syntadoc MCP server
3. Enable skills
4. Do a full bootstrap
0. Exit
    """
    print(GREETING)
    while True:
        choice = input('Choose next action: ')

        if choice not in '12340' or len(choice) != 1:
            print('Wrong action. Try again.')
            continue
        
        if choice == '4':
            for op in ops:
                op()
        elif choice == '0':
            print('Exiting...')
            sys.exit(0)
        else:
            ops[int(choice) - 1]()
