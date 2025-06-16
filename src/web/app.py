import streamlit as st
from pathlib import Path
import zipfile

from ai_solutions.main import run

st.title("Assistente IA de analise de csv fiscais")
st.write("Este IA auxilia você com analise de csv fiscais.")

with st.sidebar:
  # st.header("Selecione uma tarefa:")

  uploaded_zip = st.file_uploader(
      label="Selecione um arquivo ZIP",
      type=["zip"]
  )

  if uploaded_zip is not None:
    try:
        z = zipfile.ZipFile(uploaded_zip)
    except zipfile.BadZipFile:
        st.error("O arquivo enviado não é um ZIP válido.")
    else:
        # Defina pasta de destino; ajuste conforme necessidade
        project_root = Path(__file__).parent.parent.parent
        data_dir = project_root / "data" / "uploads"
        data_dir.mkdir(parents=True, exist_ok=True)
        
        # Para segurança contra path traversal, limpe nomes
        safe_names = []
        for member in z.namelist():
            # Remove possíveis caminhos absolutos ou referências ".."
            normalized = Path(member).name
            if not normalized:
                continue
            safe_names.append((member, normalized))
        
        for orig_name, safe_name in safe_names:
            dest_path = data_dir / safe_name
            # Extrai cada arquivo com nome seguro
            with z.open(orig_name) as source, open(dest_path, "wb") as target:
                target.write(source.read())
        
        st.success(f"Arquivos extraídos para: {data_dir}")
        # Opcional: mostrar lista extraída
        st.write([p.name for p in data_dir.iterdir() if p.is_file()])

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
    st.write(result.raw)
