use gittools::*;

fn main() {
  let args = get_args();

  let config = parse_config(&args);

  println!("Searching for {}", config.query);
  println!("In file {}", config.filename);

  let contents =
    get_contents(&config).expect("Something went wrong reading the file");

  println!("With text:\n{}", contents);
}
