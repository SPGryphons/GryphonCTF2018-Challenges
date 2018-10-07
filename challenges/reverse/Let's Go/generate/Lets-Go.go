package main

import (
	"bytes"
	"crypto/md5"
	"fmt"
	"os"
)

func checkPassword(salt, password string) bool {
	hash := []byte{249, 113, 194, 239, 127, 17, 18, 187, 185, 255, 15, 38, 173, 143, 177, 124}

	//hashInByte, _ := hex.DecodeString(hash)

	data := []byte(salt + password)

	dataHash := md5.Sum(data)

	var hashByte []byte = dataHash[:]

	if bytes.Compare(hash, hashByte) == 0 {
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
		fmt.Println("Welcome", os.Getenv("FLAG"))
	} else {
		fmt.Printf("Try again\n")
	}

}
