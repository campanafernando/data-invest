Este projeto Python utiliza o framework Streamlit para criar um painel interativo que exibe dados do mercado de ações. A fonte de dados é a biblioteca yfinance para recuperar informações de ações em tempo real, enquanto a modelagem de dados é facilitada pelo uso da biblioteca pydantic.

Instale o Poetry e execute o comando poetry install para baixar as dependências

Para iniciar o painel, execute o seguinte comando no terminal:

streamlit run main.py

Isso abrirá automaticamente o painel em seu navegador padrão.

Escolha o ativo de sua preferência e o intervalo de tempo para visualizar os dados históricos das ações.

Os dados são apresentados em gráficos interativos para facilitar possíveis análises. Além dos gráficos, são exibidas informações detalhadas sobre os ativos selecionados.
