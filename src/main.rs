use std::env;
use std::fs;
use std::io::prelude::*;
use std::fs::File;
use std::collections::HashMap;

extern crate select;

use select::document::Document;
use select::predicate::{Predicate, Attr, Class, Name};

extern crate serde;
extern crate serde_json;

#[macro_use]
extern crate serde_derive;

use serde_json::Error;

#[derive(Serialize, Deserialize)]
struct Message {
    body: String,
    name: String,
    time: String,
}

fn main() -> std::io::Result<()> {
    let mut messages: Vec<Message> = Vec::new();

    println!("The current directory is {}", env!("PWD"));
    let paths = fs::read_dir("/Users/max/dev_projects/gvoice_nlp/Takeout").unwrap();
    for path in paths {
        let path_str = path.unwrap().path().display().to_string();
//        if path_str.contains("Text") {
//            let ww: Vec<_> = path_str.split_whitespace().collect();
//            fs::rename(&path_str, ww.join(""))?
//        } else {
//            fs::remove_file(path_str)?;
//        }
        let mut file = File::open(&path_str).expect("Unable to open the file");
        let mut contents = String::new();
        file.read_to_string(&mut contents).expect(format!("Unable to read the file {}", &path_str).as_str());
        let document = Document::from(contents.as_str());
        for node in document.find(Attr("class", "message")) {
//            println!(
//                "{} {} {}",
//                node.find(Attr("class", "tel")).next().unwrap().text(),
//                node.find(Name("abbr")).next().unwrap().attr("title").unwrap(),
//                node.find(Name("q")).next().unwrap().text()
//            );
            let time = node.find(Name("abbr")).next().unwrap().attr("title").unwrap().to_owned();
            let name = node.find(Attr("class", "tel")).next().unwrap().text().to_owned();
            let body = node.find(Name("q")).next().unwrap().text();
            let msg = Message {
                name: name,
                body: body,
                time: time,
            };
            messages.push(msg);
        }
    }
    messages.sort_by(|a, b| a.time.cmp(&b.time));
    let j = serde_json::to_string(&messages)?;

    fs::write("/Users/max/dev_projects/gvoice_nlp/messages.json", j).expect("Unable to write file");

    Ok(())
}
