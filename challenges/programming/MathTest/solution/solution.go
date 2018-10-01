package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"net"
	"regexp"
	"strconv"
	"strings"
)

// Connection stuff
var host = "127.0.0.1"
var port = ":8000"

var floatBitSize = 64
var decimalPrecision = -1

type problemSum struct {
	sum   string
	state []string
}

func (problemSum *problemSum) add() bool {
	var localSum = problemSum.state

OUTERLOOP:
	for {
		var endPos = len(localSum) - 2
		if endPos < 0 {
			break
		}

		var position int
		for position = 1; position <= endPos; position += 2 {
			if localSum[position] == "+" {
				break
			}

			if position == endPos {
				break OUTERLOOP
			}
		}

		// extract elements & form now state
		num1, err := strconv.ParseFloat(localSum[position-1], floatBitSize)
		if err != nil {
			return false
		}

		num2, err := strconv.ParseFloat(localSum[position+1], floatBitSize)
		if err != nil {
			return false
		}

		// append magic
		var intermediate = append(localSum[:position-1],
			strconv.FormatFloat(num1+num2, 'f', decimalPrecision, floatBitSize))
		localSum = append(intermediate, localSum[position+2:]...)
	}

	problemSum.state = localSum
	return true
}

func (problemSum *problemSum) subtract() bool {
	var localSum = problemSum.state

OUTERLOOP:
	for {
		var endPos = len(localSum) - 2
		if endPos < 0 {
			break
		}

		var position int
		for position = 1; position <= endPos; position += 2 {
			if localSum[position] == "-" {
				break
			}

			if position == endPos {
				break OUTERLOOP
			}
		}

		// extract elements & form now state
		num1, err := strconv.ParseFloat(localSum[position-1], floatBitSize)
		if err != nil {
			return false
		}

		num2, err := strconv.ParseFloat(localSum[position+1], floatBitSize)
		if err != nil {
			return false
		}

		// append magic
		var intermediate = append(localSum[:position-1],
			strconv.FormatFloat(num1-num2, 'f', decimalPrecision, floatBitSize))
		localSum = append(intermediate, localSum[position+2:]...)
	}

	problemSum.state = localSum
	return true
}

func (problemSum *problemSum) multiply() bool {
	var localSum = problemSum.state

OUTERLOOP:
	for {
		var endPos = len(localSum) - 2
		if endPos < 0 {
			break
		}

		var position int
		for position = 1; position <= endPos; position += 2 {
			if localSum[position] == "*" {
				break
			}

			if position == endPos {
				break OUTERLOOP
			}
		}

		// extract elements & form now state
		num1, err := strconv.ParseFloat(localSum[position-1], floatBitSize)
		if err != nil {
			return false
		}

		num2, err := strconv.ParseFloat(localSum[position+1], floatBitSize)
		if err != nil {
			return false
		}

		// append magic
		var intermediate = append(localSum[:position-1],
			strconv.FormatFloat(num1*num2, 'f', decimalPrecision, floatBitSize))
		localSum = append(intermediate, localSum[position+2:]...)
	}

	problemSum.state = localSum
	return true
}

func (problemSum *problemSum) divide() bool {
	var localSum = problemSum.state

OUTERLOOP:
	for {
		var endPos = len(localSum) - 2
		if endPos < 0 {
			break
		}

		var position int
		for position = 1; position <= endPos; position += 2 {
			if localSum[position] == "/" {
				break
			}

			if position == endPos {
				break OUTERLOOP
			}
		}

		// extract elements & form now state
		num1, err := strconv.ParseFloat(localSum[position-1], floatBitSize)
		if err != nil {
			return false
		}

		num2, err := strconv.ParseFloat(localSum[position+1], floatBitSize)
		if err != nil {
			return false
		}

		// append magic
		var intermediate = append(localSum[:position-1],
			strconv.FormatFloat(num1/num2, 'f', decimalPrecision, floatBitSize))
		localSum = append(intermediate, localSum[position+2:]...)
	}

	problemSum.state = localSum
	return true
}

func writeStream(server net.Conn, data string) bool {
	length, err := fmt.Fprintf(server, data)
	return err == nil && length == len(data)
}

func readStream(server net.Conn, delim string) (string, bool) {
	var (
		full     bytes.Buffer
		success  = false
		buffer   = make([]byte, 1024)
		serverIn = bufio.NewReader(server)
	)

	for {
		length, err := serverIn.Read(buffer)
		if err != nil {
			return "", success
		}

		full.Grow(length)
		full.Write(buffer[:length])

		if strings.HasSuffix(full.String(), delim) {
			success = true
			break
		}
	}

	return strings.TrimSpace(full.String()), success
}

func main() {
	var regPat = regexp.MustCompile("Sum: (.*)\\nAnswer:")
	server, err := net.Dial("tcp", host+port)
	fmt.Println("Connected!")
	defer server.Close()

	if err != nil {
		log.Fatalln("Ded :(")
		return
	}

	receive, success := readStream(server, "Let's go! ")
	if !success {
		log.Fatalln("Ded :(")
		return
	}

	writeStream(server, "\n")

	for i := 0; i < 100; i++ {
		receive, success := readStream(server, "Answer: ")
		if !success {
			log.Fatalln("Ded 1 :(")
			return
		}

		var problemSum problemSum

		sum := regPat.FindStringSubmatch(receive)
		problemSum.sum = sum[1]
		problemSum.state = strings.Split(problemSum.sum, " ")
		problemSum.add()
		problemSum.multiply()
		problemSum.subtract()
		problemSum.divide()

		answer, err := strconv.ParseFloat(problemSum.state[0], floatBitSize)
		ansString := strconv.FormatFloat(answer, 'f', 25, floatBitSize)
		if err != nil {
			log.Fatalln("Own Answer:", ansString, "\nSum:", receive)
		}

		success = writeStream(server, ansString+"\n")
		if !success {
			log.Fatalln("Ded, server doesn't like me - writing failed :(")
			return
		}

		fmt.Printf("Completed Sum %d: %s\nAnswer: %s\n\n", i+1, problemSum.sum, ansString)
	}

	receive, success = readStream(server, "\n")
	if !success {
		log.Fatalln("Doesn't like me")
	}

	fmt.Println(receive)
}
