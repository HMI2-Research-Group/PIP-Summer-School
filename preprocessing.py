import shutil
import os


def main():
    # check if HeadData folder exists, if not create it
    if not os.path.exists("HeadData"):
        os.mkdir("HeadData")
        os.mkdir("HeadData/Up")
        os.mkdir("HeadData/Down")
        os.mkdir("HeadData/Right")
        os.mkdir("HeadData/Left")
    else:
        shutil.rmtree("HeadData")
        os.mkdir("HeadData")
        os.mkdir("HeadData/Up")
        os.mkdir("HeadData/Down")
        os.mkdir("HeadData/Right")
        os.mkdir("HeadData/Left")


if __name__ == "__main__":
    main()
