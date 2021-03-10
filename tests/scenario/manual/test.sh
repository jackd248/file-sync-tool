#!/bin/sh

#
# Feature: MANUAL
#
sh helper/cleanup.sh
sh helper/dummy.sh www2

printf "\033[94m[TEST]\033[m Feature: MANUAL"
printf " \033[90m(Sync: WWW2 -> WWW1, Initiator: WWW2)\033[m"

docker-compose exec www2 pip3 install --upgrade -r requirements.txt > /dev/null
docker-compose exec www2 python3 /var/www/html/file_sync_tool -fo /var/www/html/tests/files/www2/dir1/ -ft /var/www/html/tests/files/www1/dir1/ -oh www2 -ou user -opw password -th www1 -tu user -tpw password $1

FILE=./files/www2/dir1/dummyfile
if [ -f "./files/www1/dir1/dummy1.file" ] && [ -f "./files/www1/dir2/dummy1.file" ] && [ ! -f "./files/www1/dir1/dummy2.file" ] && [ ! -f "./files/www1/dir2/dummy2.file" ] && [ -f "./files/www1/dir1/dummy3.file" ] && [ -f "./files/www1/dir2/dummy3.file" ]; then
    echo " \033[92m✔\033[m"
else
    echo " \033[91m✘\033[m"
    exit 1
fi
