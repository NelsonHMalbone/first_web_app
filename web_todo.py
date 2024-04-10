import functions
import streamlit as st

todos = functions.get_todos()


def add_todo():  # call back function for text input
    # this is key to be called to get the value which is store in new_todo
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)



st.title("My Todo App")
st.subheader("My first web app")

for index, todo in enumerate(todos):
    # add a key we can see it in the session state
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]  # user selects a to-do will update from session state
        st.experimental_rerun()

st.text_input(label="Enter Todos: ",
              placeholder="add to do here",
              on_change=add_todo, key="new_todo")

# leave up on dev of program but when finsh delete it
# st.session_state

