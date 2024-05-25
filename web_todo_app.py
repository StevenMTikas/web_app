import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state['new_todo'] + '\n'
    todos.append(todo_local)
    functions.write_todos(todos)

st.title('My Todo App')
st.subheader('This is my todo app, it really :blue[super cool] :sunglasses:', divider='rainbow')
st.write('This app is designed to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='Todo app input box', label_visibility='hidden', 
              placeholder='Add a todo here....', on_change=add_todo, key='new_todo')