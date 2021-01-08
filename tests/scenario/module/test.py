from file_sync_tool import sync

if __name__ == "__main__":
    sync.Sync(
        mute=True,
        config={
            "target": {
            },
            "origin": {
                "host": "www1",
                "user": "user",
                "password": "password"
            },
            "files": {
                "config": [
                    {
                        "origin": "/var/www/html/tests/files/www1/dir1/",
                        "target": "/var/www/html/tests/files/www2/dir1/",
                        "exclude": [
                          "dummy2.file"
                        ]
                    },
                    {
                        "origin": "/var/www/html/tests/files/www1/dir2/",
                        "target": "/var/www/html/tests/files/www2/dir2/",
                        "exclude": [
                            "dummy2.file"
                        ]
                    }
                ]
            }
    })
