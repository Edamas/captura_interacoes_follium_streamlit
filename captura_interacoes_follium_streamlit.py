import streamlit as st
import folium
from streamlit_folium import st_folium

# Criar o mapa
m = folium.Map(location=[-15.7801, -47.9292], zoom_start=4)

# Adicionar um marcador inicial
folium.Marker(
    location=[-15.7801, -47.9292],
    popup="Centro do Brasil",
).add_to(m)

# Mostrar o mapa e capturar os eventos
output = st_folium(m, width=700, height=500)

# Verificar se o output está retornando corretamente
st.write(output)

# Exibir as interações do usuário (cliques, centro do mapa, zoom)
if output:
    if "center" in output:
        st.write("Centro do Mapa:", output["center"])
    if "zoom" in output:
        st.write("Zoom Atual:", output["zoom"])
    if "last_clicked" in output:
        st.write("Último Clique em:", output["last_clicked"])
