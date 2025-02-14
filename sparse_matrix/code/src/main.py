from sparse_matrix import SparseMatrix

def print_matrix(matrix):
    """ Prints the sparse matrix in a readable format. """
    print(f"\nMatrix ({matrix.num_rows} x {matrix.num_cols}):")
    for i in range(matrix.num_rows):
        row_values = []
        for j in range(matrix.num_cols):
            row_values.append(str(matrix.get_element(i, j)))
        print(" ".join(row_values))

def main():
    """ Interactive menu for performing operations on sparse matrices """
    print("\n🔹 Sparse Matrix Calculator 🔹")

    # Get file paths from the user
    file1 = input("Enter the file path for the first matrix: ").strip()
    file2 = input("Enter the file path for the second matrix: ").strip()

    try:
        matrix1 = SparseMatrix(file1)
        matrix2 = SparseMatrix(file2)

        while True:
            print("\nChoose an operation:")
            print("1️⃣ Addition")
            print("2️⃣ Subtraction")
            print("3️⃣ Multiplication")
            print("4️⃣ Exit")

            choice = input("Enter your choice (1/2/3/4): ").strip()

            if choice == "1":
                result = matrix1.add(matrix2)
                operation = "Addition"
            elif choice == "2":
                result = matrix1.subtract(matrix2)
                operation = "Subtraction"
            elif choice == "3":
                result = matrix1.multiply(matrix2)
                operation = "Multiplication"
            elif choice == "4":
                print("Exiting program. Goodbye! 👋")
                break
            else:
                print("⚠️ Invalid choice! Please enter 1, 2, 3, or 4.")
                continue

            # Print and save result
            print_matrix(result)
            result.save_to_file("result.txt")
            print(f"✅ {operation} result saved in 'result.txt'.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
