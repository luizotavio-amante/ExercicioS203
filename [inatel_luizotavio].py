
!pip install streamlit

 %%writefile app.py
 import streamlit as st
 
 # Definindo o estilo da página
 st.set_page_config(page_title="Cantina da Neide", page_icon="🍽️")
 st.markdown(
     """
     <style>
     .main {
         background-color: #f0f8ff; /* Branco */
         color: #003366; /* Azul */
     }
     </style>
     """,
     unsafe_allow_html=True
 )
 
 # Título da aplicação
 st.title("Cantina da Neide")
 
 # Formulário de login
 with st.form(key='login_form'):
     username = st.text_input("Usuário")
     password = st.text_input("Senha", type='password')
 
     # Botão de login
     submit_button = st.form_submit_button(label='Entrar')

 # Lógica de autenticação simples
 if submit_button:
     if username == "inatel" and password == "luizotavio":
         st.success("Bem-vindo à Cantina da Neide!")
     else:
        st.error("Usuário ou senha incorretos.")


!streamlit run app.py & npx localtunnel --port 8501