#!/usr/bin/env bash
VERSION="1.0.0"

# Docker
USER='circa10a'
PROJECT='web-link-tester'
NAMESPACE=${USER}/${PROJECT}
# Docker experimental config
echo '{"experimental":true}' | sudo tee /etc/docker/daemon.json
[ -d ~/.docker ] || mkdir ~/.docker
[ -f ~/.docker/config.json ] || touch ~/.docker/config.json
echo '{"experimental":"enabled"}' | sudo tee ~/.docker/config.json
sudo service docker restart
# Auth
echo $docker_password | docker login -u="$USER" --password-stdin

# Latest x86
docker build -t "${NAMESPACE}:latest" . && \
docker push "${NAMESPACE}:latest" && \
# Versioned x86
docker tag "${NAMESPACE}:latest" "${NAMESPACE}:${VERSION}" && \
docker push "${NAMESPACE}:${VERSION}"

# prepare qemu for ARM builds
docker run --rm --privileged multiarch/qemu-user-static:register --reset

for i in $(ls *.rpi); do
  arch="$(echo ${i} | cut -d- -f2 | cut -d. -f1)"
  # Latest
  docker build -f "./Dockerfile-${arch}.rpi" -t "${NAMESPACE}:latest-${arch}-rpi" . && \
  docker push "${NAMESPACE}:latest-${arch}-rpi" && \
  # Versioned
  docker tag "${NAMESPACE}:latest-${arch}-rpi" "${NAMESPACE}:${VERSION}-${arch}-rpi" && \
  docker push "${NAMESPACE}:${VERSION}-${arch}-rpi"
done

# Support multiple architectures with same image
docker manifest create "${USER}/${PROJECT}:latest ${USER}/${PROJECT}:latest-arm32v7-rpi" "${USER}/${PROJECT}:latest-arm64v8-rpi"
docker manifest annotate "${USER}/${PROJECT}:latest ${USER}/${PROJECT}:latest-arm32v7-rpi --os linux --arch armv7"
docker manifest annotate "${USER}/${PROJECT}:latest ${USER}/${PROJECT}:latest-arm64v8-rpi --os linux --arch arm64 --variant armv8"
docker manifest push "${NAMESPACE}:latest"