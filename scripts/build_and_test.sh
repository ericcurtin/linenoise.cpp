#!/bin/bash

main() {
  set -exu -o pipefail

  local os
  os="$(uname -s)"
  if [ "$os" = "Darwin" ]; then
    brew install meson
  else
    sudo apt install meson
  fi

  export CC=gcc
  export CXX=g++
  cmake .
  make -j $(nproc)

  git clean -fdx
  meson build --buildtype=release --prefix=/usr
  ninja -v -C build

  git clean -fdx
  export CC=clang
  export CXX=clang++
  cmake .
  make -j $(nproc)

  git clean -fdx
  meson build --buildtype=release --prefix=/usr
  ninja -v -C build
}

main "$@"

