# file sync tool

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/file_sync_tool-kmi)
![PyPI](https://img.shields.io/pypi/v/file_sync_tool-kmi)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/jackd248/file-sync-tool/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/jackd248/file-sync-tool/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/jackd248/file-sync-tool/badges/build.png?b=master)](https://scrutinizer-ci.com/g/jackd248/file-sync-tool/build-status/master)

Python script to synchronize files from an origin to a target system using [rsync](https://linux.die.net/man/1/rsync).

This tool is an addon of the [db-sync-tool](https://github.com/jackd248/db-sync-tool).

## Installation

### Prerequisite

The script needs python __3.5__ or higher. It is necessary for some additional functionalities to have [pip](https://pypi.org/project/pip/) installed on your local machine. 

<a name="install-pip"></a>
### pip
The library can be installed from [PyPI](https://pypi.org/):
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

For further information see the documentation of the [db-sync-tool](https://github.com/jackd248/db-sync-tool).

## Usage

### Command line

Run the python script via command line.

Installed via [pip](#install-pip):
```bash
$ python3 file_sync_tool
```

Installed via [composer](#install-composer):
```bash
$ python3 vendor/kmi/file-sync-tool/file_sync_tool
```

<a name="shell-arguments"></a>
#### Shell arguments

```bash
usage: file_sync_tool [-h] [-f CONFIG_FILE] [-v] [-m] [-o HOST_FILE]

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
```

If you haven't declare a path to a SSH key, during the script execution you are requested to enter the SSH password for the given user in the shell argument or the `config.json` to enable a SSH connection for the remote system. 

### Import

You can import the python package and use them inside your project:

```python
from file_sync_tool import sync

if __name__ == "__main__":
    sync.Sync(config={}, args*)
```

## Build

The packaging process of the python module is described on [python.org](https://packaging.python.org/tutorials/packaging-projects/).

## Tests

A docker container set up is available for testing purpose. See [here](tests/README.md).