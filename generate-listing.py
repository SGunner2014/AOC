import os
import json
import importlib

# This file generates a JSON listing for all valid years, days, parts, example files

excluded_names = [
    '.DS_Store',
]

listings = []

years_path = "./years"
years = os.listdir(years_path)
for year in years:
    year_listing = {
        "year": year,
        "days": {},
    }
    if os.path.isdir(f"{years_path}/{year}") and year not in excluded_names:
        days = os.listdir(f"{years_path}/{year}")
        for day in days:
            if os.path.isdir(f"{years_path}/{year}/{day}") and day not in excluded_names:
                day_path = f"{years_path}/{year}/{day}"

                day_number = int(day.replace("day", ""))

                day_file_path = f"{day_path}/main.py"

                if not os.path.isfile(day_file_path):
                    day_file_path = f"{day_path}/day{day_number}.py"
                    if not os.path.isfile(day_file_path):
                        print(f"Skipping {day_file_path}")
                        continue

                # day_module = importlib.import_module(f"years.{year}.{day}.main")
                if day_file_path.endswith("main.py"):
                    day_module = importlib.import_module(f"years.{year}.{day}.main")
                else:
                    day_module = importlib.import_module(f"years.{year}.{day}.day{day_number}")

                listing = {
                    "tests": [],
                    "example_inputs": [],
                    "inputs": [],
                }

                day_file_listing = os.listdir(day_path)
                for file in day_file_listing:
                    if file.endswith(".txt") and os.path.isfile(f"{day_path}/{file}"):
                        if file.startswith("example"):
                            listing["example_inputs"].append(file)
                        elif file.startswith("input"):
                            listing["inputs"].append(file)

                day_module_dir = dir(day_module)
                if "part1" in day_module_dir:
                    listing["part1"] = True
                if "part2" in day_module_dir:
                    listing["part2"] = True

                listing["main_file"] = day_file_path[2:]

                if "tests" in day_module_dir:
                    tests = day_module.tests

                    for (filename, values) in tests.items():
                        test = {
                            "filename": filename,
                        }

                        if isinstance(values, tuple):
                            test["expected"] = values[0]
                            test["args"] = values[1:]
                        else:
                            test["expected"] = values

                        listing["tests"].append(test)

                year_listing["days"][day_number] = listing

    listings.append(year_listing)


h = open("listing.json", "w")
h.write(json.dumps(listings, indent=2))
h.close()