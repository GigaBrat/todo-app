import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Ljubi te brat, todo App")
st.subheader("Manje dodavaj, vise zavrsavaj.")
st.write("Never forget to dream big.")


for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ", placeholder="Add new todo: ",
              on_change=add_todo, key="new_todo")

