#include <stdio.h>
#include <string.h>
#include <iostream>

char* obfuscate(std::string input) {
	int i = input.length();
	char* out = new char[i + 1];

	out[i--] = '\0';

	for (char &c : input) {
		out[i] = c + (i--) * 10 + 1;
	}

	return out;
}

int main() {
	std::string userInput;
	const char flagObs[] = "\x7E\x3E\x49\x81\x88\x68\x6E\xA6\x86\xB2\x95\xB3\xC7\xCC\xE4\x12\xE7\xFF\xF8\x06";
	std::cout << "Gimme something: ";
	std::cin >> userInput;
	
	if (strcmp(obfuscate(userInput), flagObs) == 0) {
		std::cout << "You got it!";
	}
	else {
		std::cout << "Better luck next time...";
	}

	return 0;
}