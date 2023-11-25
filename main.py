import sys
import os
import zlib


def main():
    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/master\n")
        print("Initialized git directory")
    elif command == "cat-file":
        if sys.argv[2] == "-p" and sys.argv[3] is not None:
            # get all files in .git/objects
            files = os.listdir(".git/objects")
            print(sys.argv[3])
            print(files)

            for file in files:
                # get all files in .git/objects/{file}
                files2 = os.listdir(f".git/objects/{file}")
                for file2 in files2:
                    # check if file2 is the file we are looking for
                    if file2 == sys.argv[3]:
                        # print file2
                        with open(f".git/objects/{file}/{file2}", "rb") as f:
                            print(zlib.decompress(f.read()))
                            # print(f.read().decode())
            pass
            # with open(f".git/objects/{sys.argv[3][:2]}/{sys.argv[3][2:]}", "rb") as f:
            # print(f.read().decode())
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()

