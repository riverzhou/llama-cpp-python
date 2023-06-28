#!/bin/bash

rm -rf dist _skbuild

CMAKE_ARGS="-DLLAMA_CUBLAS=on -DLLAMA_CUDA_DMMV_F16=on -DLLAMA_NATIVE=on -DLLAMA_LTO=on -DLLAMA_AVX512=on -DLLAMA_AVX512_VBMI=on -DLLAMA_AVX512_VNNI=on " FORCE_CMAKE=1  python setup.py bdist_wheel

