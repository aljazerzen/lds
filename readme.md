# LDS

> steem.io commenting bot for posting Bitcoin price

## Requirements

- `python3.6`
- `python3.6-dev`

## Installation

```
$ pip install --upgrade setuptools
$ pip install -r requirements.txt
$ steempy set nodes https://rpc.steemviz.com
$ steempy importaccount yourAccountName
```

## Start

```
$ UNLOCK=walletPassword python main.py
```

If `steampy` it existing with this error: `pkg_resources.ContextualVersionConflict: (toml 0.9.3...`
go to `$PYTHON_HOME/lib/python3.6/site-packages/steem-0.18.103-py3.6.egg-info/require.txt` and 
change `toml==0.9.3.1` to `toml==0.9.3`