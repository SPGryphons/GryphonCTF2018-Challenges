package main

import (
	"fmt"
)

// https://github.com/KyleBanks/XOREncryption/blob/master/Go/xor.go
func EncryptDecrypt(input, key string) (output string) {
	for i := range input {
		output += string(input[i] ^ key[i%len(key)])
	}

	return output
}

func main() {
	var FLAG string = "GCTF{G0_G0_G0}"
	var userIn string

	fmt.Printf("Hello give me your key: ")
	fmt.Scanln(&userIn)

	fmt.Printf("You entered: %s\n", userIn)
	// call encryption
	userOut := EncryptDecrypt(FLAG, userIn)
	fmt.Printf("This is the output: %s\n", userOut)
}
