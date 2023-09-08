import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    #when user writed new to-d0
    # below retrieves what the user wrote
    new_todo = st.session_state["new_todo"] +'\n'
    todos.append(new_todo)
    functions.write_todos(todos)

st.title("To-Do App")
st.write("Increase your productivity.")

todos = functions.get_todos()


for index, each in enumerate(todos):
    #adding key, so when clicked, action is recorded; know what they clicked
    #every to-do will have their own key
    checkbox = st.checkbox(each, key=each)

    #when a checkbox is clicked (true);
    #remove the item
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)

        #removes the item from the web dictionary
        del st.session_state[each]

        #
        st.experimental_rerun()



#when writing a new to-do and enter, it goes to function add_todo
#when they write down, key associated to this is "new_todo which will store what the user wrote there
st.text_input(label=' ', placeholder="Add a new to-do...", on_change=add_todo, key='new_todo')

