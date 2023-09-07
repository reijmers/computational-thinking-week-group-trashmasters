use std::fs::File;
use std::io::{self, BufRead, Write};
use std::path::Path;
use std::fs::OpenOptions;

fn main() -> io::Result<()> {
    let path = Path::new("C:\\Users\\Gur Levy\\computational-thinking-week-group-trashmasters-1\\challenge_day4\\fulldata\\data5.txt");
    let file = File::open(&path)?;
    let reader = io::BufReader::new(file);

    let mut output = OpenOptions::new()
        .write(true)
        .create(true)
        .open("C:\\Users\\Gur Levy\\computational-thinking-week-group-trashmasters-1\\challenge_day4\\fulldata\\data6.txt")?;

    for (line_number, line) in reader.lines().enumerate() {
        let line = line?;

        if line_number == 0 {
            // This is the header, add "Evaluation" to it and write to file
            writeln!(output, "{},Evaluation", line)?;
            continue;
        }

        let parts: Vec<&str> = line.split(',').collect();
        if parts.len() < 7 {
            continue; // Skip invalid lines
        }

        let mut total_score = 0;
        let mut num_skills = 0;

        for &skill in &parts[1..=5] {
            match skill {
                "low" => {
                    total_score += 2;
                    num_skills += 1;
                },
                "middle" => {
                    total_score += 3;
                    num_skills += 1;
                },
                "good" => {
                    total_score += 4;
                    num_skills += 1;
                },
                "super" => {
                    total_score += 5;
                    num_skills += 1;
                },
                _ => (), // Skip if it's something else
            }
        }

        let evaluation = if num_skills > 0 {
            (total_score as f32) / (num_skills as f32)
        } else {
            0.0 // or whatever you want to set it to if no skills are evaluated
        };

        writeln!(output, "{},{},{}", line, parts[6], evaluation)?;
    }

    Ok(())
}
