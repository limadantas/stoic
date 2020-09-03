#!/bin/bash
while :
do
    noise=$(bc -l <<< "$RANDOM*0.0018+10")
    noise=$(echo $noise | awk '{print int($1)}')
    url="http://34.71.110.167:7896/iot/d?k=4jggokgpepnvsb2uv4s40d59ov&i=db_db001&d=noise|$noise"
    echo "Random noise: ${noise} - ${url}"
    curl --silent --output /dev/null -v --header "Connection: keep-alive" $url
	sleep 0.5
done
