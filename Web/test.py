import streamlit as st
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random
import restart as res
from QQ import Group_function
import pickle
import copy

# 初始化所需存储状态
if "uploaded_file" not in st.session_state:
    st.session_state["uploaded_file"] = None
if "unit_list" not in st.session_state:
    st.session_state["unit_list"] = []
if "unit_list" in st.session_state:
    unit_list = st.session_state["unit_list"]
if "df" not in st.session_state:
    st.session_state["df"] = None
if "df1" not in st.session_state:
    st.session_state["df1"] = None
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
        attacker = st.selectbox('请选择进攻人员',st.session_state['df']['姓名'])
        name_list = st.session_state['df']['姓名'].tolist()
        n1 = name_list.index(attacker)
        attackee = st.selectbox('请选择防守人员',st.session_state['df']['姓名'])
        name_list = st.session_state['df']['姓名'].tolist()
        n2 = name_list.index(attackee)
        if st.button('吸血（演示事例）'):
            melee = res.attribution(valuable=True,limit=[0,999],value=5)
            hp = res.attribution(valuable=True,limit=[0,20],value=10)
            def blood_steal_realize(owner,repeat,world_status):
                if world_status['event_id_now'] == after_attack.id:
                    if world_status['attacker'] == owner:
                        res.universal_id_dict[owner].attribution_dict[hp.id].add_value(world_status['damage'],world_status)
                return 0,world_status
            blood_steal_atom = res.atom(blood_steal_realize)
            def damage_settlement(owner,repeat,world_status):
                if world_status['event_id_now'] == attack.id:
                    res.universal_id_dict[world_status['attackee']].attribution_dict[hp.id].add_value(-world_status['damage'],world_status)
                return 0,world_status
            damage_atom = res.atom(damage_settlement)
            attack = res.event()
            after_attack = res.event()
            do_attack = res.action(reg_atom_dict={attack.id:[damage_atom.id]},event_list=[attack.id,after_attack.id])
            player1 = unit_list[n1]
            p1 = copy.deepcopy(player1)
            p1.after_deepcopy()
            player2 = unit_list[n2]
            blood_steal = res.attribution(valuable=False,reg_atom_dict={after_attack.id:[blood_steal_atom.id]})
            p1.after_change_attribution_dict()
            p1.attribution_dict[blood_steal.id].attach()
            p2 = copy.deepcopy(player2)
            p2.after_deepcopy()
            p1.act(do_attack.id,{'attacker':p1.id,
                                'attackee':p2.id,
                                'damage':p1.attribution_dict[melee.id].value})
            st.write(p1.attribution_dict[hp.id].__dict__)
            st.write(p2.attribution_dict[hp.id].__dict__)
    #hp_now = st.slider('目前血量',0,hp,hp)

# 添加单位函数
def add_unit(unit):
    unit_list.append(unit)
    st.session_state["unit_list"] = unit_list
    df = pd.DataFrame([[e.id,e.description['name']] 
                    for e in st.session_state["unit_list"]], columns=['id','姓名'])
    st.dataframe(df)
    st.session_state['df'] = df
    res.universal_id_dict[unit.id]=unit
    res.attribution_model_dict[hp.id]=hp

def del_unit(name):
    name_list = st.session_state['df']['姓名'].tolist()
    n = name_list.index(name)
    unit_list.pop(n)
    st.session_state["unit_list"] = unit_list
    df = pd.DataFrame([[e.id,e.description['name']] 
                       for e in st.session_state["unit_list"]], columns=['id','姓名'])
    st.session_state['df'] = df

# 显示单位列表函数
def show_unit_list():
    if len(st.session_state["unit_list"]) == 0:
        st.write('角色列表为空！')
    else:
        n=list(st.session_state["unit_list"][0].attribution_dict.keys())
        df = pd.DataFrame([[e.id,e.description['name'],e.attribution_dict[n[0]].value] 
                    for e in st.session_state["unit_list"]], columns=['id','姓名','hp'])
        st.dataframe(df)
        st.session_state['df'] = df
          
# 添加单位界面
def add_unit_page():
    st.subheader('添加新角色')
    name_text = st.text_input('姓名')
    limit_num = st.number_input('上限',min_value=1,max_value=999999)
    value_num = st.number_input( '血量',min_value=0,max_value=limit_num)
    hp = res.attribution(valuable=True,limit=[0,limit_num],value=value_num)
    unit = res.unit(description={"name":name_text},init_attribution = {hp.id:{'value':hp.value}})
    unit.on_load()
    st.write(unit.attribution_dict[hp.id].value)
    if st.button('添加'):
        add_unit(unit)
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
    if st.button("保存"):
        game_list = [res.universal_id_dict,res.attribution_model_dict]
        with open('my_game.pickle','wb') as f:
            pickle.dump(game_list,f)
        
def load_game():
    with open('my_game.pickle','rb') as f:
        game_list = f

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