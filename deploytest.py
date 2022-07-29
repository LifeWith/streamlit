
import os 
import streamlit as st

try:
    # path 입력받기
    st.title('path를 입력하세요')
    path = st.text_input('예) C:\Sample\Python\merge')

    if st.button('하위 파일 조회'):
        if os.path.exists(path):
            # 해당 path의 파일 리스트 출력
            file_list = os.listdir(path) 
            st.write(file_list)
        else:
            st.write('경로를 확인하세요')

    #input("Press enter to exit ;)")
except Exception as e:
    print(e)
    input("Press enter to exit ;)")

#streamlit run deploytest.py