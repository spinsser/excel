import streamlit as st
import pandas as pd

# st.html("""
# <style>
# body, html {
#     direction: RTL;
#     unicode-bidi: bidi-override;
#     text-align: right;
# }
# p, div, input, label, h1, h2, h3, h4, h5, h6 {
#     direction: RTL;
#     unicode-bidi: bidi-override;
#     text-align: right;
# }
# </style>
# """)

stock_df = pd.read_csv('./input.csv', encoding='utf8')
stock_df.drop(columns=['Unnamed: 23', 'Unnamed: 24'], inplace=True, errors='ignore')

markets = stock_df['السوق'].unique()


if __name__ == "__main__":
    st.header('Stock Analyzer v0.04')
    st.divider()
    options = st.multiselect(
    "Choose the market",
    markets,
    markets,)
    dividens = st.toggle("Dividens only")
    st.divider()
    filtered_df = stock_df[stock_df['السوق'].isin(options)]
    if dividens:
        filtered_df = filtered_df[~filtered_df['توزيعات الأرباح'].isin(['0.00%', 'Unavailable', None])]
    st.dataframe(filtered_df,
                hide_index=True,
                column_config={
                    "السعر": None,
                    "رمز الشركة": st.column_config.Column(pinned=True),

                })

    # st.html("""
    # <style>
    # [data-testid=stElementToolbarButton]:first-of-type {
    #     display: none;
    # }
    # </style>
    # """)
    # with st.container(height=300):
    #     st.html(stock_df.to_html())