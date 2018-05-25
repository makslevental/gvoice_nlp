use std::env;
use std::fs;

extern crate select;
use select::document::Document;
use select::predicate::{Predicate, Attr, Class, Name};

fn main() -> std::io::Result<()> {
    let path = env::current_dir().unwrap();
    println!("The current directory is {}", env!("PWD"));
//    let paths = fs::read_dir("./Takeout").unwrap();
//    for path in paths {
//        let path_str = path.unwrap().path().display().to_string();
//        if path_str.contains("Text") {
//            let ww: Vec<_> = path_str.split_whitespace().collect();
//            fs::rename(&path_str, ww.join(""))?
//        }
//    }
    // include_Str is relative to this file (i.e. main.rs)
    let document = Document::from(include_str!("../Takeout/+1704168662-Text-2011-06-13T17_35_47Z.html"));
    for node in document.find(Attr("class", "message").descendant(Name("q"))) {
        println!("{} ({:?})", node.text(), node);
    }
    Ok(())
}
