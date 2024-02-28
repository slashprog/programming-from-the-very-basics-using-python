use std::io::{self, Write};

fn main() {
    print!("Enter a number: ");
    io::stdout().flush().expect("Failed to flush stdout!");

    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .expect("Failed to read user input!");

    let number: u32 = input
                .trim()
                .parse()
                .expect("Please enter a valid number!");

    for i in 1..=10 {
        println!("{} x {} = {}", number, i, number * i);
    }
}
