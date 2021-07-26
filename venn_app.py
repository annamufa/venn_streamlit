import streamlit as st
from venn import venn, get_intersections
import re

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Venn plots')

st.text('You can choose the number of lists on the left, write the values and label them.')
st.text('Scroll down to get the intersection for your lists.')

n_venn = st.sidebar.selectbox(
    "How many lists do you have?",
    (2,3,4)
)

separator = st.sidebar.selectbox(
    "What separator?",
    (",", "space or tab")
)

if separator == ",":
    collect_list = lambda x: [i for i in re.split(",", x) if i != ""]
else:
    collect_list = lambda x: [i for i in re.split(" ", x) if i != ""]

list_1 = collect_list(st.sidebar.text_input("List 1"))
list_2 = collect_list(st.sidebar.text_input("List 2"))
lists = [list_1, list_2]

if n_venn > 2:
    list_3 = collect_list(st.sidebar.text_input("List 3"))
    lists.append(list_3)
    if n_venn == 4:
        list_4 = collect_list(st.sidebar.text_input("List 4"))
        lists.append(list_4)

labels = collect_list(st.sidebar.text_input("List labels (in order)"))[:n_venn]

if len(labels)<n_venn:
    labels = ["List 1", "List 2", "List 3", "List 4"][:n_venn]

fig = venn(data=lists, names=labels, colors = ["palevioletred", "darkseagreen", "cornflowerblue","navajowhite"][:n_venn])
st.pyplot(fig)

intersections = st.multiselect("Choose lists to interesect: ",
                         (labels))
if len(intersections)<2:
    st.text("Choose at least two lists")

else:
    lists_label = dict(zip(intersections, lists))

    a = st.selectbox("",
             (intersections))

    operator_1 = st.selectbox("",
                 ("and", "without"))
    b = st.selectbox("",set(intersections)-set([a]), key = "labels_1")

    if operator_1 == "and":
        result = set(lists_label[a])&set(lists_label[b])
    else:
        result = set(lists_label[a]) - set(lists_label[b])


    if len(intersections)>2:
        operator_2 = st.selectbox("",
                                  ("and", "without"), key = "2")
        c = st.selectbox("",set(intersections)-set([a,b]), key = "labels_2")

        if operator_2 == "and":
            result = result&set(lists_label[c])
        else:
            result = result-set(lists_label[c])

        if len(intersections)==4:
            operator_3 = st.selectbox("",("and", "without"), key = "3")
            d = st.selectbox("",set(intersections)-set([a,b,c]), key = "labels_3")
            if operator_3 == "and":
                result = result & set(lists_label[d])
            else:
                result = result - set(lists_label[d])

    st.text(list(result))






