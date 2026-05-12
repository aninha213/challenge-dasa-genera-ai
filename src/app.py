import streamlit as st
import json

st.set_page_config(page_title="Genera AI")

st.title("🧬 Genera AI")
st.subheader("Interpretação Inteligente de Relatórios Genéticos")

st.write("Projeto desenvolvido para o Challenge Dasa.")

with open("../data/exemplo_relatorio.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

st.header("Paciente")
st.write(dados["paciente"])

st.header("Predisposições Genéticas")

for item in dados["predisposicoes"]:
    st.write(f"### {item['condicao']}")
    st.write(f"Risco: {item['risco']}")
    st.write(item["descricao"])

st.header("Ancestralidade")
st.write(dados["ancestralidade"])
