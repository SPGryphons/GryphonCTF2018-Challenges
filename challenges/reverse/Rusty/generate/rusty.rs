use std::io;
use std::env;

fn main() {
    print!("Password > ");
    io::Write::flush(&mut io::stdout()).expect("flush failed!");

    let mut pass = String::new();
    match io::stdin().read_line(&mut pass) {
        Ok(_) => {},
        Err(err) => println!("Could not parse input: {}", err)
    }
    // Rot13: mYsUpersECretRustprogrampasSWorD
    let realpass = "zLfHcrefRPergEhfgcebtenzcnfFJbeQ";

    if pass.trim() == rot13(realpass) {
        let key = "FLAG";
        match env::var(key) {
            Ok(val) => println!("Here's your flag: {}", val),
            Err(e) => println!("couldn't interpret {}: {}", key, e),
        }
    } else {
        println!("No flags for you!");
    }
}

fn rot13(text: &str) -> String {
    text.chars().map(|c| {
        match c {
            'A' ... 'M' | 'a' ... 'm' => ((c as u8) + 13) as char,
            'N' ... 'Z' | 'n' ... 'z' => ((c as u8) - 13) as char,
            _ => c
        }
    }).collect()
}