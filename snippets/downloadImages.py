## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally

start = 1
stop = 54

range = range(start, stop+1)

for i in range:
    imageNumber = str(i).zfill(6)
    imageUrl = "https://recherche.archives.finistere.fr/viewer/index.php/show/full/medias/collections/M/06M/6M01/6M0544/FRAD029_6M_0544_06_" + imageNumber + ".jpg"
    filename = imageUrl.split("/")[-1]
    # Open the url image, set stream to True, this will return the stream content. add User-agent to simulate web browser (with human behind…) and avoid error
    r = requests.get(imageUrl, stream=True, headers={'User-agent': 'Mozilla/5.0'})
    # Check if the image was retrieved successfully
    if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
    # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')
        break
