import streamlit as st
import about
import mask_detection_app

# st.set_page_config(
#         page_title="Mask Detection APP",
#         # page_icon="",
#         layout="wide",
#         initial_sidebar_state="expanded",
#         menu_items={
#             'About': "My Github Profile https://github.com/BintangRamadhan837"
#         }
#     )

pages = {
"About Project": about,
"Mask Detection": mask_detection_app
}

st.sidebar.title("Mask Detection")
selection = st.sidebar.selectbox("Pages", list(pages.keys()))
page =pages[selection]
page.main()