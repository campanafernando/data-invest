import streamlit as st
from app.stock_market.stock_market_controller import StockMarketData
from forex_python.converter import CurrencyRates
from app.database.db import create_connection, create_table
from app.database.repository import insert_comment, get_comments

conn = create_connection("datainvest.db")
create_table(conn)

st.markdown(
        """
        <style>
        .big-font {
            font-size:20px !important;
            font-weight: bold;
        }
        .stock-info {
            color: #008080;
        }
        .graph-title {
            color: #000080;
        }
        </style>
        """, unsafe_allow_html=True
    )

st.title('DataInvest')

symbol = st.text_input('Insira a ação desejada:')

if symbol:
    stock_market_data = StockMarketData(
        ticker_symbol=symbol
    )

    currency_converter = CurrencyRates()

    stock_market_general_data = stock_market_data.get_equity_general_data()

    col1, col2 = st.columns([2, 3]) 

    if stock_market_data is not None:
        with col1:
            st.markdown('**Informações gerais:**', unsafe_allow_html=True)
            st.markdown(f"<div class='stock-info'>Ação escolhida: {stock_market_general_data.symbol}</div>", unsafe_allow_html=True)

            open_value_brl = round(currency_converter.convert('USD', 'BRL', stock_market_general_data.open_value), 2)
            higher_value_brl = round(currency_converter.convert('USD', 'BRL', stock_market_general_data.higher_value), 2)
            lower_value_brl = round(currency_converter.convert('USD', 'BRL', stock_market_general_data.lower_value), 2)
            closed_value_brl = round(currency_converter.convert('USD', 'BRL', stock_market_general_data.closed_value), 2)

            st.write(f"Valor de abertura: {stock_market_general_data.open_value} USD / {open_value_brl} BRL")
            st.write(f"Valor mais alto do último intervalo: {stock_market_general_data.higher_value} USD / {higher_value_brl} BRL")
            st.write(f"Valor mais baixo do último intervalo: {stock_market_general_data.lower_value} USD / {lower_value_brl} BRL")
            st.write(f"Valor de fechamento: {stock_market_general_data.closed_value} USD / {closed_value_brl} BRL")
            st.write(f"Volume total de trades realizadas: {stock_market_general_data.volume}")

        with col2:
            st.markdown('<div class="graph-title">Gráfico da Ação</div>', unsafe_allow_html=True)
            st.markdown('<div class="big-font">Selecione o intervalo de tempo para o gráfico:</div>', unsafe_allow_html=True)
            time_frame = st.radio("", ['diário', 'semanal'])

            stock_market_graph = stock_market_data.get_equity_graph(time_frame)
            if stock_market_graph is not None:
                st.pyplot(stock_market_graph, bbox_inches='tight')

        st.markdown('<div class="big-font">Comentários do Analista</div>', unsafe_allow_html=True)
        comment = st.text_area("Adicione seu comentário aqui:")
        if st.button('Salvar Comentário'):
            insert_comment(conn, symbol, comment)
            st.success('Comentário salvo com sucesso!')

        st.markdown('<div class="big-font">Comentários Anteriores</div>', unsafe_allow_html=True)
        comments = get_comments(conn, symbol)
        for comment in comments:
            st.text(f"{comment[3]}: {comment[2]}")  
