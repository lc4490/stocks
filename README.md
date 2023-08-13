# Stocks (Steals + Blocks)

This Python script reads player information from a file named `playerinfo.txt` and analyzes the data to calculate player performance metrics. The script uses the Pandas library to load and manipulate the data, and it calculates a custom metric called "stocks" (combined steals and blocks) to rank players based on their defensive contributions.

## How to Use

1. Place the `playerinfo.txt` file in the same directory as the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the command:

   ```bash
   python stocks.py
   ```

4. The script will display the top 10 players based on the "stocks" metric.

## Features

- Loads player information from the `playerinfo.txt` file.
- Calculates the "stocks" metric by combining steals and blocks for each player.
- Sorts the player data based on the "stocks" metric in descending order.
- Displays the top 10 players with the highest "stocks" values.

## Note

- The script assumes that the `playerinfo.txt` file contains comma-separated values (CSV) with headers in the first row and player data in subsequent rows.
  
- `playerinfo.txt` is simply the stat sheet for all players in the 2022-2023 season. It will need to be updated for the 2023-2024 season.

- The script demonstrates a simple data analysis task using Pandas and NumPy.

- The script is provided as-is and may not have extensive error handling or advanced features.

## Disclaimer

This script is for educational and illustrative purposes only. It may require modifications to work with different data formats or to suit specific needs.

**Author**: Leo Chao

**Date**: 2023/08/13
