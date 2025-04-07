This project implements a Sparse Matrix class in Python that supports:
-Matrix Addition
-Matrix Subtraction
-Matrix Multiplication
-File Input/Output Handling
-User Interaction for Matrix Operations

The program reads matrices from text files and allows users to perform operations through an interactive menu.

I used Git Large File Storage (LFS) to manage the large files for them to be pushed to my github. 

How to Run the Program

1- Navigate to the Project Directory
cd /dsa/sparse_matrix/code/src/

2- Run the Program
python main.py
An interactive menu will be displayed, giving clear instructions. 

You will be prompted to enter the file paths for two matrices. Then, you can choose an operation:

Choose an operation:
1️⃣ Addition
2️⃣ Subtraction
3️⃣ Multiplication
4️⃣ Exit

The result is displayed and saved in result.txt.

If an invalid operation is selected, an error message is shown.


Features

✅ Sparse Matrix Representation – Uses a dictionary to store only nonzero values.
✅ Error Handling – Prevents invalid operations and handles incorrect file formats.
✅ Interactive CLI Menu – Asks users which operation they want to perform.
✅ File I/O – Reads matrices from files and saves results to result.txt.


Example Usage

Input Matrices (matrix1.txt & matrix2.txt)

matrix1.txt:

rows=2
cols=3
(0,0,3)
(0,2,5)
(1,1,7)

matrix2.txt:

rows=2
cols=3
(0,0,1)
(0,1,4)
(1,2,2)

Running the Program

Enter the file path for the first matrix: sample_inputs/matrix1.txt
Enter the file path for the second matrix: sample_inputs/matrix2.txt
Choose an operation:
1️⃣ Addition

Output (Addition Result)

Matrix (2 x 3):
4 4 5
0 7 2

The result is also saved in result.txt.

Error Handling

⚠️ Invalid File Format – If the file format is incorrect, an error message will be displayed.
⚠️ Dimension Mismatch – If operations cannot be performed due to size mismatch, an error is shown.
⚠️ Invalid Input – If an incorrect menu option is chosen, the program will prompt the user again.


Notes

Ensure input files follow the correct format.

Addition and subtraction require matrices of the same dimensions.

Multiplication requires the first matrix’s columns to match the second matrix’s rows.


