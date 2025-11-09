import streamlit as st
from pathlib import Path
import helpers as hp

curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
logo_pic = curr_dir / "media" / "logo.png"
st.logo(logo_pic, size="large")


hp.emojiRain()
st.set_page_config(page_title="Karol Vincent", page_icon=logo_pic, layout="wide")
pg = st.navigation([st.Page("main.py",title="About Me"),st.Page("portfolio.py", title="Portfolio")], position="top")
pg.run()