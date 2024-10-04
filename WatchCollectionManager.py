import pandas as pd

class WatchCollection:
    # Constructor method to initialize object
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.collection = self.load_collection_from_csv()

    # Loads watch_collection csv
    def load_collection_from_csv(self):
        try:
            return pd.read_csv(self.csv_file)
        # Exception Handling
        except FileNotFoundError:
            return pd.DataFrame(columns=['Brand', 'Model', 'Type'])
    
    # Method to add watch    
    def add_watch(self, brand, model, watch_type):
        # Creates a new DataFrame with the provided details
        new_watch = pd.DataFrame({'Brand': [brand], 'Model': [model], 'Type': [watch_type]})
        self.collection = pd.concat([self.collection, new_watch], ignore_index=True)
        print(f"Watch added: {brand} {model}")

    def remove_watch(self, index):
        # Extracts the details of the watch to be removed based on the provided index
        removed_watch = self.collection.iloc[index]
        self.collection = self.collection.drop(index)
        print(f"Watch removed: {removed_watch['Brand']} {removed_watch['Model']}")

    # Method to edit watch by brand, model, and type)
    def edit_watch(self, index, column, new_value):
        self.collection.at[index, column] = new_value
        print("Watch information updated")

    # Searchs for watch 
    def search_watch(self, column, value):
        # filters the collection DataFrame based on the specified column and value
        result = self.collection[self.collection[column] == value]
        print(result)

def binary_search_watch(self, column, value):
    # Sort the collection DataFrame based on the specified column
    sorted_collection = self.collection.sort_values(by=column)

    # Initialize pointers for binary search
    left, right = 0, len(sorted_collection) - 1

    # Perform binary search
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        # Retrieve the value at the middle index in the sorted collection
        mid_value = sorted_collection.iloc[mid][column]

        # Check if the middle value matches the target value
        if mid_value == value:
            print(f"Watch found: {sorted_collection.iloc[mid]}")
            return
        # If the middle value is less than the target value, adjust the left pointer
        elif mid_value < value:
            left = mid + 1
        # If the middle value is greater than the target value, adjust the right pointer
        else:
            right = mid - 1

    # Print a message indicating that the watch was not found
    print("Watch not found")

# method to sort collection
def sort_collection(self, order):
    # Define a mapping for sorting order (ascending or descending)
    order_mapping = {'asc': True, 'desc': False}
    
    # Sort the collection DataFrame based on the 'Type' column
    self.collection = self.collection.sort_values(by='Type', ascending=order_mapping.get(order, True))
    
    # Print a message indicating that the collection has been sorted
    print("Collection sorted")


def save_changes(self):
    # Save the changes made to the collection DataFrame to the CSV file
    self.collection.to_csv(self.csv_file, index=False)
    
    # Print a message indicating that changes have been saved to the CSV file
    print("Changes saved to CSV")


def update_csv(self):
    # Save changes before updating the CSV file and print a confirmation message
    self.save_changes()
    print("Exiting the program.")

def main():
    # cvs file that stores the watch collection
    csv_file = 'watch_collection.csv'
    # calls WatchCollection class which contains all the methods
    watch_manager = WatchCollection(csv_file)

    while True:
        print("\nWatch Collection Manager:")
        print("1. Display Collection")
        print("2. Add Watch")
        print("3. Remove Watch")
        print("4. Edit Watch")
        print("5. Search Watch")
        print("6. Sort Collection")
        print("7. Save Changes (without exiting)")
        print("8. Save and Exit")     
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            watch_manager.display_collection()
        elif choice == '2':
            brand = input("Enter the brand: ")
            model = input("Enter the model: ")
            watch_type = input("Enter the watch type: ")
            watch_manager.add_watch(brand, model, watch_type)
        elif choice == '3':
            index = int(input("Enter the index of the watch to remove: "))
            watch_manager.remove_watch(index)
        elif choice == '4':
            index = int(input("Enter the index of the watch to edit: "))
            column = input("Enter the column to edit (Brand/Model/Type): ")
            new_value = input("Enter the new value: ")
            watch_manager.edit_watch(index, column, new_value)
        elif choice == '5':
            print("Search Options:")
            print("1. Linear Search")
            print("2. Binary Search")
            search_choice = input("Enter your search choice (1-2): ")
            column = input("Enter the column to search (Brand/Model/Type): ")
            value = input("Enter the value to search: ")

            if search_choice == '1':
                watch_manager.search_watch(column, value)
            elif search_choice == '2':
                watch_manager.binary_search_watch(column, value)
            else:
                print("Invalid search choice. Please enter 1 or 2.")
        elif choice == '6':
            print("Sort Options:")
            print("1. Ascending Order")
            print("2. Descending Order")
            sort_choice = input("Enter your sort choice (1-2): ")

            if sort_choice == '1':
                watch_manager.sort_collection('asc')
            elif sort_choice == '2':
                watch_manager.sort_collection('desc')
            else:
                print("Invalid sort choice. Please enter 1 or 2.")
        elif choice == '7':
            watch_manager.save_changes()
            break
        elif choice == '8':
            watch_manager.update_csv()
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()