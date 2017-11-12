#!/bin/bash
docker rm -f web-link-tester
docker rmi -f circa10a/web-link-tester
docker run --name web-link-tester -d -p 80:80 circa10a/web-link-tester
