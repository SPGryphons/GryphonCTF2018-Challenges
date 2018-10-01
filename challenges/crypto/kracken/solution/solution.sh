#!/bin/sh
pkcrack -C ../distrib/kracken.zip -P solution.zip -c gryphons.html -p gryphons.html -d out
unzip out -d output
rm -f out
