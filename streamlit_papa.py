import streamlit as st

st.title('Hello papa :)')

h = st.number_input('Hauteur (mm)')
l = st.number_input('Largeur (mm)')
p = st.number_input('Profondeur (mm)')
ep = st.number_input('Epaisseur (mm)')
nb_et_f = st.number_input('Nombre étagères fixes')
nb_et_a = st.number_input('Nombre etageres amovibles')

dim_planches_verticales = [ep, h - 2 * ep, p]
dim_planches_horizontales = [l, ep, p]
dim_fond = [l, h, ep]
dim_etagere_fixe = [l - 2 * ep, ep, p]
dim_etagere_amovible = [l - 2 * ep - 2, ep, p - 5]

st.write("\nPour ton meuble il faut : ")
st.write("- ", 2, " planches ", dim_planches_verticales[0], " x ", dim_planches_verticales[1], " x ", dim_planches_verticales[2], " mm")
st.write("- ", 2, " planches ", dim_planches_horizontales[0], " x ", dim_planches_horizontales[1], " x ", dim_planches_horizontales[2], " mm")
st.write("- ", 1, " planche ", dim_fond[0], " x ", dim_fond[1], " x ", dim_fond[2], " mm") 
if nb_et_f >= 2:
    st.write("- ", nb_et_f, " planches ", dim_etagere_fixe[0], " x ", dim_etagere_fixe[1], " x ", dim_etagere_fixe[2], " mm")
elif nb_et_f == 1:
    st.write("- ", nb_et_f, " planche ", dim_etagere_fixe[0], " x ", dim_etagere_fixe[1], " x ", dim_etagere_fixe[2], " mm")
if nb_et_a == 1:
    st.write("- ", nb_et_a, " planche ", dim_etagere_amovible[0], " x ", dim_etagere_amovible[1], " x ", dim_etagere_amovible[2], " mm")
elif nb_et_a >= 2:
    st.write("- ", nb_et_a, " planches ", dim_etagere_amovible[0], " x ", dim_etagere_amovible[1], " x ", dim_etagere_amovible[2], " mm")
