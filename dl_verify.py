import os


def verify_all_images(jpegfolder: str, lastpagenumber: int) -> bool:
    imagelist = os.listdir(jpegfolder)
    allimages = True
    for i in range(lastpagenumber):
        i += 1
        if str(i) + ".jpg" not in imagelist:
            allimages = False
    return allimages


def find_missing_images(jpegfolder: str, lastpagenumber: int) -> list[int]:
    imagelist = os.listdir(jpegfolder)
    missingints = []
    for i in range(1, lastpagenumber + 1):
        if str(i) + ".jpg" not in imagelist:
            missingints.append(i)
    return missingints


if __name__ == "__main__":
    print(find_missing_images("jpegtemp", 31))
