#!/bin/bash
if ! [ -n "$BASH_VERSION" ];then
    echo "this is not bash, calling self with bash....";
    SCRIPT=$(readlink -f "$0")
    /bin/bash $SCRIPT
    exit;
fi

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# Run your own commands here
# for building and deploying your codebase,
# preferably through docker

# Start server in 1280 x 1024 resolution.
tightvncserver :1 -geometry 1280x1024

# Run the selenium server in the background
java -jar selenium-server-standalone-3.8.1.jar -enablePassThrough false &

# Sleep for a sec so that the selenium server has time to initialize
sleep 3

# Run the selenium tests tests
/usr/bin/php myPhpTestsEntryPoint.php

# Stop the selenium and vnc servers
killall java
tightvncserver -kill :1
