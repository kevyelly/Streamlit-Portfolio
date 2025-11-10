from pathlib import Path
import helpers as hp
import streamlit as st
from streamlit_carousel import carousel
curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
styles_css = curr_dir / "styles" / "styles.css"
whole_pic = curr_dir / "media" / "whole.png"

with open(styles_css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


st.markdown(f'''
    <p style="text-align: center; margin-top: -4rem;margin-bottom:0;display: block; color: #e5e8f3; font-size: 2.75em; font-weight: 800" >{hp.PTITLE}</p>''', unsafe_allow_html=True)
st.markdown(f'''
    <p style="text-align: center;margin-top:0;font-style:italic;display: block; color: #e5e8f3; font-size: 1.5em; font-weight: 400" >{hp.PSUBHEADING}</p>''', unsafe_allow_html=True)
st.space(size="small")
st.markdown(f'''
    <p style="text-align: justify; margin:0;color: #e5e8f3; font-size: 1.5em;font-weight: 600" >{hp.PC1TITLE}</p>''',
            unsafe_allow_html=True)
st.space()
col1, col2, col3, col4 = st.columns(4, border=True)
with col1:
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg", width=100)
        st.markdown(f'''
            <p style="text-align: center; margin-top:1.2rem; margin-bottom:1.2rem;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >Java</p>''',
                    unsafe_allow_html=True)
with col2:
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg", width=100)
        st.markdown(f'''
            <p style="text-align: center;margin-top:1.2rem; margin-bottom:1.2rem; color: #9883e8; font-size: 1.2em;font-weight: 600" >C++</p>''',
                    unsafe_allow_html=True)
with col3:
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg", width=100)
        st.markdown(f'''
            <p style="text-align: center;margin-top:1.2rem; margin-bottom:1.2rem; color: #e5e8f3; font-size: 1.2em;font-weight: 600" >SQL</p>''',
                    unsafe_allow_html=True)
with col4:
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg", width=100)
        st.markdown(f'''
            <p style="text-align: center;margin-top:1.2rem; margin-bottom:1.2rem;color: #9883e8; font-size: 1.2em;font-weight: 600" >Python</p>''',
                    unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4, border=True)
with col1:
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg", width=100)
        st.markdown(f'''
            <p style="text-align: center;margin-top:1.2rem; margin-bottom:1.2rem; color: #9883e8; font-size: 1.2em;font-weight: 600" >HTML5</p>''',
                    unsafe_allow_html=True)
with col2:
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg", width=100)
        st.markdown(f'''
            <p style="text-align: center;margin-top:1.2rem; margin-bottom:1.2rem; color: #e5e8f3; font-size: 1.2em;font-weight: 600" >CSS3</p>''',
                    unsafe_allow_html=True)
with col3:
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.image(hp.STSVG, width=100)
        st.markdown(f'''
            <p style="text-align: center;color: #9883e8;margin-top:1.2rem; margin-bottom:1.2rem; font-size: 1.2em;font-weight: 600" >Streamlit</p>''',
                    unsafe_allow_html=True)
with col4:
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.image("https://www.vectorlogo.zone/logos/kotlinlang/kotlinlang-icon.svg", width=100)
        st.markdown(f'''
            <p style="text-align: center;margin-top:1.2rem; margin-bottom:1.2rem;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >Kotlin</p>''',
                    unsafe_allow_html=True)


st.space(size="medium")
st.markdown(f'''
    <p style="text-align: justify; margin:0;color: #e5e8f3; font-size: 1.5em;font-weight: 600" >{hp.PC2TITLE}</p>''',
            unsafe_allow_html=True)
st.space()
col1, col2 = st.columns(2, border=True)
with col1:
    st.markdown(f'''
        <p style="text-align: center; color: #9883e8;margin:0; font-size: 2em;font-weight: 800" >Numbuddy</p>''',
                unsafe_allow_html=True)
    st.markdown(f'''
        <p style="text-align: center;margin-top:0;margin-bottom:0;font-style:italic;display: block; color: #e5e8f3; font-size: 1em; font-weight: 400" >{hp.NBDESC}</p>''',
                unsafe_allow_html=True)
    st.markdown(f'''
        <p style="text-align: justify; margin:1rem 1.5rem 1rem;color: #e5e8f3; font-size: 1em;font-weight: 400" >{hp.NBEDESC}</p>''',
                unsafe_allow_html=True)
    st.markdown(hp.NBGITHUB_BUTTON, unsafe_allow_html=True)
    st.space(size="small")
    cont=st.container(horizontal_alignment="center", border=True)
    with cont:
        carousel(items=hp.NUMBUDDY_ITEMS)
    st.markdown(f'''
        <p style="text-align: center; color: #e5e8f3; margin-bottom:10px;font-size: 1.2em; font-weight: 700" >{hp.TECH_STACK}</p>''',
                unsafe_allow_html=True)
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.image("https://www.vectorlogo.zone/logos/kotlinlang/kotlinlang-icon.svg", width=60)
        st.markdown(f'''
                    <p style="text-align: center;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >Kotlin</p>''',
                    unsafe_allow_html=True)
with col2:
    st.markdown(f'''
        <p style="text-align: center; color: #9883e8;margin:0; font-size: 2em;font-weight: 800" >League Merch Site</p>''',
                unsafe_allow_html=True)
    st.markdown(f'''
        <p style="text-align: center;margin-top:0;margin-bottom:0;font-style:italic;display: block; color: #e5e8f3; font-size: 1em; font-weight: 400" >{hp.LMDESC}</p>''',
                unsafe_allow_html=True)
    st.markdown(f'''
        <p style="text-align: justify; margin:1rem 1.5rem 1rem;color: #e5e8f3; font-size: 1em;font-weight: 400" >{hp.LMEDESC}</p>''',
                unsafe_allow_html=True)
    st.markdown(hp.LMGITHUB_BUTTON, unsafe_allow_html=True)
    st.space(size="small")
    cont=st.container(horizontal_alignment="center", border=True)
    with cont:
        carousel(items=hp.LM_ITEMS)
    st.markdown(f'''
        <p style="text-align: center; color: #e5e8f3; margin-bottom:10px;font-size: 1.2em; font-weight: 700" >{hp.TECH_STACK}</p>''',
                unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        cont = st.container(horizontal_alignment="center")
        with cont:
            st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg", width=60)
            st.markdown(f'''
                        <p style="text-align: center;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >HTML5</p>''',
                        unsafe_allow_html=True)
    with col2:
        cont = st.container(horizontal_alignment="center")
        with cont:
            st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg", width=60)
            st.markdown(f'''
                        <p style="text-align: center;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >CSS3</p>''',
                        unsafe_allow_html=True)
    with col3:
        cont = st.container(horizontal_alignment="center")
        with cont:
            st.image("	https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg", width=60)
            st.markdown(f'''
                        <p style="text-align: center;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >Javascript</p>''',
                        unsafe_allow_html=True)

col1, col2 = st.columns(2, border=True)
with col1:
    st.markdown(f'''
        <p style="text-align: center; color: #9883e8;margin:0; font-size: 2em;font-weight: 800" >Exceed</p>''',
                unsafe_allow_html=True)
    st.markdown(f'''
        <p style="text-align: center;margin-top:0;margin-bottom:0;font-style:italic;display: block; color: #e5e8f3; font-size: 1em; font-weight: 400" >{hp.EXDESC}</p>''',
                unsafe_allow_html=True)
    st.markdown(f'''
        <p style="text-align: justify; margin:1rem 1.5rem 1rem;color: #e5e8f3; font-size: 1em;font-weight: 400" >{hp.EXEDESC}</p>''',
                unsafe_allow_html=True)
    st.markdown(hp.EXEGITHUB_BUTTON, unsafe_allow_html=True)
    st.space(size="small")
    cont=st.container(horizontal_alignment="center", border=True)
    with cont:
        carousel(items=hp.EXCEED_ITEMS)
    st.markdown(f'''
        <p style="text-align: center; color: #e5e8f3; margin-bottom:10px;font-size: 1.2em; font-weight: 700" >{hp.TECH_STACK}</p>''',
                unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        cont = st.container(horizontal_alignment="center")
        with cont:
            st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg", width=60)
            st.markdown(f'''
                        <p style="text-align: center;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >HTML5</p>''',
                        unsafe_allow_html=True)
    with c2:
        cont = st.container(horizontal_alignment="center")
        with cont:
            st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg", width=60)
            st.markdown(f'''
                        <p style="text-align: center;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >CSS3</p>''',
                        unsafe_allow_html=True)
    with c3:
        cont = st.container(horizontal_alignment="center")
        with cont:
            st.image("https://www.svgrepo.com/show/354180/php.svg", width=60)
            st.markdown(f'''
                        <p style="text-align: center;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >PHP</p>''',
                        unsafe_allow_html=True)
with col2:
    st.markdown(f'''
        <p style="text-align: center; color: #9883e8;margin:0; font-size: 2em;font-weight: 800" >ExcelOne</p>''',
                unsafe_allow_html=True)
    st.markdown(f'''
        <p style="text-align: center;margin-top:0;margin-bottom:0;font-style:italic;display: block; color: #e5e8f3; font-size: 1em; font-weight: 400" >{hp.EODESC}</p>''',
                unsafe_allow_html=True)
    st.markdown(f'''
        <p style="text-align: justify; margin:1rem 1.5rem 1rem;color: #e5e8f3; font-size: 1em;font-weight: 400" >{hp.EOEDESC}</p>''',
                unsafe_allow_html=True)
    st.markdown(hp.EOGITHUB_BUTTON, unsafe_allow_html=True)
    st.space(size="small")
    cont=st.container(horizontal_alignment="center", border=True)
    with cont:
        carousel(items=hp.EO_ITEMS)
    st.markdown(f'''
        <p style="text-align: center; color: #e5e8f3; margin-bottom:10px;font-size: 1.2em; font-weight: 700" >{hp.TECH_STACK}</p>''',
                unsafe_allow_html=True)
    cont = st.container(horizontal_alignment="center")
    with cont:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg", width=60)
        st.markdown(f'''
                    <p style="text-align: center;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >Java</p>''',
                     unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.25, 0.5, 0.25])
with col2:
    bigcont = st.container(horizontal_alignment="center", border=True)
    with bigcont:
        st.markdown(f'''
            <p style="text-align: center; color: #9883e8;margin:0; font-size: 2em;font-weight: 800" >What Remains</p>''',
                    unsafe_allow_html=True)
        st.markdown(f'''
            <p style="text-align: center;margin-top:0;margin-bottom:0;font-style:italic;display: block; color: #e5e8f3; font-size: 1em; font-weight: 400" >{hp.WRDESC}</p>''',
                    unsafe_allow_html=True)
        st.markdown(f'''
        <p style="text-align: justify; margin:1rem 1.5rem 1rem;color: #e5e8f3; font-size: 1em;font-weight: 400" >{hp.WREDESC}</p>''',
                    unsafe_allow_html=True)
        st.markdown(hp.WRGITHUB_BUTTON, unsafe_allow_html=True)
        st.space(size="small")
        cont=st.container(horizontal_alignment="center", border=True)
        with cont:
            st.image("https://i.imgur.com/57jmo9w.png", use_container_width=True)
        st.markdown(f'''
            <p style="text-align: center; color: #e5e8f3; margin-bottom:10px;font-size: 1.2em; font-weight: 700" >{hp.TECH_STACK}</p>''',
                    unsafe_allow_html=True)
        cont = st.container(horizontal_alignment="center")
        with cont:
            st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg", width=60)
            st.markdown(f'''
                        <p style="text-align: center;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >Java</p>''',
                         unsafe_allow_html=True)


st.space(size="medium")
st.markdown(f'''
    <p style="text-align: center; margin:0;color: #e5e8f3; font-size: 2em;font-weight: 600" >Connect <span style='color: #9883e8'>With Me</span> 🤝</p>''',
            unsafe_allow_html=True)
st.markdown(f'''
        <p style="text-align: center;margin-top:0;margin-bottom:0;font-style:italic;display: block; color: #e5e8f3; font-size: 0.8em; font-weight: 400" >Just click the icons😉</p>''',
                unsafe_allow_html=True)
st.space()
c1, c2, c3 = st.columns([0.15, 0.70, 0.15])
with c2:
    c = st.container(border=True)
    with c:
        cl1, cl2, cl3, cl4= st.columns(4, border=True)
        with cl1:
            c = st.container(horizontal_alignment="center", vertical_alignment="center", width="stretch", height="stretch")
            with c:
                st.markdown(hp.GITHUB_CLICKABLE, unsafe_allow_html=True)
                st.markdown(f'''
                    <p style="text-align: center; margin:0;color: #e5e8f3; font-size: 1.2em;font-weight: 600" >SixtoAvenue</p>''',
                            unsafe_allow_html=True)
                st.markdown(f'''
                        <p style="text-align: center;margin-top:0;margin-bottom:0.5rem;font-style:italic;display: block; color: #e5e8f3; font-size: 0.7em; font-weight: 400" >Github</p>''',
                            unsafe_allow_html=True)
        with cl2:
            c = st.container(horizontal_alignment="center", vertical_alignment="center", width="stretch", height="stretch")
            with c:
                st.markdown(hp.LINKEDIN_CLICKABLE, unsafe_allow_html=True)
                st.markdown(f'''
                    <p style="text-align: center; margin:0;color: #e5e8f3; font-size: 0.8em;font-weight: 600" >Karol Vincent Bebedor</p>''',
                            unsafe_allow_html=True)
                st.markdown(f'''
                        <p style="text-align: center;margin-top:0;margin-bottom:0.5rem;font-style:italic;display: block; color: #e5e8f3; font-size: 0.7em; font-weight: 400" >LinkedIn</p>''',
                            unsafe_allow_html=True)
        with cl3:
            c = st.container(horizontal_alignment="center", vertical_alignment="center", width="stretch",
                             height="stretch")
            with c:
                st.markdown(hp.TEAMS_CLICKABLE, unsafe_allow_html=True)
                st.markdown(f'''
                        <p style="text-align: center; margin:0;color: #e5e8f3; font-size: 0.8em;font-weight: 600" >Karol Vincent Bebedor</p>''',
                            unsafe_allow_html=True)
                st.markdown(f'''
                            <p style="text-align: center;margin-top:0;margin-bottom:0.5rem;font-style:italic;display: block; color: #e5e8f3; font-size: 0.7em; font-weight: 400" >MS Teams</p>''',
                            unsafe_allow_html=True)
        with cl4:
            c = st.container(horizontal_alignment="center", vertical_alignment="center", width="stretch",
                             height="stretch")
            with c:
                st.markdown(hp.GMAIL_CLICKABLE, unsafe_allow_html=True)
                st.markdown(f'''
                        <p style="text-align: center; margin:0;color: #e5e8f3; font-size: 0.6em;font-weight: 600" >bebedorkarolvincent@gmail.com</p>''',
                            unsafe_allow_html=True)
                st.markdown(f'''
                            <p style="text-align: center;margin-top:0;margin-bottom:0.5rem;font-style:italic;display: block; color: #e5e8f3; font-size: 0.7em; font-weight: 400" >Gmail</p>''',
                            unsafe_allow_html=True)

st.space(size="large")
st.markdown(f'''
    <p style="text-align: center;margin-top:0;font-style:italic;display: block; color: #e5e8f3; font-size: 0.8em;opacity:0.7; font-weight: 400" >Don't forget to checkout the navigation tab on the upper left 😉</p>''', unsafe_allow_html=True)
