# Word Frequency Analysis
from TextSplitter import TextSplitter
from BatchMaker import BatchMaker


if __name__ == '__main__':
    files = [
        "2001_ASpaceOdyssey.txt",
        "BladeRunner.txt",
        "Dune.txt",
        "FightClub.txt",
        # "Interstellar_Mandarin.txt",
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
        movie = TextSplitter(f)
        movie.partition_words()
        movie.partition()
