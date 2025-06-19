import streamlit as st
from pathlib import Path
import zipfile
import shutil

from ai_solutions.main import run

st.title("Assistente IA de análise de arquivos CSV")
st.write("Este assistente de IA auxilia você na análise automatizada de arquivos CSV enviados. Envie um arquivo ZIP contendo pelo menos um arquivo CSV para começar.")

# Variável de controle para liberar perguntas
csvs_encontrados = []


with st.sidebar:
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

        # Limpa o diretório antes de extrair
        if data_dir.exists() and data_dir.is_dir():
            shutil.rmtree(data_dir)
        data_dir.mkdir(parents=True, exist_ok=True)
        
        # Para segurança contra path traversal, limpe nomes
        safe_names = []
        for member in z.namelist():
            # Remove possíveis caminhos absolutos ou referências ".."
            normalized = Path(member).name
            if not normalized:
                continue
            safe_names.append((member, normalized))

        # Extrai apenas arquivos CSV
        for orig_name, safe_name in safe_names:
            if safe_name.lower().endswith('.csv'):
                dest_path = data_dir / safe_name
                with z.open(orig_name) as source, open(dest_path, "wb") as target:
                    target.write(source.read())

        # Atualiza a lista de CSVs extraídos
        csvs_encontrados = [p for p in data_dir.iterdir() if p.is_file() and p.suffix.lower() == ".csv"]

        if not csvs_encontrados:
                st.error("O arquivo ZIP não contém nenhum arquivo CSV válido. Por favor, envie um ZIP contendo pelo menos um arquivo .csv.")
        else:
            st.success(f"Arquivos CSV extraídos para: {data_dir}")
            # Opcional: mostrar lista extraída
            st.write([p.name for p in csvs_encontrados])

# Só mostra o campo de pergunta e executa a task se houver CSV
if csvs_encontrados:
    type_task = "Responder Pergunta sobre o CSV:"
    user_answer = st.text_area("Digite sua pergunta sobre o conteúdo do CSV:")
    if st.button("Executar verificação do conteúdo do CSV"):
        if not user_answer.strip():
            st.warning("Por favor, insira uma pergunta sobre o conteúdo do CSV.")
        else:
            st.write("Processando sua solicitação... Aguarde um momento.")
            result = run(user_answer)
            st.subheader("Resposta do Assistente sobre o conteúdo do CSV:")
            st.write(result.raw)
else:
    st.info("Faça upload de um arquivo ZIP contendo pelo menos um CSV para liberar o envio de perguntas.")