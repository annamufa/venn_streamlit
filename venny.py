import streamlit as st
from venn import venn
import re

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('DDO a Venn')

collect_list = lambda x: [i for i in re.split(",", x) if i != ""]

n_venn = st.sidebar.selectbox(
    "How many lists?",
    (2,3,4)
)

list_1 = collect_list(st.text_input("List 1"))
list_2 = collect_list(st.text_input("List 2"))

if n_venn == 4:
    list_3 = collect_list(st.text_input("List 3"))
    list_4 = collect_list(st.text_input("List 4"))
    lists = [list_1, list_2, list_3, list_4]

elif n_venn == 3:
    list_3 = collect_list(st.text_input("List 3"))
    lists = [list_1, list_2, list_3]

else:
    lists = [list_1, list_2]

labels = collect_list(st.text_input("Labels"))

fig = venn(data=lists, names=labels)
st.pyplot(fig)
