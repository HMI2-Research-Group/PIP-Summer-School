import shutil
import os
import pandas as pd


def get_angle_df(df):
    # Only leave columns with headers Time(s), AngleX(deg), AngleY(deg), AngleZ(deg)
    df = df[["Time(s)", "AngleX(deg)", "AngleY(deg)", "AngleZ(deg)"]]
    return df


def main():
    # check if HeadData folder exists, if not create it
    if not os.path.exists("HeadData"):
        os.mkdir("HeadData")
        os.mkdir("HeadData/Up")
        os.mkdir("HeadData/Down")
        os.mkdir("HeadData/Right")
        os.mkdir("HeadData/Left")
        os.mkdir("HeadData/Up/gyro")
        os.mkdir("HeadData/Down/gyro")
        os.mkdir("HeadData/Right/gyro")
        os.mkdir("HeadData/Left/gyro")
    else:
        shutil.rmtree("HeadData")
        os.mkdir("HeadData")
        os.mkdir("HeadData/Up")
        os.mkdir("HeadData/Down")
        os.mkdir("HeadData/Right")
        os.mkdir("HeadData/Left")
        os.mkdir("HeadData/Up/gyro")
        os.mkdir("HeadData/Down/gyro")
        os.mkdir("HeadData/Right/gyro")
        os.mkdir("HeadData/Left/gyro")

    # Read all txt file from YahboomHeadData/Up folder
    # and write to HeadData/Up folder
    for direction in ["Up", "Down", "Right", "Left"]:
        trial_number = 1
        for file in os.listdir(f"YahboomHeadData/{direction}/Gyro"):
            if file.endswith(".txt"):
                df = get_angle_df(pd.read_csv(f"YahboomHeadData/{direction}/Gyro/" + file, sep="\t", skiprows=1))
                df.to_csv(f"HeadData/{direction}/gyro/" + f"trial{trial_number}.csv", index=False, header=False)
                trial_number += 1


if __name__ == "__main__":
    main()
