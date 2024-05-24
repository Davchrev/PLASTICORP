import streamlit as st
import PIL as image 
import requests
from streamlit_lottie import st_lottie





st.set_page_config(page_title="PLACORP",page_icon="♻️",layout="wide")
email_contact = "david@hotmail.om"

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)
        
css_load("main.css")      


url = 'https://lottie.host/4104c785-5df1-4091-9f36-e55373f86310/e1Qph0iVER.json'

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie=load_lottie(url)     



# INTRO

with st.container(): 
    st.header("vetereia, somos PLACORP 👋")
    st.title("Queremos ver un mundo con menos plastico y mas biodiversidad")
    st.write(
        
            '''
             Demostrar que la gestion de residuos solidos en el Perú ha fracazado rotundamente, desde el manejo de sistema de gestin de la basura, hasta el aprovechamiento de los rellenos sanitarios y la educacion ambietal en la población peruana, la cual es escasa.
             
             ***BUSCAMOS UN MUNDO MAS LIMPIO Y MAS RESPETUOSO*** 
             
             '''
             )
    st.write("[Saber Mas](https://google.com)")
    
# SOBRE NOSOTROS

with st.container():
    import streamlit as st

    st.write("---")
   

    text_column, animation_column = st.columns(2)
    with text_column:
        st.header("Sobre Nosotros🔍🕵️")
        st.write('''
               somos 3 estudiantes egresados de la carrera de ingenieria industrial en al universidad de lima, con el pasar de los años, hemos visto como nuestra ciudad, que con tanto cariño nos ha visto crecer y nos ha cogido, viene siendo destruida y contaminadamente por los grandes empresarios y las grandes empresas. es por esto que quremos brindar nuestros servicios para poder dar nuestro grano de arena en este cambio global que se esta viendo en el mundo y que es importante
               nuestro servicios comprender :
               
               - ***Recogo de Basura y valorización***
               
               - ***Biocombustribles***
               
               - ***Compostaje***
               
               - ***Reciclaje vidrio y plastico***
               
               - ***Venta pallet plastico***
                 
               ***EL CAMBIO QUE QUEREMOS VER EN EL MUNDO, DEBE EMPEZAR EN NUESTRO PROPIO MUNDO*** 
                '''
        )
        st.write("[Quieres saber mas?](https://facebook.com)")
        
    with animation_column:
        st.lottie(lottie, height =400)   
        

# SERVICIOS

with st.container():
    st.write("---")
    st.header("Servicios⚙️")
    st.write("##")
    image_column, text_column, = st.columns((1,2))
    with image_column:
        
        st.image("asd.jpg", use_column_width=True)
    with text_column:
        
        st.subheader("GESTION DE RESIDUOS SOLIDOS")
        
        st.write(
            '''
            Brindar sopote y servicio a la empresasas productoras del Peru, para poder mejorar la eficiencia de los canales de gestion de residuos, mediante la implementación de metodologias de trabajo y una correcta valorización y manipulación de los productos intangibles y quimicos encontrados en el momento del despeje
        
            ''',)
        st.write("[Saber Mas](https://amazon.com)")




with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column, = st.columns((1,2))
    with image_column:
        
        st.image("asd1.jpg", use_column_width=True)
        
        
    with text_column:
        
        st.write("##")
        
        st.subheader("GESTION DE RESIDUOS SOLIDOS")
        
        st.write(
            '''
            Brindar sopote y servicio a la empresasas productoras del Peru, para poder mejorar la eficiencia de los canales de gestion de residuos, mediante la implementación de metodologias de trabajo y una correcta valorización y manipulación de los productos intangibles y quimicos encontrados en el momento del despeje
        
            ''',)
        st.write("[Saber Mas](https://amazon.com)")
        
st.write("---")

with st.container():
      st.write("---")
      st.write("##")
      image_column, text_column, = st.columns((1,2))
with image_column:
        
    st.image("asd2.jpeg", use_column_width=True)

with text_column:
        
        st.write("##")
        
        st.subheader("GESTION DE RESIDUOS SOLIDOS")
        
        st.write(
            '''
            Brindar sopote y servicio a la empresasas productoras del Peru, para poder mejorar la eficiencia de los canales de gestion de residuos, mediante la implementación de metodologias de trabajo y una correcta valorización y manipulación de los productos intangibles y quimicos encontrados en el momento del despeje
        
            ''',)
        st.write("[Saber Mas](https://amazon.com)")
    
    
# FORM CONTACT

with st.container():
    st.write("---")
    st.header("Contacta con nosotros📩 ")  
    st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_contact}" method="POST">
     <input type="hidden" name="_catcha" value="false">
     <input type="message" name="name" placeholder = "tu nombre" required>
     <input type="message" name="email" placeholder = "tu email" required>
     <textarea type="message" name="messenge" placeholder = "tu mensaje aqui" required></textarea>
     <button type="submit">ENVIAR</button>
    </form>
     """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    

      
    
    

    
    
    
    
    



