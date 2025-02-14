import os

class SparseMatrix:
    def __init__(self, file_path=None, num_rows=None, num_cols=None):
        if file_path:
            self.load_from_file(file_path)
        else:
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.data = {}

    def load_from_file(self, file_path):
        self.data = {}
        try:
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]
                
                if not lines[0].startswith("rows=") or not lines[1].startswith("cols="):
                    raise ValueError("Input file has wrong format")
                
                self.num_rows = int(lines[0].split('=')[1])
                self.num_cols = int(lines[1].split('=')[1])
                
                for line in lines[2:]:
                    if not (line.startswith("(") and line.endswith(")")):
                        raise ValueError("Input file has wrong format")
                    
                    row, col, value = map(int, line[1:-1].split(","))
                    self.data[(row, col)] = value
        except Exception as e:
            raise ValueError("Error reading file: " + str(e))

    def get_element(self, row, col):
        return self.data.get((row, col), 0)

    def set_element(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def add(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for addition")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        
        all_keys = set(self.data.keys()).union(other.data.keys())
        for key in all_keys:
            result.set_element(key[0], key[1], self.get_element(*key) + other.get_element(*key))
        
        return result

    def subtract(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for subtraction")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        
        all_keys = set(self.data.keys()).union(other.data.keys())
        for key in all_keys:
            result.set_element(key[0], key[1], self.get_element(*key) - other.get_element(*key))
        
        return result

    def multiply(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions do not match for multiplication")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        
        for (i, k), v1 in self.data.items():
            for j in range(other.num_cols):
                if (k, j) in other.data:
                    result.set_element(i, j, result.get_element(i, j) + v1 * other.get_element(k, j))
        
        return result

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(f"rows={self.num_rows}\n")
            file.write(f"cols={self.num_cols}\n")
            for (row, col), value in sorted(self.data.items()):
                file.write(f"({row}, {col}, {value})\n")





   