import streamlit as st
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random
import restart as res
from QQ import Group_function


# 初始化所需存储状态
if "uploaded_file" not in st.session_state:
    st.session_state["uploaded_file"] = None
if "unit_list" not in st.session_state:
    st.session_state["unit_list"] = []
if "df" not in st.session_state:
    st.session_state["df"] = None
if "df1" not in st.session_state:
    st.session_state["df1"] = None
if "unit_list" in st.session_state:
    unit_list = st.session_state["unit_list"]
if "universal_id" not in st.session_state:
    st.session_state["universal_id"] = {}
if "ban_list" not in st.session_state:
    st.session_state['ban_list'] = []

# 关于地图编辑的相关函数
def drawing():
    st.subheader('地图编辑')
    drawing_mode = st.sidebar.selectbox(
        "画图工具", ("point", "freedraw", "line", "rect", "circle", "transform")
    )

    stroke_width = st.sidebar.slider("画笔宽度：", 1, 25, 3)
    if drawing_mode == 'point':
        point_display_radius = st.sidebar.slider("点圈半径：", 1, 25, 3)
    stroke_color = st.sidebar.color_picker("画笔颜色 ")
    bg_color = st.sidebar.color_picker("背景颜色", "#eee")
    fill_shape_color = st.sidebar.color_picker("图形填充颜色")
    if st.session_state["uploaded_file"] is not None:
        bg_image = Image.open(st.session_state["uploaded_file"])
        w = bg_image.width       #图片的宽
        h = bg_image.height      #图片的高
    

    # 画布设置
    canvas_result = st_canvas(
        #fill_color="rgba(0, 165, 0, 0.3)",  # Fixed fill color with some opacity
        fill_color=fill_shape_color or "rgba(0, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        background_image= bg_image if st.session_state["uploaded_file"] else None,
        #update_streamlit=realtime_update,
        height = h/3 if st.session_state["uploaded_file"] else None,
        width = w/3 if st.session_state["uploaded_file"] else None,
        #height = st.slider('高度',100,1000,step = 100),
        #width = st.slider('宽度',100,1000,step = 100),
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

def dice_roll():
    st.subheader("投掷骰子")
    st.write("点击投掷骰子")
    result = None
    if st.button("六面骰"):
        result = random.randint(1, 6)
    if st.button("八面骰"):
        result = random.randint(1, 8)
    if st.button("十面骰"):
        result = random.randint(1, 10)
    if st.button("二十面骰"):
        result = random.randint(1, 20)
    if result is not None:
        st.caption(f'本次投掷骰子的结果是{result}')

def unit_battle():
    st.subheader('战斗系统')
    if st.session_state['df'] is None:
        st.write('目前还没有创建任何事件')
        return
    else:
        option = st.multiselect(
    '请选择战斗人员',
    st.session_state['df']['姓名'])
    
    #hp_now = st.slider('目前血量',0,hp,hp)

class Unit():
    def __init__(self, name, hp, position):
        self.name = name
        self.hp = hp
        self.position = position

# 添加单位函数
def add_unit(name, hp, position):
    unit = Unit(name, hp, position)
    #unit = res.unit(init_attribution = {name:{name},hp:{hp},position:{position}})
    #st.write(unit)
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
    st.subheader('添加新角色')
    name = st.text_input('姓名')
    age = st.number_input('hp', min_value=0, max_value=9999999999)
    position = st.text_input('职业')
    if st.button('添加'):
        add_unit(name, age, position)
        st.success('添加成功！')

def del_unit_page():
    st.subheader('删除角色')
    if 'df' in st.session_state:
        if st.session_state['df'] is None:
            st.write('目前还没有创建任何角色')
            return
        else:
            option = st.selectbox('请选择需要删除的角色',st.session_state['df']['姓名'])
            if st.button('删除'):
                del_unit(option)
                st.success('删除成功！')

# 显示单位列表界面
def show_unit_list_page():
    st.subheader('角色列表')
    st.warning('请勿在添加后刷新页面以避免信息丢失', icon="⚠️")
    show_unit_list()

def upload_map():
    st.warning('请勿在添加后刷新页面以避免信息丢失', icon="⚠️")
    st.subheader('地图文件上传')
    uploaded_file= st.file_uploader('地图文件',type=['jpg','png'])
    st.session_state["uploaded_file"] = uploaded_file
    # 需要将文件上传到文件夹中才不会引起报错，否则会在切换页面后丢失信息

def save_game():
    st.title("保存你的游戏")
    st.write("输入你的备注")
    input_list = st.text_area("备注", "")
    if st.button("保存"):
        df = pd.DataFrame(st.session_state["df"], columns=[""])
        df.to_csv("output.csv", index=False)
        output_path = input("输入保存路径：")
        df.to_csv(output_path, index=False)
        st.write("成功导出为output.csv")

def load_game():
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state['df1'] = df
        st.write(st.session_state['df1'])

def qq_management():
    input_number = st.text_input("请输入QQ群号：")
    if st.button('加入'):
        qq = Group_function(input_number)
        if 'qq_flag' not in st.session_state:
            qq.Get_messgae_and_auto_reply()
            st.session_state['qq_flag'] = True
    if st.button('发送地图'):
        qq.G_picture(st.session_state["uploaded_file"])
    if st.button('发送信息'):
        qq.G_send(st.text_input)
    option1 = st.selectbox("禁言人员",qq.g_list)
    ban_list = st.session_state['ban_list']
    option2 = st.selectbox("解禁人员",ban_list)
    if st.button('禁言'):
        qq.G_ban(option1)
        ban_list.append(option1)
        st.session_state['ban_list'] = ban_list
    if st.button('解禁'):
        n = ban_list.index(option2)
        qq.G_ban_cancel(option2)
        ban_list.pop(n)   
        st.session_state['ban_list'] = ban_list
    
        

    # 主程序
def main():
    st.title('GM辅助系统')
    menu = ['角色编辑','角色战斗','地图编辑','QQ管理']
    choice = st.sidebar.selectbox('选择菜单', menu)
    if st.sidebar.button('保存游戏'):
        save_game()
    if st.sidebar.button('加载游戏'):
        load_game()
    if choice == '角色编辑':
        add_unit_page()
        del_unit_page()
        show_unit_list_page()
    elif choice == '地图编辑':
        upload_map()
        drawing()
    elif choice == '角色战斗':
        unit_battle()
        dice_roll()
    elif choice == 'QQ管理':
        qq_management()

if __name__ == '__main__':
    main()