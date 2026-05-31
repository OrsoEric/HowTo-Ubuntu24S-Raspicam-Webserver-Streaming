# create UV

libcamera needs Python 3.12 

first time install UV

## Delete existing venv

```bash
rm -rf .venv
```

## Install UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

source $HOME/.local/bin/env 
```

## Use local cache

export UV_CACHE_DIR="/home/sona/UV_CACHE"

## create and activate venv

```bash
uv venv .venv --python 3.12

source .venv/bin/activate

python --version
```

<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ rm -rf .venv
sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ uv venv .venv --python 3.12
Using CPython 3.12.3 interpreter at: /usr/bin/python3.12
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ source .venv/bin/activate
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ python --version
Python 3.12.3
```

</details>
