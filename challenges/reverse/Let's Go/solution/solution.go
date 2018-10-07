package main

import (
	"fmt"
)

var FLAG string = "THIS_IS_THE_FLAG"

// https://github.com/KyleBanks/XOREncryption/blob/master/Go/xor.go
func EncryptDecrypt(input, key string) (output string) {
	for i := range input {
		output += string(input[i] ^ key[i%len(key)])
	}

	return output
}

func main() {
	input := "vrewJvnvnvL"
	key := "111111111111111111111"

	out := EncryptDecrypt(input, key)

	fmt.Println("The val: ", out)
}
