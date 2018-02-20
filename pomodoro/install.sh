#!/usr/bin/env bash

sources=$(pwd)

echo -e "#!/bin/sh\npython $sources/pomodorod.py" > /usr/bin/pomodorod
chmod +x /usr/bin/pomodorod

echo -e "#!/bin/sh\npython $sources/pomodoro.py \"\$@\"" > /usr/bin/pomodoro
chmod +x /usr/bin/pomodoro
