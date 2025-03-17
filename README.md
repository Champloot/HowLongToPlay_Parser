# HowLongToPlay Parser

This script retrieves estimated game completion times from the howlongtoplay.ru website. It provides estimates for the main campaign, campaign plus additional tasks, and a full playthrough.

## Prerequisites

*   Python 3.6+
*   `requests` library:  `pip install requests`
*   `beautifulsoup4` library: `pip install beautifulsoup4`

## Installation

1.  Clone the repository or download the script files (`main.py` and `parser.py`).

## Usage

The script is executed from the command line, providing the game name as an argument.

```bash
python main.py -g "Game Name"
# or
python main.py --game "Game Name"

markdown
Replace "Game Name" with the name of the game you want to search for. The game name should be similar to how it’s listed on howlongtoplay.ru for the best results.

Example:

python main.py -g "Dead Cells"

bash
This will output the estimated completion times for Dead Cells.

Output
The script will print the estimated game completion times in the following format:

Main campaign:                  Xh. Ym.
Campaign + additional tasks:    Ah. Bm.
Full playthrough:               Ch. Dm.

Where X, Y, A, B, C, and D are the estimated hours and minutes.

Error Handling
If the script encounters an error (e.g., the game is not found on howlongtoplay.ru), it will print the message:

Something went wrong

Script Details
main.py: This is the main script that parses the command-line arguments, calls the parse function from parser.py, and prints the results. It handles user input and error reporting.
parser.py: This script contains the parse function, which fetches the data from howlongtoplay.ru, parses the HTML using BeautifulSoup, and extracts the estimated completion times. It uses the requests library to make HTTP requests and beautifulsoup4 to parse the HTML. It also defines a custom exception DefaultError for handling errors during parsing.
Code Explanation
main.py:

Uses optparse to handle command-line arguments (specifically the -g or --game option).
Converts the game name to lowercase.
Replaces digits in the game name with repeated ‘i’ characters (this is a specific handling of the website requirements). For example “diablo4” becomes “diabloiiii”.
Calls the parse() function from parser.py with the corrected game name.
Prints the formatted output.
Catches the DefaultError exception if something goes wrong during the parsing process.
parser.py:

Constructs the URL for howlongtoplay.ru based on the provided game name.
Makes an HTTP request to the URL using the requests library.
Checks if the response status code is 200 (OK). If not, raises a DefaultError.
Parses the HTML content using BeautifulSoup with the html.parser.
Locates the relevant div elements containing the time estimates.
Extracts the numerical values (hours and minutes) from the text of these div elements using regular expressions.
Returns a list containing the extracted time estimates for the main campaign, campaign plus additional tasks, and full playthrough.
Note on Website Usage
Please use this script responsibly and avoid excessive requests to the howlongtoplay.ru website. Too many requests in a short period might be interpreted as abuse and could result in your IP address being blocked. Consider adding delays between requests if you plan to use the script for multiple lookups. “`
