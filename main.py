from pathlib import Path
import helpers as hp
import streamlit as st


curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
styles_css = curr_dir / "styles" / "styles.css"
wall_pic = curr_dir / "media" / "wall.png"
graduate_pic = curr_dir/ "media" /"graduate.png"
logo_pic = curr_dir / "media" / "logo.png"
dost_logo = curr_dir / "media" / "dost.png"
mythic_logo = curr_dir / "media" / "mythic_logo.png"
codechum_logo = curr_dir / "media" / "codechum.png"




st.set_page_config(page_title="Karol Vincent", page_icon=logo_pic, layout="wide")
st.logo(logo_pic, size="large")

with open(styles_css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


st.markdown(hp.getImage("media/profile.png"), unsafe_allow_html=True)

st.markdown(f'''
    <p style="text-align: center; display: block; color: #e5e8f3; font-size: 3.5em; font-weight: 800" >{hp.TITLE}</p>''', unsafe_allow_html=True)

st.space(size='small')
col1, col2 = st.columns([0.3, 0.7], border=True)
with col1:
    st.image(wall_pic, use_container_width=True)
    st.image(graduate_pic, use_container_width=True)
with col2:

    header_container = st.container(horizontal_alignment="center")
    with header_container:
        st.markdown(f'''
            <p style="text-align: center; color: #e5e8f3; margin-bottom:0;font-size: 1.5em; font-weight: 800" >{hp.NAME}</p>''',
            unsafe_allow_html=True)
        st.markdown(f'''
            <p style="text-align: center; margin: 0 auto 0;color: #e5e8f3; font-size: 0.8em; font-style: italic;font-weight: 400" >{hp.NAMESUB}</p>''',
            unsafe_allow_html=True)
        st.markdown(f'''
            <p style="text-align: justify; margin:0;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >{hp.NAMEH1}</p>''',
            unsafe_allow_html=True)
        st.markdown(f'''
            <p style="text-align: justify; margin:1rem 1.5rem 1rem;color: #e5e8f3; font-size: 1em;font-weight: 400" >{hp.CH1CONTENT}</p>''',
            unsafe_allow_html=True)
        st.markdown(f'''
            <p style="text-align: justify; margin:0;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >{hp.NAMEH2}</p>''',
            unsafe_allow_html=True)
        st.markdown(f'''
            <p style="text-align: justify; margin:1rem 1.5rem 1rem;color: #e5e8f3; font-size: 1em;font-weight: 400" >{hp.CH2CONTENT}</p>''',
            unsafe_allow_html=True)
        st.markdown(f'''
            <p style="text-align: justify; margin:0;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >{hp.NAMEH3}</p>''',
            unsafe_allow_html=True)
        st.markdown(f'''
            <p style="text-align: justify; margin:1rem 1.5rem 1rem;color: #e5e8f3; font-size: 1em;font-weight: 400" >{hp.CH3CONTENT}</p>''',
            unsafe_allow_html=True)

st.space(size='medium')
#achievements
st.markdown(f'''
<p style="text-align: center; display: block; color: #e5e8f3; font-size: 2.5em; font-weight: 800" >{hp.ACHIEVEMENT}</p>''', unsafe_allow_html=True)
st.space(size='small')


col1, col2, col3 = st.columns(3, border=True, gap="medium")
with col1:
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.space()
        st.image(dost_logo, use_container_width=False)
        st.markdown(f'''
            <p style="text-align: center; margin:0;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >{hp.A1HEADER}</p>''',
                    unsafe_allow_html=True)
        st.markdown(f'''
                    <p style="text-align: center; margin: 0 auto 0;color: #e5e8f3; font-size: 0.8em; font-weight: 400" >{hp.A1SUB}</p>''',
                    unsafe_allow_html=True)
        st.markdown(f'''
                    <p style="text-align: center; margin: 0 auto 0;color: #e5e8f3; font-size: 0.6em;font-style:italic; font-weight: 300" >{hp.A1PERIOD}</p>''',
                    unsafe_allow_html=True)
        st.space(size='small')
with col2:
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.space()
        st.image(codechum_logo, use_container_width=False)
        st.markdown(f'''
            <p style="text-align: center; margin:0;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >{hp.A2HEADER}</p>''',
                    unsafe_allow_html=True)
        st.markdown(f'''
                    <p style="text-align: center; margin: 0 auto 0;color: #e5e8f3; font-size: 0.8em; font-weight: 400" >{hp.A2SUB}</p>''',
                    unsafe_allow_html=True)
        st.markdown(f'''
                    <p style="text-align: center; margin: 0 auto 0;color: #e5e8f3; font-size: 0.6em;font-style:italic; font-weight: 300" >{hp.A2PERIOD}</p>''',
                    unsafe_allow_html=True)
        st.space(size='small')
with col3:
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.space()
        st.image(mythic_logo, use_container_width=False)
        st.markdown(f'''
            <p style="text-align: center; margin:0;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >{hp.A3HEADER}</p>''',
                    unsafe_allow_html=True)
        st.markdown(f'''
                    <p style="text-align: center; margin: 0 auto 0;color: #e5e8f3; font-size: 0.8em; font-weight: 400" >{hp.A3SUB}</p>''',
                    unsafe_allow_html=True)
        st.markdown(f'''
                    <p style="text-align: center; margin: 0 auto 0;color: #e5e8f3; font-size: 0.6em;font-style:italic; font-weight: 300" >{hp.A3PERIOD}</p>''',
                    unsafe_allow_html=True)
        st.space(size='small')

st.space(size='large')
st.markdown(f'''
    <p style="text-align: center;margin-top:0;font-style:italic;display: block; color: #e5e8f3; font-size: 0.8em;opacity:0.7; font-weight: 400" >Don't forget to checkout the navigation tab on the upper left 😉</p>''', unsafe_allow_html=True)