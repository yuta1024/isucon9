#!/bin/bash

set -eux

curl -k -XPOST https://127.0.0.1:8080/initialize -H 'Content-Type: application/json' -d @initialize.json
