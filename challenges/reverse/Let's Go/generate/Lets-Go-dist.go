package main

import (
	"bytes"
	"crypto/md5"
	"fmt"
	"strings"
)

func checkPassword(salt, password string) bool {
	hash := []byte{216, 93, 133, 32, 61, 121, 151, 54, 148, 93, 202, 176, 15, 138, 179, 137}

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
	checkPassword(SALT, userIn)

	if strings.TrimRight(userIn, "\n") == "https://pastebin.com/U6NLFqWJ" {
    	fmt.Printf("Hey that's an interesting link.\n")
	}

	fmt.Printf("Comparing not implemented... Access challenge server pls\n")
}
