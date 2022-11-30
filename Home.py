import streamlit as kp
import backe

todos = backe.todo_open()
kp.set_page_config(layout='wide')
def adds_todo():
    newt=kp.session_state['newto']+'\n'
    todos.append(newt)
    backe.todo_write(todos)

kp.title('My Todo App')
kp.write("<b>App increases that increases productivity</b>",unsafe_allow_html=True)
kp.subheader('My Todo App')
kp.text_input(label='',placeholder='add a todo',on_change=adds_todo,key='newto')

for index,todo in enumerate(todos):
    checkbox=kp.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        backe.todo_write(todos)
        del kp.session_state[todo]
        kp.experimental_rerun()

