import pandas as pd
import numpy as np
import copy
import os
import time
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
#import random
import restart as res
#from QQ import Group_function
import pickle
from streamlit_ace import st_ace
from streamlit_option_menu import option_menu
from streamlit_extras.colored_header import colored_header
from streamlit_extras.customize_running import center_running
from streamlit_extras.no_default_selectbox import selectbox

path = "/Users/oscarchen/Documents/GitHub/py_epi_sys"
game_name = 'my_game.pickle'

## 所有变量后带0的都是临时变量
def create_id(name,defined_num):
    st.write(res.universal_id_dict)
    st.subheader('ID设置')
    @st.cache_resource
    def cache_id(): # 由于缓存只支持列表
        idl = [0]
        return idl
    idl = cache_id()
    id=idl[0]
    col1, col2 = st.columns(2)
    with col2:
        st.write(f'{name}的末尾固定是0{defined_num}')
        agree = st.checkbox('自动分配')
        if agree:
            id = 0
            flag = True
            st.write('已自动分配ID信息')
        else:
            flag = False
    with col1:
        id0 = st.number_input(f'请输入{name}ID:',value=0,min_value=0,max_value=999999,disabled=flag) 
        if st.button(f'确认输入{name}ID'):
            id = int(id0)
            idl.pop(0)
            idl.insert(0, id)
            st.success('输入成功！')
    return id

## 给所有类的描述输入窗口
def create_description(name):# 规避的方法就是column name不同
    st.subheader(f'{name}描述编辑')
    st.caption('''编辑前请先按左上角后按delete清空，表格大小可拖动调节，输入内容可单击编辑。
                    首行信息将用于侧栏展示。''')
    df = pd.DataFrame([{f"{name}键": "名称", f"{name}值":''},])
    description0 = st.experimental_data_editor(df,num_rows="dynamic",
                                               width=500,height=140)
    description = dict(description0.values[:]) 
    return description

## rad = register_atom_dict，提供事件和原子绑定的窗口
def event_atom_connection(name):
    df = pd.DataFrame([{f"{name}事件ID": "", f"{name}原子ID":''},])
    el_rad0 = st.experimental_data_editor(df,num_rows="dynamic",width=500,height=140)
    el_rad1 = el_rad0.values[:]
    el_rad = {}
    if st.button('确认事件原子连接'):
        for row in el_rad1:
            if row[0] not in el_rad:
                el_rad[row[0]] = [row[1]]
            else:
                el_rad[row[0]].append(row[1])
    return el_rad

## 事件列创建函数
def create_event_list(name):
    df0 = pd.DataFrame([{f"{name}事件ID列": ""}])
    el0 = st.experimental_data_editor(df0,num_rows="dynamic",width=300,height=140)
    el1 = el0.values[:]
    event_list0 = el1.tolist()
    event_list = [x for i in event_list0 for x in i]
    return event_list









## 一个自定义保存路径和游戏名的主页
def home_page():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('游戏加载与保存')
        path0 = st.text_input('请输入游戏加载保存路径')
        name0 = st.text_input('请输入游戏名称')
        game_name0 = name0 + '.pickle'
        if st.button('确认输入'):
            path,game_name = path0,game_name0
            return path,game_name
    with col2:
        st.subheader('事件编辑页面')

## 从底层重新开始搭建 添加原子的组件
def add_atom():
    id = create_id('原子',0)
    description = create_description('原子')
    st.subheader('程序录入')
    with open('model.py', 'r') as f:
        model_data = f.read()
        context = st_ace(value=model_data,language='python',
                         tab_size=4,auto_update=True,placeholder='Write your code here') 
    if st.button('确认输入程序'):
        with open('temp.py','w') as f:
            f.write(context)
        st.success('输入成功！')
    #st.write(id) 确认为0的时候
    if st.button('确认输入原子'):
        with open('temp.py','r') as f:
            temp = f.read()
        with open(os.path.join(path, game_name), "rb") as f:
            res.universal_id_dict = copy.deepcopy(pickle.load(f))
            res.ond()
        res.atom(func = temp,id = id,description = description)
        with open(os.path.join(path, game_name), "wb") as f:
            pickle.dump(res.universal_id_dict,f)
        center_running()
        st.success('原子装载成功！')
        time.sleep(1)
        st.experimental_rerun()

## 添加事件的组件
def add_event():
    col1, col2 = st.columns(2)
    with col1:
        id = create_id('事件',1)
        description = create_description('事件')
        if st.button('确认输入事件'):  
            with open(os.path.join(path, game_name), "rb") as f:
                res.universal_id_dict = copy.deepcopy(pickle.load(f))
                res.ond()
            res.event(id=id,description=description)
            with open(os.path.join(path, game_name), "wb") as f:
                pickle.dump(res.universal_id_dict,f)
            center_running()
            st.success('事件编写成功！')
            time.sleep(1)
            st.experimental_rerun()
    with col2:
        st.subheader('展示事件列栏目')
        selectbox([])
        pass

## 添加行动的组件
def add_action():
    col1, col2 = st.columns(2)
    with col1:
        id = create_id('行动',2)
        description = create_description('行动')
    with col2:
        st.subheader('行动注册')
        el_rad = event_atom_connection('行动')
        st.subheader('注册事件列')
        event_list = create_event_list('行动')
        if st.button('确认输入行动'):
            with open(os.path.join(path, game_name), "rb") as f:
                res.universal_id_dict = copy.deepcopy(pickle.load(f))
                res.ond()
            res.action(reg_atom_dict=el_rad,event_list=event_list,id=id,description=description)
            with open(os.path.join(path, game_name), "wb") as f:
                pickle.dump(res.universal_id_dict,f)
            center_running()
            st.success('行动创建成功！')
            time.sleep(1)
            st.experimental_rerun()

## 属性
def add_attribution():
    col1, col2 = st.columns(2)
    with col1:
        id = create_id('属性',3)
        description = create_description('属性')
        st.subheader('属性注册')
        el_rad = event_atom_connection('属性')
    with col2:
        valuable = st.checkbox('此属性为数值类属性')
        if valuable:
            limit_num = st.number_input('上限',min_value=1,max_value=999999)
            value_num = st.number_input('数值',min_value=0,max_value=limit_num)
            st.subheader('数值变动事件列')
            event_list_vc = create_event_list('数值变动')
            st.subheader('上限变动事件列')
            event_list_lc = create_event_list('上限变动')
            if st.button('确认输入属性'):
                # 待调整
                with open(os.path.join(path, game_name), "rb") as f:
                    res.universal_id_dict = copy.deepcopy(pickle.load(f))
                    res.ond()
                res.attribution(valuable = True,limit = limit_num, value = value_num,reg_atom_dict=el_rad,owner=None,event_list_on_value_change=event_list_vc,event_list_on_limit_change=event_list_lc,attach_ctn=None,id=id,description=description)
                with open(os.path.join(path, game_name), "wb") as f:
                    pickle.dump(res.universal_id_dict,f)
                center_running()
                st.success('数值属性创造成功！')
                time.sleep(1)
                st.experimental_rerun()
        else:
            if st.button('确认输入属性'):
                with open(os.path.join(path, game_name), "rb") as f:
                    res.universal_id_dict = copy.deepcopy(pickle.load(f))
                    res.ond()
                res.attribution(valuable = False, reg_atom_dict=el_rad,owner=None,attach_ctn=None,id=id,description=description)
                with open(os.path.join(path, game_name), "wb") as f:
                    pickle.dump(res.universal_id_dict,f)
                center_running()
                st.success('非数值属性创造成功！')
                time.sleep(1)
                st.experimental_rerun()

# 角色
def add_unit():
    col1, col2 = st.columns(2)
    with col1:
        id = create_id('角色',4)
        description = create_description('角色')
        # init_attribution / attribution_dict
        if st.button('确认输入角色'):
            with open(os.path.join(path, game_name), "rb") as f:
                res.universal_id_dict = copy.deepcopy(pickle.load(f))
                res.ond()
            res.unit(id=id,description=description)
            with open(os.path.join(path, game_name), "wb") as f:
                pickle.dump(res.universal_id_dict,f)
            center_running()
            st.success('角色编写成功！')
            time.sleep(1)
            st.experimental_rerun()
    with col2:
        st.subheader('角色模版') # 和许睿确定拷贝的细则
        a0 = file_seeker('角色拷贝',4)
        if st.button('确认拷贝角色'):
            with open(os.path.join(path, game_name), "rb") as f:
                res.universal_id_dict = copy.deepcopy(pickle.load(f))
                res.ond()
            if a0 is not None:
                a = res.unit(copy.deepcopy(res.universal_id_dict[a0[0]]))
                a.after_deepcopy()
            with open(os.path.join(path, game_name), "wb") as f:
                pickle.dump(res.universal_id_dict,f)
            center_running()
            st.success('角色拷贝成功！')
            time.sleep(1)
            st.experimental_rerun()
        # selectbox('请选择角色模版',unit_menu)
        # 角色模板
        # 角色属性初始化

def upload_map():
    st.warning('请勿在添加后刷新页面以避免信息丢失', icon="⚠️")
    st.subheader('地图文件上传')
    uploaded_file= st.file_uploader('地图文件',type=['jpg','png'])
    st.session_state["uploaded_file"] = uploaded_file
# 地图
def add_map():
    upload_map()
    st.subheader('地图编辑')
    drawing_mode = st.sidebar.selectbox(
        "画图工具", ("point", "freedraw", "line", "rect", "circle", "transform")
    )
    stroke_width = st.sidebar.slider("画笔宽度：", 1, 25, 3)
    if drawing_mode == 'point':
        point_display_radius = st.sidebar.slider("点圈半径：", 1, 25, 3)
    stroke_color = st.sidebar.color_picker("画笔颜色 ")
    bg_color = st.sidebar.color_picker("背景颜色", "#eee")
    #fill_shape_color = st.sidebar.color_picker("图形填充颜色")
    if st.session_state["uploaded_file"] is not None:
        bg_image = Image.open(st.session_state["uploaded_file"])
        w = bg_image.width       #图片的宽
        h = bg_image.height      #图片的高
    # 画布设置
    canvas_result = st_canvas(
        #fill_color="rgba(0, 165, 0, 0.3)",  # Fixed fill color with some opacity
        fill_color="rgba(240, 240, 240, 0.2)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        background_image= bg_image if st.session_state["uploaded_file"] else None,
        update_streamlit=True,
        height = h if st.session_state["uploaded_file"] else None,
        width = w if st.session_state["uploaded_file"] else None,
        #height = st.slider('高度',100,1000,step = 100),
        #width = st.slider('宽度',100,1000,step = 100),
        drawing_mode=drawing_mode,
        point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
        key="canvas",
    )
# 游戏界面
def battle():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('请选择行动')
        a0 = file_seeker('开始行动（在此之前，确保你已经创建了事件和动作）',2)
        a = None
        if a0 is not None:
            a = res.universal_id_dict[a0[0]]
        action_owner_id = st.number_input('绑定实施者',0,999999)
        dfao = pd.DataFrame([{"世界状态": "", "传入ID":''},])
        description0 = st.experimental_data_editor(dfao,num_rows="dynamic",
                                                width=500,height=140)
        description_oid = dict(description0.values[:]) 
        if st.button('进行游戏'):
            with open(os.path.join(path, game_name), "rb") as f:
                res.universal_id_dict = copy.deepcopy(pickle.load(f))
                res.ond()
            if a is not None:
                a.do(owner_id=action_owner_id,world_status=description_oid)
            else:
                st.write('请添加事件')
            with open(os.path.join(path, game_name), "wb") as f:
                pickle.dump(res.universal_id_dict,f)
            st.success('游戏进行成功！')
            center_running()
            time.sleep(1)
            st.experimental_rerun()
    with col2:
        result_menu=[]
        for _ in res.universal_id_dict.keys():
            if _[-1] == 4:
                menu_id = res.universal_id_dict[_].id
                menu_name = res.universal_id_dict[_].description
                menu_attribution = res.universal_id_dict[_].attribution_dict[hp.id].__dict__
                result_menu.append([menu_id,menu_name,menu_attribution])
                '''{'valuable': True, 'reg_atom_dict': [], 'limit': [0, 35], 'value': 28, 'event_list_on_value_change': {}, 'event_list_on_limit_change': {}, 'owner': 204, 'attach_ctn': 1, 'num': 3, 'id': 103}
{'valuable': True, 'reg_atom_dict': [], 'limit': [0, 35], 'value': 14, 'event_list_on_value_change': {}, 'event_list_on_limit_change': {}, 'owner': 304, 'attach_ctn': 1, 'num': 3, 'id': 103}'''
        st.write(result_menu)
        #selected_action = selectbox('开始行动（在此之前，确保你已经创建了事件和动作）',action_menu)
        #if selected_action is not None:
            #file = f'{selected_action["id"]}.pickle'

# 文件查找函数
def file_seeker(name,defined_num):
    menu=[]
    for _ in res.universal_id_dict.keys():
        if _ % 100 == defined_num:
            menu_id = res.universal_id_dict[_].id
            menu_name = res.universal_id_dict[_].description
            menu.append([menu_id,menu_name])
    a0 = selectbox(f'{name}',menu)
    return a0

# 主程序
def main():
    with st.sidebar:
        selected = option_menu('GM辅助系统', ['首页',"原子建构", "事件建构", "行动建构", '属性建构','角色建构','地图建构','游戏页面'], 
        icons=['house','gear','hourglass-split', 'arrows-move', "bookmark",'people','map','boxes'], 
        menu_icon="cast", default_index=0)
        file_seeker("原子",0)
        file_seeker("事件",1)
        file_seeker("行动",2)
        file_seeker("属性",3)
        file_seeker("角色",4)
    if selected == '首页':
        colored_header(label="GM辅助系统",description="一款自定义TRPG辅助工具系统，首页具有刷新功能",color_name="violet-70",)
        home_page() # 发布后启用的功能
        res.universal_id_dict={}
        with open(os.path.join(path, game_name), "wb") as f:
            pickle.dump(res.universal_id_dict,f)
    elif selected == '原子建构':
        colored_header(label="原子建构",description="用于存放实现逻辑处理的函数，其中的函数负责处理world_status字典",color_name="red-70",)
        add_atom()
    elif selected == '事件建构':
        colored_header(label="事件建构",description="用于储存由atom所存储的函数的列表，在使用event.run()方法时，该类会依次调用所有他存储的函数",color_name="blue-green-70",)
        add_event()
    elif selected == '行动建构':
        colored_header(label="行动建构",description="用于存储一个执行的动作，负责存储一个event列表，在action.do()时依次对其中的event使用event.run()",color_name="green-70",)
        add_action()
    elif selected == '属性建构':
        colored_header(label="属性建构",description="用于存储所有的附着在人物身上的属性组成的一个event列表，在改变时，对列表中每个event依次使用event.run()",color_name="blue-70",)
        add_attribution()
    elif selected == '角色建构':
        colored_header(label="角色建构",description="负责挂载许多attirbution的深拷贝，是执行action的主体",color_name="light-blue-70",)
        add_unit()
    elif selected == '地图建构':
        colored_header(label="地图建构",description="可编辑的地图导入和导出",color_name="yellow-70",)
        add_map()
    elif selected == '游戏页面':
        colored_header(label="游戏页面",description="各类角色交互的页面",color_name="orange-70",)
        battle()
    
    #choice = st.sidebar.selectbox('选择菜单', menu)

if __name__ == '__main__':
    main()

#st.write(description)
    #des_name = st.text_input('描述名：')
    #description = None
    #description = dict([(f'{des_name}',st.text_input('内容：'))])

        #unit_menu=[]
        #for file in os.listdir(path):
            #if file.endswith("04.pickle") and file[:-7].isdigit():
                #with open(os.path.join(path, file), "rb") as f:
                    #res.universal_id_dict = pickle.load(f)
                    #unit_menu.append(a.description)