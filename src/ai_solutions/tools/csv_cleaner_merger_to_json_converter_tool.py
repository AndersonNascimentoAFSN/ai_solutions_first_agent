import os
from typing import List
import pandas as pd
from crewai.tools import BaseTool

class CSVCleanerMergerToJSONConverterTool(BaseTool):
    """
    Tool para limpeza, normalização e mesclagem de arquivos CSV, salvando o resultado como um JSON.

    Esta ferramenta:
    - Remove linhas completamente vazias de cada CSV.
    - Padroniza nomes de colunas (lowercase, sem acentos, underscores).
    - Converte colunas de texto para tipos numéricos quando possível.
    - Mescla arquivos com base nas colunas em comum (inner join).
    - Salva o resultado em um arquivo JSON.

    Exemplo de uso:
        tool = CSVCleanerMergerToJSONConverterTool()
        tool._run(['arquivo1.csv', 'arquivo2.csv'])
    """
    name: str = "CSVCleanerMergerToJSONConverterTool"
    description: str = (
        "Limpa, normaliza colunas e mescla múltiplos arquivos CSV, salvando o resultado como um JSON."
    )
    save: str = "json_path"

    def _run(self, paths: List[str]) -> str:
        """
        Limpa, normaliza, mescla múltiplos arquivos CSV e salva o resultado em um arquivo JSON.

        Args:
            paths (List[str]): Lista de caminhos dos arquivos CSV a serem processados.

        Returns:
            str: Caminho do arquivo JSON salvo com os dados mesclados e limpos.

        Raises:
            ValueError: Se não for possível ler um dos arquivos CSV,
                        se não houver DataFrames válidos,
                        ou se não houver colunas em comum para merge.
            Exception: Se houver falha ao salvar o JSON.
        """
        cleaned_dfs: List[pd.DataFrame] = []

        for path in paths:
            try:
                df = pd.read_csv(path, encoding='utf-8', sep=None, engine='python')
            except Exception as e:
                raise ValueError(f"Erro ao ler o arquivo CSV '{path}': {e}")

            # Remove linhas completamente vazias
            df.dropna(how="all", inplace=True)

            # Padroniza nomes de colunas: strip, lowercase, sem acentos, underline
            df.columns = (
                df.columns
                  .str.strip()
                  .str.lower()
                  .str.normalize('NFKD')
                  .str.encode('ascii', errors='ignore')
                  .str.decode('ascii')
                  .str.replace(' ', '_')
            )

            # Converte colunas object para tipos numéricos quando possível
            for col in df.select_dtypes(include=["object"]).columns:
                new_col = pd.to_numeric(df[col], errors="ignore")
                if not new_col.equals(df[col]):
                    df[col] = new_col

            cleaned_dfs.append(df)

        if not cleaned_dfs:
            raise ValueError("Nenhum DataFrame válido foi carregado.")

        # Identifica colunas comuns
        common_cols = set(cleaned_dfs[0].columns)
        for df in cleaned_dfs[1:]:
            common_cols.intersection_update(df.columns)

        if not common_cols:
            raise ValueError(
                "Não há colunas em comum para realizar o merge. "
                f"Colunas do primeiro DataFrame: {list(cleaned_dfs[0].columns)}."
            )

        # Usa a primeira coluna comum ordenada como chave de merge
        merge_key = sorted(common_cols)[0]
        # self.log(f"Realizando merge usando a coluna: '{merge_key}'")

        # Merge sucessivo (inner join)
        merged_df = cleaned_dfs[0]
        for df in cleaned_dfs[1:]:
            merged_df = pd.merge(merged_df, df, on=merge_key, how="inner")

        # Define caminho para salvar o JSON
        data_dir = os.path.join(os.getcwd(), "data")
        os.makedirs(data_dir, exist_ok=True)
        json_path = os.path.join(data_dir, "merged_cleaned.json")

        try:
            merged_df.to_json(json_path, orient='records', force_ascii=False, indent=2)
        except Exception as e:
            raise Exception(f"Erro ao salvar o JSON: {e}")

        # self.log(f"JSON salvo em: {json_path}")
        return json_path
