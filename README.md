# User Manual for the Watch Collection Catalog System

## Introduction

Welcome to the Watch Collection Manager! This program allows you to manage your watch collection efficiently. Whether you want to add new watches, remove existing ones, search for specific watches, or organize your collection, this program has you covered.

## Getting Started

Upon starting the program, you will be presented with the main menu, which provides the following options:

### Menu Overview
The program offers a simple text-based menu system. Each option corresponds to a specific action you can perform on your watch collection.

1. Display Collection
2. Add Watch
3. Remove Watch
4. Edit Watch
5. Search Watch
6. Sort Collection
7. Save Changes (without exiting)
8. Save and Exit

### Displaying All Watches

To view all the watches in the collection:
Enter `1`. 
The watches will be displayed in the order they were added to the collection.

### Adding a Watch

To add a watch to your collection:
Enter `2`.
Enter the brand, model, and type information as prompted.
The program will confirm that the watch has been successfully added.

### Removing a Watch

To remove a watch from your collection:
Enter `3`.
Enter the index of the watch you want to remove.
The program will confirm the removal of the watch.

### Editing Watch Information

To edit information for a watch in your collection:
Enter `4`.
Enter the index of the watch you want to edit.
Enter the column (Brand/Model/Type) you want to edit.
Enter the new value for the selected column.
The program will confirm that the watch information has been updated.

### Searching the Collection

To search for watches in your collection:
Enter `5`.
Select the search option (Linear Search/Binary Search).
Enter the column (Brand/Model/Type) you want to search.
Enter the value you are searching for.
The program will display the search results.

### Sorting the Collection

To sort your collection:
Enter `6`.
Select the sort order (Ascending Order/Descending Order).
The program will confirm that the collection has been sorted.

### Saving Changes (without exiting)

To save changes to your collection:
Enter `7`.
The program will save the changes to the CSV file and you will remain in the program.

### Exiting the Program

To exit the program:
Enter `8`.
Any changes made during your session will be saved automatically.

### Persistent Storage
The watch collection is stored in a CSV file (watch_collection.csv). Changes made to the collection are persistently saved to this file, ensuring that your data is preserved between program sessions.

### Error Handling
The program handles the case when the CSV file is not found, creating an empty collection if needed. If you encounter any issues, refer to the error messages for guidance.
