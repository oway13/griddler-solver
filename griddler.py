import ast

class Griddler:
    solved = False

    def __init__(self, gridd_file):
        with open(gridd_file, 'r') as f:
            dimensions = ast.literal_eval(f.readline())
            row_reqs = ast.literal_eval(f.readline())
            col_reqs = ast.literal_eval(f.readline())
            gridd = f.readline()
        self.rows = dimensions[0]
        self.cols = dimensions[1]
        self.row_reqs = row_reqs
        self.col_reqs = col_reqs
        self.name = gridd_file
        if gridd:
            self.gridd = ast.literal_eval(gridd)
        else:
            self.gridd = [ [0]*self.cols for _ in range(self.rows) ]

    def save_to_file(self):
        if not self.solved:
            newname = self.name.replace("unsolved", "startsolved")
        else:
           newname = self.name.replace("unsolved", "solved") 
        with open(newname, 'w') as f:
            dimensions = [self.rows, self.cols]
            f.write(str(dimensions) + "\n")
            f.write(str(self.row_reqs) + "\n")
            f.write(str(self.col_reqs) + "\n")
            f.write(str(self.gridd))

def main():
    pear = Griddler("pear_small_unsolved.gridd")
    pear.save_to_file()

main()