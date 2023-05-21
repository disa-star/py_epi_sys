import streamlit as st
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import restart as res

# 初始化所需存储状态
if "uploaded_file" not in st.session_state:
    st.session_state["uploaded_file"] = None
if "unit_list" not in st.session_state:
    st.session_state["unit_list"] = []
if "df" not in st.session_state:
    st.session_state["df"] = None

# 关于地图编辑的相关函数
def drawing():
    drawing_mode = st.sidebar.selectbox(
        "画图工具", ("point", "freedraw", "line", "rect", "circle", "transform")
    )

    stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
    if drawing_mode == 'point':
        point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
    stroke_color = st.sidebar.color_picker("Stroke color hex: ")
    bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
    if st.session_state["uploaded_file"] is not None:
        bg_image = st.session_state["uploaded_file"]


    # 画布设置
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        background_image=Image.open(bg_image) if st.session_state["uploaded_file"] else None,
        #update_streamlit=realtime_update,
        height=150,
        drawing_mode=drawing_mode,
        point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
        key="canvas",
    )

    # 本部分存在的问题有：画面可能会截断（时有时无的问题）、画出的图像无法导出
    #if canvas_result.image_data is not None:
        #st.image(canvas_result.image_data)
    #if canvas_result.json_data is not None:
        #objects = pd.json_normalize(canvas_result.json_data["objects"]) # need to convert obj to str because PyArrow
        #for col in objects.select_dtypes(include=['object']).columns:
            #objects[col] = objects[col].astype("str")
        #st.dataframe(objects)

# 创建单位类
class Unit:
    def __init__(self, name, hp, position):
        self.name = name
        self.hp = hp
        self.position = position
    
def unit_battle():
    option = st.multiselect(
    '请选择战斗人员',
    st.session_state['df']['姓名'])
    pass
    #hp_now = st.slider('目前血量',0,hp,hp)

unit_list = st.session_state["unit_list"]

# 添加单位函数
def add_unit(name, hp, position):
    unit = Unit(name, hp, position)
    unit_list.append(unit)
    st.session_state["unit_list"] = unit_list
    df = pd.DataFrame([[e.name, e.hp, e.position] for e in st.session_state["unit_list"]], columns=['姓名', 'hp', '职业'])
    st.session_state['df'] = df

def del_unit(name):
    name_list = st.session_state['df']['姓名'].tolist()
    n = name_list.index(name)
    unit_list.pop(n)
    st.session_state["unit_list"] = unit_list
    df = pd.DataFrame([[e.name, e.hp, e.position] for e in st.session_state["unit_list"]], columns=['姓名', 'hp', '职业'])
    st.session_state['df'] = df


# 显示单位列表函数
def show_unit_list():
    if len(st.session_state["unit_list"]) == 0:
        st.write('角色列表为空！')
    else:
        df = pd.DataFrame([[e.name, e.hp, e.position] for e in st.session_state["unit_list"]], columns=['姓名', 'hp', '职业'])
        st.dataframe(df)
        st.session_state['df'] = df
        
        
# 添加单位界面
def add_unit_page():
    st.header('添加新角色')
    name = st.text_input('姓名')
    age = st.number_input('hp', min_value=0, max_value=100)
    position = st.text_input('职业')
    if st.button('添加'):
        add_unit(name, age, position)
        st.success('添加成功！')

def del_unit_page():
    st.header('删除角色')
    if st.session_state['df']['姓名'] is None:
        st.stop()
    option = st.selectbox('请选择需要删除的角色',st.session_state['df']['姓名'])
    if st.button('删除'):
        del_unit(option)
        st.success('删除成功！')

# 显示单位列表界面
def show_unit_list_page():
    st.write('角色列表')
    st.warning('请勿在添加后刷新页面以避免信息丢失', icon="⚠️")
    show_unit_list()

def upload_map():
    uploaded_file= st.file_uploader('地图文件',type=['jpg','png'])
    st.session_state["uploaded_file"] = uploaded_file
    if st.session_state["uploaded_file"] is not None:
        st.image(st.session_state["uploaded_file"])
    st.warning('请勿在添加后刷新页面以避免信息丢失', icon="⚠️")


# 主程序
def main():
    st.title('GM辅助系统')
    menu = ['角色编辑','角色战斗','地图上传','地图批注']
    choice = st.sidebar.selectbox('选择菜单', menu)
    if choice == '角色编辑':
        add_unit_page()
        del_unit_page()
        show_unit_list_page()
    elif choice == '地图上传':
        upload_map()
    elif choice == '角色战斗':
        unit_battle()
    else: drawing()



if __name__ == '__main__':
    main()