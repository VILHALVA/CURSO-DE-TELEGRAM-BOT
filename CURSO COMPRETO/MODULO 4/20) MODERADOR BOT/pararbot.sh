ps -ef | grep bot | grep -v grep | awk '{print $2}' | xargs kill -9
