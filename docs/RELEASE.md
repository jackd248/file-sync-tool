# Release Guide

To release a new version of the script, the following steps are necessary:

1. Update the [Changelog](../CHANGELOG.md)
2. Increase the application version according the [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
   
    - Update the `__version__` in [`file_sync_tool/info.py`](../file_sync_tool/info.py)
    - Update the `"version"` in [`composer.json`](../composer.json)
3. Generate a new distribution archive (see [python.org](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives))
   
    - _Optionally_: install the latest version of `setuptools` and `wheel`:
    ```bash
    $ python3 -m pip install --user --upgrade setuptools wheel 
   ```
   - Generate the archive:
    ```bash
    $ python3 setup.py sdist bdist_wheel 
   ```
4. Upload the distribution archive to [pypi.org](https://pypi.org/) (see [python.org](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives))
   
    - _Optionally_: install `twine` for the upload:
    ```bash
    $ python3 -m pip install --user --upgrade twine 
   ```
   - Upload the archive:
    ```bash
    $ python3 -m twine upload dist/*
   ```
5. Create a new Git Tag with the new version
   
    ```bash
    $ git tag v1.4
   ```
6. Push the commit to the [github repository](https://github.com/jackd248/file-sync-tool)
7. The package is now available via [pypi.org](https://pypi.org/project/file-sync-tool-kmi/) and [packagist](https://packagist.org/packages/kmi/file-sync-tool)