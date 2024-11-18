#face password
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import logging
logging.getLogger("deepface").setLevel(logging.ERROR)
logging.basicConfig(level=logging.ERROR)
from deepface import DeepFace

def check_validaty():

    try:

        pattern = (r"/home/soren/Pictures/images/pattern.jpg")
        image = (f"/home/soren/Pictures/images/key.jpg")

        result = DeepFace.verify(image, pattern)

        if result["verified"] == True:
            #log.write_log(True)
            os.remove(image)
            return True
        
        else:
            #log.write_log(False)
            return False
    
    except:
        return False