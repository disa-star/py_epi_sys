import streamlit as st
import restart as res
import pickle
import os

@st.cache_resource
def cache_id(): # 由于缓存只支持列表
    idl = [0]
    return idl

if st.button('确认输入原子'):
    id=0
    a = res.atom(func = 'def',id = id,description = None)  #唯一的区别
    path = "/Users/oscarchen/Documents/GitHub/py_epi_sys"
    with open(os.path.join(path, f"{a.id}.pickle"), "wb") as f:
        pickle.dump(a,f)
    st.success('原子装载成功！')
    st.experimental_rerun()
st.write(res.universal_id_dict)


'''@st.cache_resource
def cache_id():
    id = {}
    return id

id = cache_id()
input = st.text_input('输入：')
if st.checkbox('add 1'):
    id[input]=1
st.write(id)'''
'''
if st.checkbox('minus 1'):
    delete = st.selectbox('削除する要素を選択して下さい', options=id)
    if st.button('Delete'):
        lst.remove(delete)
        st.success(f'Delete : {delete}')'''
'''
if st.checkbox('change'):
    change_from = st.selectbox('変更する要素を選択して下さい', options=id)
    change_index = lst.index(change_from)
    change_to = st.text_input('何に変更しますか')
    if st.button('Change'):
        lst.remove(change_from)
        lst.insert(change_index, change_to)
        st.success(f'Change {change_from} to {change_to}')'''

