import streamlit as st
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random
import restart as res
from QQ import Group_function
import pickle

# 初始化 unit_list是universal_id_dict的暂存处 ; attr_list是attribution_model_dict的暂存处
if "unit_list" not in st.session_state:
    st.session_state["unit_list"] = []
if "unit_list" in st.session_state:
    unit_list = st.session_state["unit_list"]
if "attr_list" not in st.session_state:
    st.session_state["attr_list"] = []
if "attr_list" in st.session_state:
    attr_list = st.session_state["attr_list"]
# df是一个中间产物
if "df" not in st.session_state:
    st.session_state["df"] = None

# 保存游戏
def save_game():
    st.title("保存你的游戏")
    if st.button("保存"):
        res.universal_id_dict = st.session_state['unit_list']
        res.attribution_model_dict = st.session_state['attr_list']
        game_list = [res.universal_id_dict,res.attribution_model_dict]
        with open('my_game.pickle','wb') as f:
            pickle.dump(game_list,f)

# 加载游戏     
def load_game():
    with open('my_game.pickle','rb') as f:
        game_list = f
        res.universal_id_dict=game_list[0]
        res.attribution_model_dict=game_list[1]
# 以上两个部分旨在保存本系统最重要的两个大字典：res.universal_id_dict,res.attribution_model_dict
# 两个大字典中存在{ID:content}这样的映射关系，前者是角色的字典映射，后者是属性的映射

# 添加角色
def add_unit(unit,hp):
    res.universal_id_dict[unit.id]=unit
    res.attribution_model_dict[hp.id]=hp
    st.session_state['unit_list']=res.universal_id_dict 
    st.session_state['attr_list']=res.attribution_model_dict
    df = pd.DataFrame([[e.id,e.description['name']] 
                    for e in st.session_state['unit_list']], columns=['id','姓名'])
    st.session_state['df'] = df

def add_unit_page():
    st.subheader('添加新角色')
    name_text = st.text_input('姓名')
    limit_num = st.number_input('上限',min_value=1,max_value=999999)
    value_num = st.number_input( '血量',min_value=0,max_value=limit_num)
    if st.button('添加'):
        hp = res.attribution(valuable=True,limit=[0,limit_num],value=value_num)
        unit = res.unit(description={"name":name_text},init_attribution = {hp.id:{'value':hp.value}})
        add_unit(unit,hp)
        st.success('添加成功！')

# 删除角色
def del_unit(name):
    name_list = st.session_state['df']['姓名'].tolist()
    n = name_list.index(name)
    unit_list.pop(n)
    st.session_state["unit_list"] = unit_list
    res.universal_id_dict = st.session_state['unit_list']
    df = pd.DataFrame([[e.id,e.description['name']] 
                       for e in st.session_state["unit_list"]], columns=['id','姓名'])
    st.session_state['df'] = df
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

# 展示角色
def show_unit_list():
    if len(st.session_state["unit_list"]) == 0:
        st.write('角色列表为空！')
    else:
        df = pd.DataFrame([[e.id,e.description['name']] 
                           for e in st.session_state["unit_list"]], columns=['id','姓名'])
        st.dataframe(df)
        st.session_state['df'] = df
def show_unit_list_page():
    st.subheader('角色列表')
    st.warning('请勿在添加后刷新页面以避免信息丢失', icon="⚠️")
    show_unit_list()

# 地图展示
def upload_map():
    st.warning('请勿在添加后刷新页面以避免信息丢失', icon="⚠️")
    st.subheader('地图文件上传')
    uploaded_file= st.file_uploader('地图文件',type=['jpg','png'])
    st.session_state["uploaded_file"] = uploaded_file
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
    #fill_shape_color = st.sidebar.color_picker("图形填充颜色")
    if st.session_state["uploaded_file"] is not None:
        bg_image = Image.open(st.session_state["uploaded_file"])
        w = bg_image.width       #图片的宽
        h = bg_image.height      #图片的高
    

    # 画布设置
    canvas_result = st_canvas(
        #fill_color="rgba(0, 165, 0, 0.3)",  
        fill_color="rgba(165, 165, 165, 0.0)",
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
def unit_battle():
    st.subheader('战斗系统')
    if st.session_state['df'] is None:
        st.write('目前还没有创建任何人物')
        return
    
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

def add_atom():
    id = num_input()
    description = dict_input()
    func = paragraph_input()
    with open('temp.py','w') as f:
        context = f'''
import restart as res
import pickle
def temp(owner,repeat,world_status):
    {func}
    return 0,world_status

a = res.atom(temp,id={id},description = {description})
with open("{random_name}", "wb") as f:
    pickle.dump(a, f)
        '''
        f.write(context)
    os.run('temp.py')

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

