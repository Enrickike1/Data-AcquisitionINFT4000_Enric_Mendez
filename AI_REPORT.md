# AI Report

## What worked well / badly with AI

At the beginning, I used AI before I really understand the dataset, so my first attempt was not working good and I decided to start again. After I spent some time understanding the data, I used AI to make the skeleton of the project and improve it step by step. I gave instructions about the files and the data, and I checked the results after every change. It helped me with the main workflow, the scraping functions and the visualisations. Sometimes I had to correct the AI because some country names did not match with the ISO2 codes and some web pages were not loading directly. I tested the code and asked for changes when something was not working.

## Prompts used

### Creating the initial project structure

Context: university Data Acquisition project. Repo already has data/human_trafficking.csv (CTDC human trafficking dataset, 48,801 rows, 63 columns; unknown values coded as -99 or "00"; citizenship and CountryOfExploitation are ISO2 codes).

Create notebook 01_kaggle.ipynb with cells that load the CSV into pandas, show the shape, dtypes, head and null counts, count the values -99 and "00" per column, and show value_counts for the main columns. Add an empty markdown cell titled "Dataset description". Also create AI_REPORT.md and requirements.txt. Keep the code minimal and commented. Do not commit anything.

### Creating the main workflow

Create the main Python file for the project. Load the human trafficking CSV, use a reproducible sample of 10,000 rows, remove unknown citizenship values, count the records by citizenship and save the result to a CSV. Keep the code simple and easy to explain.

### Scraping the poverty data

Add a scraping step for the World Bank poverty table using requests and BeautifulSoup. Extract the country name, the latest available year and the percentage of people below the poverty line. Convert the country names to ISO2 codes and merge the result with the trafficking data using citizenship.

### Fixing country code matches

Some country names are not matching correctly with their ISO2 codes. Add simple aliases for countries such as Niger, Nigeria, Lao PDR, Cote d'Ivoire and Turkiye. Use exact matching instead of fuzzy matching when possible, and keep unmatched values visible.

### Adding the corruption data

Add a second scraping step for the corruption ranking page. Extract the country name and the 2025 CPI score, convert the country names to ISO2 codes and merge this data with the trafficking and poverty data. Save the final CSV.

### Splitting the code into files

Split the project into three simple files: index.py for the main workflow, scraping.py for the BeautifulSoup table scraper, and country_codes.py for the country name to ISO2 conversion. Keep the code minimal and remove unnecessary comments.

### Creating the visualisations

Create a notebook called 03_visualisation.ipynb. Load the final CSV and use Seaborn and Matplotlib to create a top-10 nationalities bar chart, a poverty versus trafficking scatter plot and a corruption versus trafficking scatter plot. Add simple markdown sections where I can write my own observations.

### Simplifying the comments and descriptions

Clean up the comments in the code and leave only short comments that are easy to explain. Add a short dataset description explaining the number of rows and columns, the 10,000-row sample, the main columns and the columns not used in the analysis.
