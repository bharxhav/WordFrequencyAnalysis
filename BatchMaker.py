# Creates the Batch Files
import subprocess


class BatchMaker:
    def __init__(self, files, directory="H:\\Projects-DSP-Case_Study\\WordFrequencyAnalysis\\results"):
        self.files = files
        self.directory = directory

    def write_batch(self):
        adj = ["cd " + self.directory, ""]

        for f in self.files:
            adj.append('mkdir ' + f[:-4])

        fp = open('results/FolderMaker.bat', 'w')
        fp.write("\n".join(adj))
        fp.close()

        print("Written The Batch File")

    def create_folders(self):
        subprocess.run([self.directory+"\\FolderMaker.bat"], shell=True)

        print()
        print("Created Folders")
