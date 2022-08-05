import streamlit as st
import requests
import pickle
import ast

def main():
    st.title('Amazon Product Recommeder')
    product_list = pickle.load(open('product_list.pkl','rb'))
    product_list = set(product_list)
    input = st.selectbox('Enter the Product ID',product_list)
    if st.button('Recommend'):
        response = requests.get('http://localhost:8000/recommend?input={}'.format(input))
        data_temp = response.content.decode('UTF-8')
        data = ast.literal_eval(data_temp)
        for i in data:
            st.write(data[i])
            

if __name__ == '__main__':
    main()