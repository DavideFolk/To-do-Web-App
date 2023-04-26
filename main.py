import streamlit as st
import functions


def add_todo():
    todo_to_add = st.session_state["new_todo"] + "\n"
    todos.append(todo_to_add)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


todos = functions.get_todos()

st.title("My To Do app")
st.subheader("This is my amazing app.")
st.write("This app increase your <b>productivity</b>", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
