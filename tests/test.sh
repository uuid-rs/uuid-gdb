#!/bin/bash

cargo build
cargo run > correct_result.txt
coredumpctl dump > ./rust.core
rust-gdb --command=./gdb_commands.txt ./target/debug/tests ./rust.core > test_output.txt

if [[ $(grep "test1" correct_result.txt) == $(grep "test1" test_output.txt) ]]
then
    echo "Test passed"
    exit 0
else
    echo "Test failed"
    exit 1
fi
