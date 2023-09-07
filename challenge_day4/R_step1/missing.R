# Check if jsonlite is installed; if not, install it
if (!requireNamespace("jsonlite", quietly = TRUE)) {
  install.packages("jsonlite", repos = "http://cran.rstudio.com/")
}

# Load the required library
library(jsonlite)

# Read the JSON file into a data frame
json_data <- fromJSON("data1.json")

# Convert the 'people' list to a data frame
people_df <- as.data.frame(json_data$people)

# Replace NAs with column means
for(col_name in names(people_df)) {
  if(is.numeric(people_df[[col_name]])) {
    # Calculate mean, excluding NAs
    col_mean <- mean(people_df[[col_name]], na.rm = TRUE)
    
    # Replace NAs with the calculated mean
    people_df[[col_name]][is.na(people_df[[col_name]])] <- col_mean
  }
}

# Replace the 'people' list in the original data with the modified data frame
json_data$people <- person_df

# Convert the updated data back to JSON format
json_text <- toJSON(json_data, pretty = TRUE)

# Overwrite the original JSON file
write(json_text, "data2.json")
