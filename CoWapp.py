import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
# Define o título da página, o ícone e o layout para ocupar a largura inteira.
st.set_page_config(
    page_title="Análise de Dados Círculo de Willis",
    page_icon="🔘",
    layout="wide",
)

# --- Carregamento dos dados Paciente 1 - Condições Normais---
df_ramos = pd.read_excel('C:\\Users\\Gabriel\\OneDrive - Unesp\\TCC\\resultados_Ramos.xlsx')
df_nos = pd.read_excel('C:\\Users\\Gabriel\\OneDrive - Unesp\\TCC\\resultados_Nos.xlsx')

# --- Carregamento dos dados Paciente 2 - Oclusão de 70% PCoA---
df_ramos2 = pd.read_excel('C:\\Users\\Gabriel\\OneDrive - Unesp\\TCC\\resultados_Ramos2.xlsx')
df_nos2 = pd.read_excel('C:\\Users\\Gabriel\\OneDrive - Unesp\\TCC\\resultados_Nos2.xlsx')

PCA = df_ramos['Vazões (L/s)'].iloc[[1, 8, 16, 17, 18, 19, 20, 21]].sum()
PCoA = df_ramos['Vazões (L/s)'].iloc[[2, 9]].sum()
ICA = df_ramos['Vazões (L/s)'].iloc[[3, 22, 23, 25, 26, 10]].sum()
MCA = df_ramos['Vazões (L/s)'].iloc[[35, 36, 37, 41, 40, 38, 39, 28, 29, 30, 32, 31, 33, 34]].sum()
ACA = df_ramos['Vazões (L/s)'].iloc[[4, 11, 5, 6, 7, 12, 13, 14]].sum()
ACoA = df_ramos['Vazões (L/s)'].iloc[[15]].sum()
OA = df_ramos['Vazões (L/s)'].iloc[[24, 27]].sum()
BA = df_ramos['Vazões (L/s)'].iloc[[0]].sum()

PCA2 = df_ramos2['Vazões (L/s)'].iloc[[1, 8, 16, 17, 18, 19, 20, 21]].sum()
PCoA2 = df_ramos2['Vazões (L/s)'].iloc[[2, 9]].sum()
ICA2 = df_ramos2['Vazões (L/s)'].iloc[[3, 22, 23, 25, 26, 10]].sum()
MCA2 = df_ramos2['Vazões (L/s)'].iloc[[35, 36, 37, 41, 40, 38, 39, 28, 29, 30, 32, 31, 33, 34]].sum()
ACA2 = df_ramos2['Vazões (L/s)'].iloc[[4, 11, 5, 6, 7, 12, 13, 14]].sum()
ACoA2 = df_ramos2['Vazões (L/s)'].iloc[[15]].sum()
OA2 = df_ramos2['Vazões (L/s)'].iloc[[24, 27]].sum()
BA2 = df_ramos2['Vazões (L/s)'].iloc[[0]].sum()

df_vasos = pd.DataFrame({ 'Artérias': ['ACoA', 'OA', 'PCA', 'PCoA', 'ICA', 'MCA', 'ACA', 'BA'], 
                          'Vazões (L/s)': [ACoA, OA, PCA, PCoA, ICA, MCA, ACA, BA] })

df_vasos2 = pd.DataFrame({ 'Artérias': ['ACoA', 'OA', 'PCA', 'PCoA', 'ICA', 'MCA', 'ACA', 'BA'], 
                          'Vazões (L/s)': [ACoA2, OA2, PCA2, PCoA2, ICA2, MCA2, ACA2, BA2] })
# --- Conteúdo Principal ---
st.title("🎲 Dados de Círculo de Willis")
#st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

# --- Métricas Principais (KPIs) ---
#st.subheader("Métricas gerais (Salário anual em USD)")

st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("Vazão nas Artérias - Paciente 1")
    fig1 = px.bar(df_vasos, x='Artérias', y='Vazões (L/s)', title='Vazão nas Artérias')
    st.plotly_chart(fig1, use_container_width=True)


with col_graf2:
    st.subheader("Vazão nas Artérias - Paciente 2")
    fig2 = px.bar(df_vasos2, x='Artérias', y='Vazões (L/s)', title='Vazão nas Artérias - Paciente 2')
    st.plotly_chart(fig2, use_container_width=True)

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    st.subheader("Pressão nas Artérias - Paciente 1")
    fig1 = px.bar(df_nos, x='Nó', y='Pressão nos Nós (Pa)', title='Pressão nas Artérias - Paciente 1')
    st.plotly_chart(fig1, use_container_width=True)


with col_graf4:
    st.subheader("Pressão nas Artérias - Paciente 2")
    fig2 = px.bar(df_nos2, x='Nó', y='Pressão nos Nós (Pa)', title='Pressão nas Artérias - Paciente 2')
    st.plotly_chart(fig2, use_container_width=True)

# --- Tabela de Dados Detalhados - Vazões ---
st.subheader("Dados Detalhados - Paciente 1")
st.dataframe(df_vasos)
st.subheader("Dados Detalhados - Paciente 2")
st.dataframe(df_vasos2)

# --- Tabela de Dados Detalhados - Pressões ---
st.subheader("Dados Detalhados - Paciente 1")
st.dataframe(df_nos)
st.subheader("Dados Detalhados - Paciente 2")
st.dataframe(df_nos2)