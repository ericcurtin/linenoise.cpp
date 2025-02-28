#!/bin/bash

install_dependencies() {
  if [ "$1" = "ci" ]; then
    if [ "$os" = "Darwin" ]; then
      brew install meson shellcheck coreutils
    else
      sudo apt install meson
    fi
  fi
}

set_compiler() {
  export CC="$1"
  export CXX="$2"
}

build_with_cmake() {
  cmake .
  make -j "$ncpu" VERBOSE=1
}

build_with_meson() {
  meson build --buildtype=release --prefix=/usr
  ninja -v -C build
}

main() {
  set -ex -o pipefail

  local os
  os="$(uname -s)"

  install_dependencies "$1"  
  shellcheck scripts/*.sh

  local ncpu
  ncpu="$(nproc)"

  set_compiler "gcc" "g++"
  build_with_cmake

  git clean -fdx
  build_with_meson

  git clean -fdx
  set_compiler "clang" "clang++"
  build_with_cmake

  git clean -fdx
  build_with_meson
}

main "$@"

