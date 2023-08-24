#!python3

import argparse

TEMPLATE_HEAD = """
version: '3.9'
name: tp0
services:
  server:
    container_name: server
    image: server:latest
    entrypoint: python3 /main.py
    environment:
      - PYTHONUNBUFFERED=1
      - LOGGING_LEVEL=DEBUG
    networks:
      - testing_net
"""

CLIENT_TEMPLATE = """
  client{0}:
    container_name: client{0}
    image: client:latest
    entrypoint: /client
    environment:
      - CLI_ID={0}
      - CLI_LOG_LEVEL=DEBUG
    networks:
      - testing_net
    depends_on:
      - server
"""

TEMPLATE_TAIL = """
networks:
  testing_net:
    ipam:
      driver: default
      config:
        - subnet: 172.25.125.0/24
"""

def main():
    parser = argparse.ArgumentParser(description="Generate a docker-compose file with one server and n clients")
    parser.add_argument('-n', '--number', dest="number", type=int, default=1, help='Number of clients to generate. Default: 1')
    parser.add_argument('-f', '--file', dest="file", type=str, default="docker-compose-dev.yaml", help='Output file path. Default: docker-compose-dev.yaml')
    args = parser.parse_args()

    file = args.file
    number = args.number

    if number < 1:
        print("Error: n must be greater than 0")
        exit(1)

    with open(file, "w") as f:
        t = TEMPLATE_HEAD
        for i in range(number):
            t += CLIENT_TEMPLATE.format(i+1)
        t += TEMPLATE_TAIL
        f.write(t)

main()