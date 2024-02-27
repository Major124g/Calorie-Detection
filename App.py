import streamlit as st
from PIL import Image
import requests
from bs4 import BeautifulSoup
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import time
from supa import *
from cameraSave import *

model = load_model('MODEL.h5')


# labels = {0: 'apple_pie', 1:'chocolate_cake', 2:'dumplings', 3:'fried_rice', 4:'omelette', 
#           5:'chicken_curry', 6:'donuts', 7:'french_fries', 8:'ice_cream', 9:'pizza', 10:'samosa', 11:'spaghetti'}
labels= {0:'apple_pie',1: 'chicken_curry',2: 'chocolate_cake', 
         3:'donuts',4: 'dumplings',5: 'french_fries',
         6:'fried_rice',7:'ice_cream',8: 'omelette',
         9:'pizza',10:'samosa',11:'spaghetti'}

def fetch_calories(prediction):
    try:
        url = 'https://www.google.com/search?&q=calories in '+prediction
        # https://www.google.com/search?q=calories in'+ prediction+'&hl={}'
        req = requests.get(url).text
        scrap = BeautifulSoup(req, 'html.parser')
        calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return calories
    except Exception as e:
        st.error("Can't able to fetch the Calories")
        print(e)


def prepare_image(img_path):
    img = load_img(img_path, target_size=(224, 224, 3))
    img = img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, [0])
    answer = model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    print(res)
    return res.capitalize()


def run():
    st.title("Calorie Detection System Using Image Processing")

    weight_data = fetch_weight_data()  # Call fetch_weight_data to get weight data
    
    st.image("welcome.jpg")
    st.write("""Welcome to the Calorie Detection system - the fast and easy way to identify 
             the calories in different types of food we consume in a daily basis. 
             This project named "Calorie Detection System Using Image Processing"
              is a major project from BEI076.The model is trained on a large dataset 
             of annotated food images, and is capable of detecting calories of some 
             foods like apple_pie, donuts, dumplings, chocolate_cake etc. """)
    
    x = abs(display_weight_data(weight_data))
    st.subheader(f"Click 'Capture Image' to Detect the food")

    #Call CameraSave1.py here
    #main()

    img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
    if img_file is not None:
        img = Image.open(img_file).resize((250, 250))
        st.image(img, use_column_width=False)
        save_image_path = './upload_images/' + img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        if st.button("Predict"):
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                    time.sleep(0.001)
                    my_bar.progress(percent_complete +
                                        1, text=progress_text)    
            if img_file is not None:
                result = prepare_image(save_image_path)
                
                st.success("**Predicted : " + result + '**')
                
                # st.warning("The given weight is equals to "+str(x)+" gm.")
                st.success("The given weight is equals to "+str(x) +" gm.")

                if result=='Apple_pie':
                    #st.warning("Calories : 237 Kcal(100gm)")
                    st.warning("The total calorie in the given Apple_pie is="+ str(x*2.37))
                elif result=='Chicken_curry':
                    #st.warning("Calories : 110 Kcal(100gm)")
                    st.warning("The total calorie in the given Chicken curry="+ str(x*1.1))
                elif result=='Chocolate_cake':
                    #st.warning("Calories : 371 Kcal(100gm)")
                    st.warning("The total calorie in the given Chocolate_cake is="+ str(x*3.71))
                elif result=='Donuts':
                    #st.warning("Calories : 412 Kcal(100gm)")
                    st.warning("The total calorie in the given Donuts is="+ str(x*4.12))
                elif result=='Dumplings':
                    #st.warning("Calories : 124 Kcal(100gm)")
                    st.warning("The total calorie in the given Dumplings is="+ str(x*1.24))
                elif result=='French_fries':
                    #st.warning("Calories : 296 Kcal(100gm)")
                    st.warning("The total calorie in the given French Fries is="+ str(x*2.96))
                elif result=='Fried_rice':
                    #st.warning("Calories : 168 Kcal(100gm)")
                    st.warning("The total calorie in the given Fried rice is="+ str(x*1.68))
                elif result=='Ice_cream':
                    #st.warning("Calories : 201 Kcal(100gm)")
                    st.warning("The total calorie in the given Ice-cream is="+ str(x*2.01))
                elif result=='Omelette':
                    #st.warning("Calories : 153 Kcal(100gm)")
                    st.warning("The total calorie in the given Omelette is="+ str(x*1.53))
                elif result=='Pizza':
                    #st.warning("Calories : 301 Kcal(100gm)")
                    st.warning("The total calorie in the given Pizza is="+ str(x*3.01))
                elif result=='Samosa':
                    #st.warning("Calories : 308 Kcal(100gm)")
                    st.warning("The total calorie in the given Samosa is="+ str(x*3.08))
                elif result=='Spaghetti':
                    #st.warning("Calories : 155 Kcal(100gm)")
                    st.warning("The total calorie in the given Spaghetti is="+ str(x*1.55))
                else:
                    st.warning("Out of Dataset.")


run()
