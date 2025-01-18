import csv


def validate_csv(file_path, expected_columns):
        with open(file_path, 'r', encoding='utf-8') as f:
            read_file = csv.reader(f)
            headers = next(read_file, None)

            if len(headers) != expected_columns:
                return (
                    f"CSV headers do not match expected columns.\n"
                    f"Expected: {expected_columns}\n"
                    f"Found: {headers}"
                )

        return "CSV file format is valid."


# Example usage
file_path = "Hello.csv"
expected_columns = 9

result = validate_csv(file_path, expected_columns)
print(result)
