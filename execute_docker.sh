#!/bin/bash
docker stop mosquitto
docker rm mosquitto
docker run -itd --name="mosquitto"  -p 1883:1883 -p 9001:9001 -v /Users/alexandretk/Desktop/UNB/pi_2/sunflower_broker_and_control/docker_volume/data:/mosquitto/data -v /Users/alexandretk/Desktop/UNB/pi_2/sunflower_broker_and_control/docker_volume/log:/mosquitto/log -v /Users/alexandretk/Desktop/UNB/pi_2/sunflower_broker_and_control/docker_volume/config:/mosquitto/config/ eclipse-mosquitto
