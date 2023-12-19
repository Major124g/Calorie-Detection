import streamlit as st
from PIL import Image
import requests
from bs4 import BeautifulSoup
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import time

model = load_model('MODEL.h5')


# labels = {0: 'apple_pie', 1:'chocolate_cake', 2:'dumplings', 3:'fried_rice', 4:'omelette', 
#           5:'chicken_curry', 6:'donuts', 7:'french_fries', 8:'ice_cream', 9:'pizza', 10:'samosa', 11:'spaghetti'}
labels= {0:'apple_pie',1: 'chicken_curry',2: 'chocolate_cake', 
         3:'donuts',4: 'dumplings',5: 'french_fries',
         6:'fried_rice',7:'ice_cream',8: 'omelette',
         9:'pizza',10:'samosa',11:'spaghetti'}
# labels = {0: 'apple', 1: 'banana', 2: 'beetroot', 3: 'bell pepper', 4: 'cabbage', 5: 'capsicum', 6: 'carrot',
#           7: 'cauliflower', 8: 'chilli pepper', 9: 'corn', 10: 'cucumber', 11: 'eggplant', 12: 'garlic', 13: 'ginger',
#           14: 'grapes', 15: 'jalepeno', 16: 'kiwi', 17: 'lemon', 18: 'lettuce',
#           19: 'mango', 20: 'onion', 21: 'orange', 22: 'paprika', 23: 'pear', 24: 'peas', 25: 'pineapple',
#           26: 'pomegranate', 27: 'potato', 28: 'raddish', 29: 'soy beans', 30: 'spinach', 31: 'sweetcorn',
#           32: 'sweetpotato', 33: 'tomato', 34: 'turnip', 35: 'watermelon'}
# fruits = ['Apple', 'Banana', 'Bello Pepper', 'Chilli Pepper', 'Grapes', 'Jalepeno', 'Kiwi', 'Lemon', 'Mango', 'Orange',
#           'Paprika', 'Pear', 'Pineapple', 'Pomegranate', 'Watermelon']
# vegetables = ['Beetroot', 'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Corn', 'Cucumber', 'Eggplant', 'Ginger',
#               'Lettuce', 'Onion', 'Peas', 'Potato', 'Raddish', 'Soy Beans', 'Spinach', 'Sweetcorn', 'Sweetpotato',
#               'Tomato', 'Turnip']


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
    st.image("welcome.jpg")
    st.write("""Welcome to the Calorie Detection system - the fast and easy way to identify 
             the calories in different types of food we consume in a daily basis. 
             This project named "Calorie Detection System Using Image Processing"
              is a major project from BEI076.The model is trained on a large dataset 
             of annotated food images, and is capable of detecting calories of some 
             foods like apple_pie, donuts, dumplings, chocolate_cake etc. """)
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
                # if result in vegetables:
                #     st.info('**Category : Vegetables**')
                # else:
                #     st.info('**Category : Fruit**')
                st.success("**Predicted : " + result + '**')
                #cal = fetch_calories(result)
                # if cal:
                #     st.warning('**' + cal + '(100 grams)**')
                if result=='Apple_pie':
                    st.warning("Calories : 237 Kcal(100gm)")
                elif result=='Chicken_curry':
                    st.warning("Calories : 110 Kcal(100gm)")
                elif result=='Chocolate_cake':
                    st.warning("Calories : 371 Kcal(100gm)")
                elif result=='Donuts':
                    st.warning("Calories : 412 Kcal(100gm)")
                elif result=='Dumplings':
                    st.warning("Calories : 124 Kcal(100gm)")
                elif result=='French_fries':
                    st.warning("Calories : 296 Kcal(100gm)")
                elif result=='Fried_rice':
                    st.warning("Calories : 168 Kcal(100gm)")
                elif result=='Ice_cream':
                    st.warning("Calories : 201 Kcal(100gm)")
                elif result=='Omelette':
                    st.warning("Calories : 153 Kcal(100gm)")
                elif result=='Pizza':
                    st.warning("Calories : 301 Kcal(100gm)")
                elif result=='Samosa':
                    st.warning("Calories : 308 Kcal(100gm)")
                elif result=='Spaghetti':
                    st.warning("Calories : 155 Kcal(100gm)")
                else:
                    st.warning("Out of Dataset.")


run()
