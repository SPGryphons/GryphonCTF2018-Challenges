#!/bin/sh
go build Lets-Go.go
go build Lets-Go-dist.go
mv Lets-Go-dist ../distrib/
mv Lets-Go ../service/
