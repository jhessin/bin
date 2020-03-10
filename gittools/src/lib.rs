use std::env;
use std::fs;

pub struct Config {
  pub query: String,
  pub filename: String,
}

pub fn get_args() -> Vec<String> {
  env::args().collect()
}

pub fn parse_config(args: &[String]) -> Config {
  let query = args[1].clone();
  let filename = args[2].clone();

  Config { query, filename }
}

pub fn get_contents(config: &Config) -> Result<String, std::io::Error> {
  Ok(fs::read_to_string(&config.filename)?)
}
