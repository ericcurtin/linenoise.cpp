#!/bin/bash

main() {
  set -ex -o pipefail

  local os
  os="$(uname -s)"
  if [ "$1" = "ci" ]; then
    if [ "$os" = "Darwin" ]; then
      brew install meson shellcheck
    else
      sudo apt install meson
    fi
  fi

  shellcheck scripts/*

  local ncpu
  ncpu="$(nproc)"

  export CC=gcc
  export CXX=g++
  cmake .
  make -j "$ncpu"

  git clean -fdx
  meson build --buildtype=release --prefix=/usr
  ninja -v -C build

  git clean -fdx
  export CC=clang
  export CXX=clang++
  cmake .
  make -j "$ncpu"

  git clean -fdx
  meson build --buildtype=release --prefix=/usr
  ninja -v -C build
}

main "$@"

