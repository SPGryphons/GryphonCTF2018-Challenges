#!/bin/sh
rustc rusty.rs -o rusty
cp rusty ../service/
mv rusty ../distrib/
