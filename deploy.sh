#!/usr/bin/env bash
VERSION="1.0.0"

# Docker
USER='circa10a'
PROJECT='web-link-tester'
NAMESPACE="${USER}/${PROJECT}"

# Docker experimental config
echo '{"experimental":true}' | sudo tee /etc/docker/daemon.json
[ -d ~/.docker ] || mkdir ~/.docker
[ -f ~/.docker/config.json ] || touch ~/.docker/config.json
echo '{"experimental":"enabled"}' | sudo tee ~/.docker/config.json
sudo service docker restart

# Auth
echo $docker_password | docker login -u="$USER" --password-stdin

# Latest x64
docker build -t "${NAMESPACE}:latest" . && \
docker push "${NAMESPACE}:latest" && \
# Versioned x64
docker tag "${NAMESPACE}:latest" "${NAMESPACE}:${VERSION}" && \
docker push "${NAMESPACE}:${VERSION}" && \
# x64 Arch
docker tag "${NAMESPACE}:latest" "${NAMESPACE}:latest-amd64" && \
docker push "${NAMESPACE}:latest-amd64"

# prepare qemu for ARM builds
docker run --rm --privileged multiarch/qemu-user-static:register --reset

# ARM images
for i in $(ls *.rpi); do
  arch="$(echo ${i} | cut -d- -f2 | cut -d. -f1)"
  # Latest
  docker build -f "./Dockerfile-${arch}.rpi" -t "${NAMESPACE}:latest-${arch}-rpi" . && \
  docker push "${NAMESPACE}:latest-${arch}-rpi" && \
  # Versioned
  docker tag "${NAMESPACE}:latest-${arch}-rpi" "${NAMESPACE}:${VERSION}-${arch}-rpi" && \
  docker push "${NAMESPACE}:${VERSION}-${arch}-rpi"
done

wget -O manifest-tool https://github.com/estesp/manifest-tool/releases/download/v0.9.0/manifest-tool-linux-amd64 && \
chmod +x manifest-tool && \
./manifest-tool --user "$USER" --password "$docker_password" from-spec "${USER}-${PROJECT}.yaml"