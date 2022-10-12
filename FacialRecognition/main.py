from encode import Encode
from recognition import Recognition
import json
import numpy as np

if __name__=='__main__':
    
    img_path = r'C:\Users\SURYA S\facial\FacialRecognition\Images'
    
    ch = int(input("1.Encode 2.Recognize "))
    if ch==1:
        enc = Encode(img_path)
        enc.names()
        enc.findEncodings()
        enc.save()
    else:
        with open('model.json') as f:
            data = json.load(f)
         
        eList = []
        cNames = data['classNames']
        for i in range(len(cNames)):
            eList.append(np.array(data['encodeList'][i]))
             
        
        rec = Recognition(eList, cNames)
        rec.recog()
    
    
    
    