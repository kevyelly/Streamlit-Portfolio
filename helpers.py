import base64
from pathlib import Path
from streamlit_extras.let_it_rain import rain
#funcs
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def getImage(img_path):
    return "<img style='display:block; margin: auto; margin-top: -4rem; padding: 0;' src='data:image/png;base64,{}' class='img-fluid'>".format(img_to_bytes(img_path))

def emojiRain():
    rain(
        emoji="👾",
        font_size=16,
        falling_speed=12,
        animation_length="infinite",
    )

#texts for about me

TITLE = '👾 Pixels & <span style="color: #9883e8">Purpose</span>👾'
NAME = "Karol Vincent <span style='color: #9883e8'>Bebedor</span>"
NAMESUB = "a short autobiography"
NAMEH1 = "Early <span style='color: #9883e8'>Chapters</span> 🌱"
CH1CONTENT = '''It was year 2005, when I was born in Carcar City, Cebu.
                It was in the same city that I completed my elementary and high school education.
                Throughout those years, I developed an interest in technology — primarily video games.
                I completed my basic education with decent academic performance, eventually paving the way for my current university journey.'''
NAMEH2 = "Present <span style='color: #9883e8'>Focus</span> 🛠️"
CH2CONTENT = '''In the present, I am studying as a government scholar in <u><a href="https://cit.edu" style="color: #9575DE">Cebu Insititute of Technology - University</a></u>
                under the Bachelor of Science in <i><b>Computer Science</b></i> program. Now in my third year, I’ve been steadily building my technical foundation through coursework, hands-on projects, and collaborative learning. 
                With the guidance of my instructors and peers, I’ve gained practical experience in areas such as web development, programming fundamentals, and software design — all of which continue to shape my approach to problem-solving and user-centered development.'''
NAMEH3 = "Looking <span style='color: #9883e8'>Ahead</span> 🔭"
CH3CONTENT = '''As I continue my journey in Computer Science, I’m focused on sharpening both my technical skills
                and design thinking. I aim to work on projects that combine accessibility, clarity, and emotional impact
                 — whether that’s through clean code, thoughtful interfaces, or collaborative problem-solving. In the coming years,
                  I hope to contribute to meaningful work that helps people navigate digital spaces with ease and confidence'''
ACHIEVEMENT = 'Recent <span style="color: #9883e8">Achievements </span>'
A1HEADER = 'DOST SEI <span style="color: #9883e8">SCHOLAR</span>'
A1SUB = "National Level"
A1PERIOD = "2023 - Present"
A2HEADER = 'Codechum <span style="color: #9883e8">Java Cert TOP 10</span>'
A2SUB = "Cebu Institute of Technology - University"
A2PERIOD = "2025"
A3HEADER = 'MLBB <span style="color: #9883e8">Mythical Immortal</span>'
A3SUB = "105 Stars Highest"
A3PERIOD = "2025"

#texts for portfolio
PTITLE = "Learning in <span style='color: #9883e8'>Progress</span> 👨‍💻"
PSUBHEADING = "Development Portfolio"

PC1TITLE = "Tools I’m <span style='color: #9883e8'>Learning With</span> 🌱"
PYTHON = "Python"
STSVG = '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 256 140"><path fill="#FF4B4B" d="M123.888 2.182c1.92-2.91 6.258-2.91 8.25 0l40.753 60.75l43.321 64.519a17.903 17.903 0 0 1-1.764 2.581c-.452.539-.88 1.048-1.414 1.571l-.011-.005l.01.005c-.117.112-.23.2-.37.306l-.15.115c-.49.366-.995.712-1.514 1.038c-.42.263-.767.495-1.269.736c-.5.242-1.302.532-1.784.697c-.483.167-.644.223-1 .302c-.178.035-.356.07-.533.092c-.122.021-.242.042-.363.057c-.021.007-.05.007-.07.014l-.542.064c-.568.057-1.159.086-1.763.086a697.794 697.794 0 0 1-151.26 0c-.058 0-.114 0-.172-.008h-.17l-.079-.007h-.077c-.058-.007-.115-.007-.171-.014h-.057c-.079-.007-.15-.007-.227-.014c-.47-.036-1.016-.154-1.408-.241c-.393-.079-.627-.143-.953-.215c-3.87-.917-7.424-3.25-9.053-7.025c-.043-.1-.079-.199-.122-.299l-.006-.021L.225 26.025c-1.067-2.844 1.85-5.69 4.693-4.338c.072 0 .214 0 .286.071l77.902 41.173Zm127.006 19.577c2.852-1.564 5.91 1.137 4.914 4.124v.143l-39.595 101.426l-43.321-64.52l77.931-41.173Z"/><path fill="#7D353B" d="M250.894 21.759h-.07l-77.932 41.173l43.321 64.52l39.595-101.426v-.143c.996-2.987-2.062-5.688-4.914-4.124"/><path fill="#BD4043" d="M132.138 2.182c-1.992-2.91-6.33-2.91-8.25 0l-40.782 60.75l44.878 23.723l85.05 44.948c.534-.523.962-1.032 1.414-1.57a17.903 17.903 0 0 0 1.764-2.582l-43.32-64.519l-40.754-60.75Z"/></svg>'
PC2TITLE = "My <span style='color: #9883e8'>Projects </span>🧩 "
NBDESC = "A math-learning app for kids🧮"
TECH_STACK = "TECH <span style='color: #9883e8'>STACK</span>"
NBEDESC = "A math-learning app for kids designed for Android built using Kotlin for both front-end and back-end. It has basic features such as <span style='color: #9883e8'>User Accounts </span> and <span style='color: #9883e8'>Data Persistence.</span>"
NBGITHUB_BUTTON = '''
<div style="background-color: #24292e; display:block; margin:auto;width:fit-content; padding:5px; border: 1px solid #9883e8;border-radius:10px;">
    <a href="https://github.com/kevyelly/Numbuddy" style="font-size:1rem;color:#e5e8f3;text-decoration:none;"> 
        <img src="https://www.svgrepo.com/show/303615/github-icon-1-logo.svg" style="width:20px"> Github <span style='color: #9883e8'>Repo</span></a></div>
'''
LMDESC ="A LOL-inspired mock website💻"
LMEDESC = "A mock website for League of Legends Merch. This was created to practice the <span style='color: #9883e8'>basic principles</span> of HTML, CSS, AND Vanilla JS. This was an assignment for Web Dev Course. "
LMGITHUB_BUTTON = '''
<div style="display:flex; justify-content:space-between;">
    <div style="background-color: #24292e; display:inline; margin:auto;width:fit-content; padding:5px; border: 1px solid #9883e8;border-radius:10px;">
        <a href="https://github.com/kevyelly/LeagueMerch" style="font-size:1rem;color:#e5e8f3;text-decoration:none;"> 
            <img src="https://www.svgrepo.com/show/303615/github-icon-1-logo.svg" style="width:20px"> Github <span style='color: #9883e8'>Repo</span></a></div>
    <div style="background-color: #24292e; display:inline; margin:auto;width:fit-content; padding:5px; border: 1px solid #9883e8;border-radius:10px;">
        <a href="/" style="font-size:1rem;color:#e5e8f3;text-decoration:none;"> 
            💻 Github Pages</span></a></div>
</div>
'''

EXDESC = "A team training management software 👥"
EXEDESC = "Exceed is a software aimed at managing trainings in corporate settings. It enables administrators to efficiently organize, monitor, and evaluate employee learning programs.  "
EXEGITHUB_BUTTON = '''
<div style="background-color: #24292e; display:block; margin:auto;width:fit-content; padding:5px; border: 1px solid #9883e8;border-radius:10px;">
    <a href="https://github.com/kevyelly/Exceed" style="font-size:1rem;color:#e5e8f3;text-decoration:none;"> 
        <img src="https://www.svgrepo.com/show/303615/github-icon-1-logo.svg" style="width:20px"> Github <span style='color: #9883e8'>Repo</span></a></div>
'''

EODESC = "A skill-sharing software 🛠️"
EOEDESC = "ExcelOne is a software enables for learners and teachers to collaborate. Inspired by Fiverr, this allows teachers to provide tutoring service to students on their subect of expertise."
EOGITHUB_BUTTON = '''
<div style="background-color: #24292e; display:block; margin:auto;width:fit-content; padding:5px; border: 1px solid #9883e8;border-radius:10px;">
    <a href="https://github.com/IgnisFrostburn/OOP-Capstone" style="font-size:1rem;color:#e5e8f3;text-decoration:none;"> 
        <img src="https://www.svgrepo.com/show/303615/github-icon-1-logo.svg" style="width:20px"> Github <span style='color: #9883e8'>Repo</span></a></div>
'''

WRDESC = "A visual novel game 🎮"
WREDESC = "What Remains is a visual novel game made from scratch using Java. Created for Course Completion of Java Course."
WRGITHUB_BUTTON = '''
<div style="background-color: #24292e; display:block; margin:auto;width:fit-content; padding:5px; border: 1px solid #9883e8;border-radius:10px;">
    <a href="https://github.com/BenJosephEscolano/CSIT228Capstone" style="font-size:1rem;color:#e5e8f3;text-decoration:none;"> 
        <img src="https://www.svgrepo.com/show/303615/github-icon-1-logo.svg" style="width:20px"> Github <span style='color: #9883e8'>Repo</span></a></div>
'''


GITHUB_CLICKABLE = '''
<a href="https://github.com/kevyelly" style="display: block; width:100%; height:100%;text-align:center"><img src="https://www.svgrepo.com/show/303615/github-icon-1-logo.svg" style="height:70px;width:70px"></a><div>
'''

LINKEDIN_CLICKABLE = '''
<a href="https://www.linkedin.com/in/karol-vincent-bebedor-3a4257357/" style="display: block; width:100%; height:100%;text-align:center"><img src="https://www.svgrepo.com/show/157006/linkedin.svg" style="height:70px;width:70px"></a><div>
'''
TEAMS_CLICKABLE = '''
<a href="https://teams.microsoft.com/l/chat/0/0?users=karolvincent.bebedor@cit.edu" style="display: block; width:100%; height:100%;text-align:center"><img src="https://www.svgrepo.com/show/448240/microsoft-teams.svg" style="height:70px;width:70px"></a><div>
'''
GMAIL_CLICKABLE = '''
<a href="mailto:bebedorkarolvincent@gmail.com" style="display: block; width:100%; height:100%;text-align:center"><img src="https://www.svgrepo.com/show/452213/gmail.svg" style="height:70px;width:70px"></a><div>
'''



NUMBUDDY_ITEMS = [
    dict(
        title="Numbuddy",
        text="Login Screen",
        img='https://i.imgur.com/MAIdy5x.png',
        link="https://github.com/kevyelly/Numbuddy",
    ),
    dict(
        title="Numbuddy",
        text="Home Screen",
        img="https://i.imgur.com/4G5zCTX.png",
        link="https://github.com/kevyelly/Numbuddy",
    ),
    dict(
        title="Numbuddy",
        text="Quiz Screen",
        img="https://i.imgur.com/hPLBlCX.png",
        link="https://github.com/kevyelly/Numbuddy",
    ),
    dict(
        title="Numbuddy",
        text="Settings",
        img="https://i.imgur.com/QkDKaSj.png",
        link="https://github.com/kevyelly/Numbuddy",
    )
]
LM_ITEMS = [
    dict(
        title="",
        text="",
        img='https://i.imgur.com/0v2IXVv.png',
        link="https://github.com/kevyelly/LeagueMerch",
    ),
    dict(
        title="",
        text="",
        img="https://i.imgur.com/wQw9FiA.png",
        link="https://github.com/kevyelly/LeagueMerch",
    )
]
EXCEED_ITEMS = [
    dict(
        title="",
        text="",
        img='https://i.imgur.com/sRANlmq.png',
        link="https://github.com/kevyelly/Exceed",
    ),
    dict(
        title="",
        text="",
        img="https://i.imgur.com/HV7OrNE.png",
        link="https://github.com/kevyelly/Exceed",
    ),
    dict(
        title="",
        text="",
        img="https://i.imgur.com/gi4YcnL.png",
        link="https://github.com/kevyelly/Exceed",
    )
]
EO_ITEMS = [
    dict(
        title="",
        text="",
        img="http://i.imgur.com/hD6wp6L.png",
        link="https://github.com/IgnisFrostburn/OOP-Capstone.git",
    ),
    dict(
        title="",
        text="",
        img="https://i.imgur.com/Y3gsJQV.png",
        link="https://github.com/IgnisFrostburn/OOP-Capstone.git",
    )
]



