import streamlit as st

from ai_solutions.main import run

st.title("Assistente IA de analise de csv fiscais")
st.write("Este IA auxilia você com analise de csv fiscais.")

with st.sidebar:
  st.header("Selecione uma tarefa:")
  type_task = "Responder Pergunta sobre o csv"
  user_answer = st.text_area("Digite sua pergunta sobre o conteúdo do csv:")

if st.button("Executar verificação do conteúdo do csv"):
  if not user_answer.strip():
    st.warning("Por favor, insira uma pergunta sobre o conteúdo do csv.")
  else:
    st.write("Processando sua solicitação... Aguarde um momento.")
    result = run(user_answer)
    st.subheader("Resposta do Assistente sobre o conteúdo do csv:")
    # st.write(result.get("answer", "Nenhuma resposta encontrada."))
    st.write(result)