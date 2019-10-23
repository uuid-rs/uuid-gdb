extern crate coredump;
extern crate uuid;

use uuid::Uuid;

fn main() {
    coredump::register_panic_handler().ok();
    let test1 = Uuid::parse_str("550e8400-e29b-41d4-a716-446655440000").unwrap();
    println!("test1 = uuid::Uuid( {} )", test1.to_hyphenated());
    panic!();
}
