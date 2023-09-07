using DataFrames, CSV, Statistics, DelimitedFiles

# Read the CSV file into a DataFrame
people_df = CSV.File("data3.csv") |> DataFrame

# Function to classify a score based on quartiles
function classify_score(score, quartiles)
    if score <= quartiles[1]
        return "low"
    elseif score <= quartiles[2]
        return "middle"
    elseif score <= quartiles[3]
        return "good"
    else
        return "super"
    end
end

# Iterate over each column (skipping the 'name' column)
for col_name in names(people_df)[2:end]
    # Convert float values that are whole numbers to integers
    col_data = map(x -> isa(x, Float64) && x == floor(x) ? Int(x) : x, people_df[!, col_name])

    # Compute quartiles using only integers
    valid_data = filter(x -> x isa Int, col_data)

    if isempty(valid_data)
        println("No valid data for column $col_name")
        continue
    end

    quartiles = quantile(valid_data, [0.25, 0.5, 0.75])

    # Replace values with categories or 'low' if they are Float64
    new_col = map(x -> x isa Float64 ? "low" : classification_score(x, quartiles), col_data)
    people_df[!, col_name] = new_col
end

# Save the modified DataFrame back to a new CSV file
CSV.write("data4.txt", people_df)

# Save the modified DataFrame back to a new TXT file
#writedlm("data4.txt", people_df, ',')