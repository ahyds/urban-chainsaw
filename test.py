import os
import csv

# Path to collect data from the Resources folder
csvpath=('','','WWE-Data-2016.csv')

# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

# Define the function and have it accept the 'wrestlerData' as its sole parameter
    def print_percentages(wrestlerData):
        name = input("Who are you checking?")

# Find the total number of matches wrestled
        for row in csvreader:
            if row [0] ==name:
                    total = row[1]+row[2]+row[3]
                # Find the percentage of matches won
                per_won = row[1]/total
                # Find the percentage of matches lost
                per_l = row[2]/total
                # Find the percentage of matches drawn
                per_d = row[3]/total
                # Print out the wrestler's name and their percentage stats
                print(f"Wrestler {name} has played {total} games and has win rate:  {per_won},loss rate: {per_l} and draw rate: {per_d}")
