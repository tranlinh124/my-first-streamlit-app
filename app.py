import streamlit as st

st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')

a = st.number_input('Tham số a')
b = st.number_input('Tham số b')

if st.button('Giải'):
  if a!=0:
    x = -b/a
    result = "Phương trình có một nghiệm" + str(x)
  else:
    if b==0:
      result = 'Vô số nghiệm'
    if b!=0:
      result = 'Vô nghiệm'
  st.success(result, icon = '✌')


