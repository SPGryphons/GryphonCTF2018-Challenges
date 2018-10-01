package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"math/rand"
	"net"
	"strconv"
	"strings"
	"time"
)

// timeoutDuration states how many seconds participants
// should be given to answer question
var timeoutDuration time.Duration = 3
var floatBitSize = 64
var decimalPrecision = -1

// mathParser parses math strings
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

func getProblemSum() problemSum {
	var length = getNumberInRange(3, 10)

	var sum string
	for ; length > 0; length-- {
		sum += strconv.Itoa(getNumberInRange(1, 15)) + " "

		if length != 1 {
			sum += getSign() + " "
		}
	}

	var problemSum problemSum
	problemSum.sum = strings.TrimSpace(sum)
	problemSum.state = strings.Split(problemSum.sum, " ")

	return problemSum
}

func getSign() string {
	var sign = []string{"+", "-", "*", "/"}
	return sign[getNumberInRange(0, 3)]
}

func getNumberInRange(min int, max int) int {
	return rand.Intn(max-min+1) + min
}

func clientWrite(client net.Conn, data string) bool {
	length, err := fmt.Fprintf(client, data)
	return err == nil && length == len(data)
}

func clientRead(client net.Conn) (string, bool) {
	var (
		full     bytes.Buffer
		success  = false
		buffer   = make([]byte, 1024)
		clientIn = bufio.NewReader(client)
	)

	for {
		length, err := clientIn.Read(buffer)
		if err != nil {
			return "", success
		}

		full.Grow(length)
		full.Write(buffer[:length])

		if strings.HasSuffix(full.String(), "\n") {
			success = true
			break
		}
	}

	return strings.TrimSpace(full.String()), success
}

func clientReadTimeout(client net.Conn) (string, bool) {
	var (
		full     bytes.Buffer
		success  = false
		buffer   = make([]byte, 1024)
		clientIn = bufio.NewReader(client)
	)

	client.SetReadDeadline(time.Now().Add(time.Second * timeoutDuration))

	for {
		length, err := clientIn.Read(buffer)
		if err != nil {
			if nerr, ok := err.(net.Error); ok && nerr.Timeout() {
				_ = clientWrite(client, "\n\nOpps, too slow :(\n")
			}

			return "", success
		}

		full.Grow(length)
		full.Write(buffer[:length])

		if strings.HasSuffix(full.String(), "\n") {
			success = true
			break
		}
	}

	return strings.TrimSpace(full.String()), success
}

func connectionHandler(client net.Conn) {
	// var message string
	defer client.Close()
	defer log.Println("Client disconnected from", client.RemoteAddr().String())

	var welcomeMessage = "============================ Math Test ============================\n" +
		"Welcome to the VSA\n" +
		"This math test is pretty simple\n" +
		"There are a total of 100 questions\n" +
		"Leave your answers in 25 decimal places where decimals are required\n" +
		"Oh, and you have 3 seconds for each question\n" +
		"\nLet's go! "

	clientWrite(client, welcomeMessage)

	// For blocking purposes only
	_, success := clientRead(client)
	if !success {
		return
	}

	var complete = false
	for i := 0; i < 100; i++ {
		var problemSum = getProblemSum()
		problemSum.add()
		problemSum.multiply()
		problemSum.subtract()
		problemSum.divide()

		answer, err := strconv.ParseFloat(problemSum.state[0], floatBitSize)
		if err != nil {
			log.Fatalln("Line 246 (Own Answer):", err)
		}

		success := clientWrite(client, "Sum: "+problemSum.sum+"\nAnswer: ")
		if !success {
			complete = false
			break
		}

		// Parse and check answer
		receive, success := clientReadTimeout(client)
		if !success {
			complete = false
			break
		}

		userAnswer, err := strconv.ParseFloat(receive, floatBitSize)
		if err != nil {
			log.Println("Line 265:", err)
		}

		if userAnswer != answer {
			clientWrite(client, "\nWell, that was a good attempt, but the answer was "+
				strconv.FormatFloat(answer, 'f', -1, floatBitSize)+
				"\n")
			complete = false
			break
		}
		complete = true
	}

	if complete {
		clientWrite(client, "Not bad, you're GCTF{G00D_4T_M47H}\n")
	}
}

func main() {
	// seed random first
	rand.Seed(time.Now().Unix())

	server, err := net.Listen("tcp4", ":8000")
	defer server.Close()

	if err != nil {
		log.Fatalln("Could not listen on", server.Addr().String())
	}

	fmt.Println("Server started listening on", server.Addr().String())

	for {
		client, err := server.Accept()
		if err != nil {
			log.Println("Client connection error from", client.RemoteAddr().String())
		}

		log.Println("Client connection from", client.RemoteAddr().String())
		go connectionHandler(client)
	}
}
