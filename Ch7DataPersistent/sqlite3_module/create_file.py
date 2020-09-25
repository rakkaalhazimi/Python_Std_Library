import os

filenames = ["Creating a Database", "Retrieving Data", "Query Metadata",
             "Row Objects", "Using Variables with Queries", "Bulk Loading",
             "Defining New Column Types", "Determining Types for Columns", "Transactions",
             "Isolation Levels", "In-Memory Databases", "Exporting the Contents of a Database",
             "Using Python Functions in SQL", "Querying with Regular Expressions",
             "Custom Aggregation", "Threading and Connection Sharing", "Restricting Access to Data"]

index = 1

for filename in filenames:
    edited_filename = filename.replace(" ", "_")
    os.mkdir(f"No_{index}_{edited_filename.lower()}")
    index += 1








