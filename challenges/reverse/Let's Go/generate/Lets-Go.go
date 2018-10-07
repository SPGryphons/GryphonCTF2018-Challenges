package main

import (
	"bytes"
	"crypto/md5"
	"encoding/hex"
	"fmt"
)

func checkPassword(salt, password string) bool {
	hash := "f971c2ef7f1112bbb9ff0f26ad8fb17c"

	hashInByte, _ := hex.DecodeString(hash)

	data := []byte(salt + password)

	dataHash := md5.Sum(data)

	var hashByte []byte = dataHash[:]

	if bytes.Compare(hashInByte, hashByte) == 0 {
		return true
	} else {
		return false
	}

}

func main() {
	SALT := "qweadsasgwe"
	var userIn string

	fmt.Printf("Password: ")
	fmt.Scanln(&userIn)

	fmt.Printf("You entered: %s\n", userIn)
	// call encryption
	userOut := checkPassword(SALT, userIn)
	if userOut {
		fmt.Printf("Welcome\n")
	} else {
		fmt.Printf("Try again\n")
	}

}
