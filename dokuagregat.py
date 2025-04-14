#spjbtlagregat



import glob
import os
from PIL import Image
from pdf2image import convert_from_path

# DIR=r"D:\AIL transfer\Anyer\2025\scan now"
listdok=["BA","PK","SPJBTL","SLO","SIP","PDL", "KTPNPWP", "SURVEY", "PMHN", "TOKEN"]
suffix=[".pdf","_1.pdf","_2.pdf","_3.pdf","_4.pdf","_5.pdf","_6.pdf","_7.pdf","_8.pdf","_9.pdf","_10.pdf","_11.pdf","_12.pdf","_13.pdf","_14.pdf","_15.pdf"]
awal= 1
akhir=500
for nomerail in range(awal,akhir+1):
    for dok in listdok:
        for suf in suffix[1:]:
            nompath=f"{nomerail}-{dok}{suf}"
            if os.path.exists(nompath):
                print(f"{nomerail} {dok} ada")
                listdoku=[]
                rpath=glob.glob(f"{nomerail}-{dok}*")
                for x in rpath :
                    if os.path.exists (x):
                        listdoku.append(x)
                print(listdoku)
                dokusaves=[]
                for dokusave in listdoku:
                    img=convert_from_path(dokusave,poppler_path=r"C:\ProgramData\anaconda3\envs\AIL\Library\bin", fmt="jpeg",jpegopt={'optimize':True,'progressive':False,'quality':50})
                    dokusaves.extend(img)
                if len(dokusaves)==0:
                    continue
                else:
                    # w,h=dokusaves[0].size
                    # wnew=2480
                    # r=h/w
                    # hnew=int(wnew*r)
                    # size=(wnew, hnew)
                    # print(size)
                    try:
                        dokusaves[0].save(f"{nomerail}-{dok}.pdf",save_all=True, append_images=dokusaves[1:],dpi=(150,150))
                    except (OSError, Image.UnidentifiedImageError) as e:
                # Handle the exception (e.g., skip the image)
                        print("Error processing image:", listdoku[0])
                        print("Skipping...")
                        continue
                dokusaves=[]
                print("berhasil gabung")
                break