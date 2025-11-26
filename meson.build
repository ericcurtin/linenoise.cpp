project('linenoise.cpp', 'cpp',
  default_options : [
        'werror=true',
        'warning_level=3',
        'cpp_std=c++17'
  ])

linenoise_lib = library(
    'linenoise',
    [
      'linenoise.cpp',
    ],
    cpp_args: [],
    install: true,
    dependencies: [],
    include_directories: [include_directories('.')],
)

linenoise_dep = declare_dependency(
  link_with: linenoise_lib,
  include_directories: [include_directories('.')],
)

executable('linenoise',
  'example.cpp',
  dependencies: [linenoise_dep]
)

install_headers(['linenoise.h'])

pconf = import('pkgconfig')
pconf.generate(
  linenoise_lib,
  description: 'A minimal, zero-config, BSD licensed, readline replacement ',
  url: 'https://github.com/ericcurtin/linenoise.cpp',
  version: meson.project_version(),
)