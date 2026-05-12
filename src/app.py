import streamlit as st
import json

st.set_page_config(page_title="Genera AI", layout="wide")

st.title("🧬 Genera AI")
st.subheader("Interpretação Inteligente de Relatórios Genéticos")

st.write("Projeto desenvolvido para o Challenge Dasa.")

with open("../data/exemplo_relatorio.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

st.divider()

st.header("👤 Paciente")

col1, col2, col3 = st.columns(3)

col1.metric("Nome", dados["paciente"]["nome"])
col2.metric("Idade", dados["paciente"]["idade"])
col3.metric("Sexo", dados["paciente"]["sexo"])

st.divider()

st.header("🧬 Predisposições Genéticas")

for item in dados["predisposicoes"]:

    if item["risco"] == "Elevado":
        st.error(f"{item['condicao']} - Risco {item['risco']}")

    elif item["risco"] == "Moderado":
        st.warning(f"{item['condicao']} - Risco {item['risco']}")

    else:
        st.success(f"{item['condicao']} - Risco {item['risco']}")

    st.write(item["descricao"])

st.divider()

st.header("🌎 Ancestralidade")

st.write(dados["ancestralidade"])

st.divider()

st.info("⚠️ Este sistema não substitui acompanhamento médico profissional.")
