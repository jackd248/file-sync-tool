#!/bin/sh

#
# Sync mode: SYNC_LOCAL
#
sh helper/cleanup.sh
sh helper/dummy.sh www1

printf "\033[94m[TEST]\033[m Sync mode: SYNC_LOCAL"
printf " \033[90m(Sync: WWW2 -> WWW2, Initiator: WWW2)\033[m"

docker-compose exec www2 pip3 install --upgrade -r requirements.txt > /dev/null
docker-compose exec www2 python3 /var/www/html/file_sync_tool -f /var/www/html/tests/scenario/sync_local/sync-local-to-local.json $1

if [ -f "./files/www2/dir1/dummy1.file" ] && [ -f "./files/www2/dir2/dummy1.file" ] && [ ! -f "./files/www2/dir1/dummy2.file" ] && [ ! -f "./files/www2/dir2/dummy2.file" ] && [ -f "./files/www2/dir1/dummy3.file" ] && [ -f "./files/www2/dir2/dummy3.file" ]; then
    echo " \033[92m✔\033[m"
else
    echo " \033[91m✘\033[m"
    exit 1
fi