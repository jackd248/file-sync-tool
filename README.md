# file sync tool

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/file_sync_tool-kmi)
![PyPI](https://img.shields.io/pypi/v/file_sync_tool-kmi)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/jackd248/file-sync-tool/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/jackd248/file-sync-tool/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/jackd248/file-sync-tool/badges/build.png?b=master)](https://scrutinizer-ci.com/g/jackd248/file-sync-tool/build-status/master)

Python script to synchronize files from an origin to a target system using [rsync](https://linux.die.net/man/1/rsync).

This tool is an addon of the [db-sync-tool](https://github.com/jackd248/db-sync-tool).

![Example receiver](docs/images/file-sync-tool-example-receiver.gif)

## Installation

### Prerequisite

The script needs [python](https://python.org/) __3.5__ or higher. It is necessary for some additional functionalities to have [pip](https://pypi.org/project/pip/) installed on your local machine. 

<a name="install-pip"></a>
### pip
The library can be installed from [PyPI](https://pypi.org/project/file-sync-tool-kmi/):
```bash
$ pip3 install file-sync-tool-kmi
```

<a name="install-composer"></a>
### composer
The script is also available via [packagist.org](https://packagist.org/packages/kmi/file-sync-tool) using composer:

```bash
$ composer require kmi/file-sync-tool
```

Additionally install the python requirements via the following pip command:

````bash
$ pip3 install -e vendor/kmi/file-sync-tool/
````

## Configuration

You can configure the script with [shell arguments](#shell-arguments) or using a separate configuration file.

### Configuration File

The `config.json` contains important information about the origin and the target system. 

Example structure of `config.json` in receiver mode :
```json
{
  "target": {},
  "origin": {
    "host": "ssh_host",
    "user": "ssh_user"
  },
  "files": {
    "config": [
      {
        "origin": "/var/www/html/files/",
        "target": "/var/www/html/files/",
        "exclude": [
          "*.log"
        ]
      }
    ]
  }
}
```

### Documentation

Extend the `config.json` with a `files` section containing multiple transfer entries within the `config`entry. Therefore you have to specify the `origin` source path as well as the `target` destination path of the file sync. Additionally define the rsync `exclude`s for this specific transfer.

In the `config` entry you can also define additional rsync `option`s as a list overwriting the default options.

For further information see the documentation of the [db-sync-tool](https://github.com/jackd248/db-sync-tool).

## Usage

### Command line

Run the python script via command line.

Installed via [pip](#install-pip):
```bash
$ file_sync_tool
```

Installed via [composer](#install-composer):
```bash
$ python3 vendor/kmi/file-sync-tool/file_sync_tool
```

<a name="shell-arguments"></a>
#### Shell arguments

```bash
usage: file_sync_tool [-h] [-f CONFIG_FILE] [-v] [-m] [-o HOST_FILE]
                      [-th TARGET_HOST] [-tu TARGET_USER]
                      [-tpw TARGET_PASSWORD] [-tk TARGET_KEY]
                      [-tpo TARGET_PORT] [-oh ORIGIN_HOST] [-ou ORIGIN_USER]
                      [-opw ORIGIN_PASSWORD] [-ok ORIGIN_KEY]
                      [-opo ORIGIN_PORT] [-fo FILES_ORIGIN] [-ft FILES_TARGET]
                      [-fe FILES_EXCLUDE] [-fop FILES_OPTION]

A tool for automatic file synchronization from and to host systems.

optional arguments:
  -h, --help            show this help message and exit
  -f CONFIG_FILE, --config-file CONFIG_FILE
                        Path to configuration file
  -v, --verbose         Enable extended console output
  -m, --mute            Mute console output
  -o HOST_FILE, --host-file HOST_FILE
                        Using an additional hosts file for merging hosts
                        information with the configuration file
  -th TARGET_HOST, --target-host TARGET_HOST
                        SSH host to target system
  -tu TARGET_USER, --target-user TARGET_USER
                        SSH user for target system
  -tpw TARGET_PASSWORD, --target-password TARGET_PASSWORD
                        SSH password for target system
  -tk TARGET_KEY, --target-key TARGET_KEY
                        File path to SSH key for target system
  -tpo TARGET_PORT, --target-port TARGET_PORT
                        SSH port for target system
  -oh ORIGIN_HOST, --origin-host ORIGIN_HOST
                        SSH host to origin system
  -ou ORIGIN_USER, --origin-user ORIGIN_USER
                        SSH user for origin system
  -opw ORIGIN_PASSWORD, --origin-password ORIGIN_PASSWORD
                        SSH password for origin system
  -ok ORIGIN_KEY, --origin-key ORIGIN_KEY
                        File path to SSH key for origin system
  -opo ORIGIN_PORT, --origin-port ORIGIN_PORT
                        SSH port for origin system
  -fo FILES_ORIGIN, --files-origin FILES_ORIGIN
                        File path for origin source of file sync
  -ft FILES_TARGET, --files-target FILES_TARGET
                        File path for target destination of file sync
  -fe FILES_EXCLUDE, --files-exclude FILES_EXCLUDE
                        Excludes for file sync
  -fop FILES_OPTION, --files-option FILES_OPTION
                        Additional rsync options
```

If you haven't declare a path to a SSH key, during the script execution you are requested to enter the SSH password for the given user in the shell argument or the `config.json` to enable a SSH connection for the remote system. 

### Import

You can import the python package and use them inside your project:

```python
from file_sync_tool import sync

if __name__ == "__main__":
    sync.Sync(config={}, args*)
```

## Release Guide

A detailed guide is available to release a new version. See [here](docs/RELEASE.md).

## Tests

A docker container set up is available for testing purpose. See [here](tests/README.md).