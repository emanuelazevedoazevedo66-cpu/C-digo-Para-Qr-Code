import streamlit as st

# Configuração da página
st.set_page_config(page_title="Jean Sammet Quiz", page_icon="💻")

st.title("🎓 Jean Sammet Quiz")
st.write("Teste seus conhecimentos sobre uma das maiores pioneiras da computação!")

# Dicionário com as perguntas e respostas
perguntas = [
    {"p": "Qual a data de nascimento de Jean Sammet?", "ops": ["10/03/1998", "23/08/1978", "23/03/1928", "15/09/1996"], "correta": 2},
    {"p": "Em que ano a carreira de Jean Sammet iniciou?", "ops": ["1989", "1991", "1995", "1955"], "correta": 3},
    {"p": "Jean Sammet foi uma das criadoras de qual linguagem?", "ops": ["Cobol", "C++", "Java", "Python"], "correta": 0},
    {"p": "Em qual empresa Jean Sammet trabalhou por 27 anos?", "ops": ["Google", "Microsoft", "IBM", "Apple"], "correta": 2},
    {"p": "Ela foi a primeira mulher a presidir qual organização?", "ops": ["ACM", "IEEE", "NASA", "Intel"], "correta": 0},
    {"p": "Qual era o tema do seu famoso livro de 1969?", "ops": ["Redes", "IA", "Hardware", "Linguagens de Programação"], "correta": 3},
    {"p": "Jean defendeu que as linguagens fossem baseadas em:", "ops": ["Inglês", "Binário", "Símbolos Gregos", "Desenhos"], "correta": 0},
]

# Usando um formulário para processar as respostas de uma vez
with st.form("quiz_form"):
    respostas_usuario = []
    for i, item in enumerate(perguntas):
        res = st.radio(f"**Pergunta {i+1}:** {item['p']}", item['ops'], key=i)
        respostas_usuario.append(item['ops'].index(res))
    
    submit = st.form_submit_button("Enviar Respostas")

if submit:
    pontos = 0
    for i, res in enumerate(respostas_usuario):
        if res == perguntas[i]['correta']:
            pontos += 1
    
    st.divider()
    st.subheader(f"Sua pontuação final: {pontos} de 7")
    
    if pontos == 7:
        st.balloons()
        st.success("Parabéns! Você zerou o quiz!")
    elif pontos >= 5:
        st.info("Você mandou muito bem!")
    else:
        st.warning("Continue tentando! Você consegue!")
