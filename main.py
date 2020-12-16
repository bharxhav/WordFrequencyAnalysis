# Word Frequency Analysis
from TextSplitter import TextSplitter
from BatchMaker import BatchMaker
from FrequencyAnalyser import FrequencyAnalyser

if __name__ == '__main__':
    files = [
        "2001_ASpaceOdyssey.txt",
        "BladeRunner.txt",
        "Dune.txt",
        "FightClub.txt",
        "LoremIpsumFiller.txt",
        "MadMax.txt",
        "Matrix.txt",
        "Memento.txt",
        "StarWars_EmpireStrikesBack.txt"
    ]

    bm = BatchMaker(files)
    bm.write_batch()
    bm.create_folders()

    for f in files:
        print()
        print(f"Script :: {f}")

        movie = TextSplitter(f)
        movie.partition_words()
        movie.partition()

    for f in files:
        print()
        print(f"Script :: {f}")
        fs = FrequencyAnalyser(f)
        fs.analyse()
        fs.plot()
