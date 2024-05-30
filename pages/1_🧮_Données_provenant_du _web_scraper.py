import streamlit as st
import pandas as pd

st.set_page_config(page_title="Donnees venant de Web Scraper", page_icon="🧮")
st.markdown("# Web Scraper")
st.sidebar.header("Web Scraper")

st.write(
    """Cette page montre differentes donnees non nettoyer scraper avec Web Scraper"""
)



def webScraperData():
    st.title('Données scrappées avec Web Scraper')

    data_voiture = pd.read_csv('Expat_voitures.csv')
    data_motos = pd.read_csv('Expat_moto.csv')
    data_equipements = pd.read_csv('Expat_equipements_pieces.csv')

    tabVoiture, tabMoto, TabEquipements = st.tabs(['Voitures Expat Dakar', 'Motos Expat Dakar', 'Equipements Expat Dakar'])
    tabVoiture.write('Voitures Expat Dakar')
    tabMoto.write('Motos Expat Dakar')
    TabEquipements.write('Equipements Expat Dakar')

    with tabVoiture:
        st.dataframe(data_voiture, use_container_width=True)

    with tabMoto:
        st.dataframe(data_motos)

    with TabEquipements:
        st.dataframe(data_equipements)

webScraperData()