import sys, glob, io, os, re
from pathlib import Path

pre = "mbho"
raw_files = "./raw_ocr_files/*.txt"


def split_pages(f):
    volume = Path(f).stem.split("-")[-1].zfill(2)
    # Create a folder for the files if one doesn't exist
    Path("./"+pre+volume+"/").mkdir(parents=True, exist_ok=True)
    with open(f,"r") as i:
        buff = []
        p = r"=== sarala-mahabharata-"+volume+"output-\d+-to-(\d+)\.json =========================="
        outfile = os.path.join("mbho"+volume+"/","mbho-v"+volume+"-p001-ocr.txt")
        print(outfile)
        for line in i:
            l = line.strip()
            pagestart = re.findall(p,l)
            if len(pagestart) > 0:
                page = pagestart[0]
                if int(page) > 0:
                    with open(outfile,"w") as out:
                        out.write("".join(buff))
                        buff = []
                        outfile = os.path.join("mbho"+volume+"/","mbho-v"+volume+"-p"+page.zfill(3)+"-ocr.txt")
            else:
                if l:
                    buff.append(line)

if __name__ == "__main__":
    for f in glob.glob(raw_files):
        split_pages(f)
