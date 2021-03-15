def importar_base(nome_arquivo):
    """
    Função de importação das bases csv da pasta "bases" do curso
    de Python. Arquivos depois do dia 05/03/2021 possuem esta
    função. Não criei verificação de erros, pois este arquivo
    é só para não ficar escrevendo o mesmo código em todas
    as aulas.

    @param nome_arquivo: nome do arquivo que está na pasta "base"

    return: retorna o arquivo como um dataframe
    """

    import pandas as pd
    import os
    from pathlib import Path

    p = Path(os.getcwd())
    pasta_bases = str(p.parent.parent) + "\\bases\\"
    return pd.read_csv(pasta_bases + "alugueis\\" + nome_arquivo, index_col=0)


    