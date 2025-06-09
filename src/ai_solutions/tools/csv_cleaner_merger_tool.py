import pandas as pd
import os
from typing import List
from crewai.tools import BaseTool

class CSVCleanerMergerTool(BaseTool):
    name: str = "CSVCleanerMergerTool"
    description: str = (
        "Limpa, normaliza colunas e mescla múltiplos arquivos CSV, retornando o caminho do arquivo mesclado."
    )
    save: str  = "merged_path"

    def _run(self, paths: List[str]) -> str:
        cleaned_dfs: List[pd.DataFrame] = []
        for path in paths:
            df = pd.read_csv(path)

            # 1) Remove linhas completamente vazias
            df = df.dropna(how="all")

            # 2) Padroniza nomes de coluna: strip, lowercase, sem acentos, underline
            df.columns = (
                df.columns
                  .str.strip()
                  .str.lower()
                  .str.normalize('NFKD')
                  .str.encode('ascii', errors='ignore')
                  .str.decode('ascii')
                  .str.replace(' ', '_')
            )

            # 3) Converte tipos numéricos quando possível
            for col in df.select_dtypes(include=["object"]).columns:
                coerced = pd.to_numeric(df[col], errors="ignore")
                if not coerced.equals(df[col]):
                    df[col] = coerced

            cleaned_dfs.append(df)

        if not cleaned_dfs:
            raise ValueError("Nenhum DataFrame foi carregado para mesclagem.")

        # Identifica colunas comuns a todos os DataFrames
        common_cols = set(cleaned_dfs[0].columns)
        for df in cleaned_dfs[1:]:
            common_cols &= set(df.columns)

        if not common_cols:
            raise ValueError(
                "Não há colunas em comum para realizar o merge. "
                f"Colunas do primeiro DF: {list(cleaned_dfs[0].columns)}. "
                "Impossível mesclar."
            )

        # Escolhe a primeira coluna comum como chave de merge
        merge_key = sorted(common_cols)[0]
        print(f"Merging on column: '{merge_key}'")

        # Faz merge sucessivo (inner join) em todos os DataFrames
        merged_df = cleaned_dfs[0]
        for df in cleaned_dfs[1:]:
            merged_df = merged_df.merge(df, on=merge_key, how="inner")

        # Define caminho para o CSV mesclado
        project_root = os.getcwd()
        data_dir = os.path.join(project_root, "data")
        os.makedirs(data_dir, exist_ok=True)

        merged_filename = "merged_cleaned.csv"
        merged_path = os.path.join(data_dir, merged_filename)

        # Salva o arquivo mesclado
        merged_df.to_csv(merged_path, index=False)
        print(f"CSV mesclado salvo em: {merged_path}")
        return merged_path
