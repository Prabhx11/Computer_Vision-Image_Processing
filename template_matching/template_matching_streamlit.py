import cv2
import numpy as np
import streamlit as st
from PIL import Image
 

def match_template(img,temp):
    #w, h = temp.shape[::-1]
    res = cv2.matchTemplate(img,temp,cv2.TM_CCOEFF_NORMED)
    return res
    
    

def gray(img):
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return gray_img
    

def main_loop():
    st.title('Template Matching')
    st.subheader('find the match in images with just one click')
    og_img=st.file_uploader('Upload the image here:', type = ['png','jpeg','jpg'])
    #st.image(og_img)
    template=st.file_uploader('Upload the template here:', type = ['png','jpeg','jpg'])
    #st.image(template)
    if not og_img:
        return None

    if not template:
        return None
    #st.image(og_img,width=300)
    #st.image(template)
    cola, colb = st.columns(2)
    cola.subheader("image")
    cola.image(og_img, use_column_width=True)


    colb.header("template")
    colb.image(template, use_column_width=True)


    
    og_image1 = Image.open(og_img)
    og_image2 = np.array(og_image1)
    og_gray = gray(og_image2)
    
    temp = Image.open(template)
    temp = np.array(temp)
    temp=gray(temp)
    #w, h = temp.shape[::-1]
    #og_gray=np.uint8(og_gray)
    #temp = np.uint8(temp)
    #res = cv2.matchTemplate(og_gray,temp,cv2.TM_CCOEFF_NORMED)
    #permit=st.checkbox('MATCH')
    if st.button('MATCH'):
        
        res= match_template(og_gray,temp)
        threshold = 0.9
        loc = np.where( res >= threshold)
        w, h = temp.shape[::-1]
        for pt in zip(*loc[::-1]):
            cv2.rectangle(og_image2, pt, (pt[0] + w, pt[1] + h), (255,0,0), 20)
        #cv2_imshow(og_img)
        col1, col2 = st.columns(2)
        col1.header("image")
        col1.image(og_image2, use_column_width=True)


        col2.header("template")
        col2.image(template, use_column_width=True)
#img = cv2.imread('/content/many_objects.jpg')


#template = cv2.imread('/content/one_object.jpg', 0 )


if __name__ == '__main__':
    main_loop()
