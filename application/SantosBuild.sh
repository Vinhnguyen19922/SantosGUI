#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo $DIR

pyinstaller $DIR/app.spec
chmod 777 $DIR/dist/app

echo “[Press any button to exit]”
read -rsn1
exit