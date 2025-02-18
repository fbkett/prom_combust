import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Promociones de Combustible",
    page_icon="⛽",
    layout="wide"
)

# Título principal
st.title("⛽ Promociones de Combustible - Febrero 2025")

# Crear datos con la información real
data = {
    'Estación': [
        # YPF
        'YPF', 'YPF', 'YPF', 'YPF', 'YPF', 'YPF', 'YPF', 'YPF', 'YPF',
        # AXION
        'AXION', 'AXION', 'AXION', 'AXION', 'AXION', 'AXION', 'AXION', 'AXION',
        # SHELL
        'SHELL', 'SHELL'
    ],
    'Día': [
        # YPF
        'Lunes', 'Lunes', 'Todos los días', 'Todos los días', 'Miércoles', 'Miércoles',
        'Domingo', 'Martes', 'Sábados y domingos',
        # AXION
        'Todos los días', 'Viernes', 'Sábado', 'Lunes y viernes', 'Sábados', 
        'Domingos', 'Domingo', 'Miércoles',
        # SHELL
        'Todos los días', 'Todos los días'
    ],
    'Promoción': [
        # YPF
        'Galicia Crédito Master Premium + modo', 'Galicia Crédito Master + modo',
        'Modo + BNA Crédito', 'NaranjaN Crédito desde app YPF',
        'Modo + Macro Visa Signature Selecta', 'Modo + Macro Crédito Visa Platinum',
        'Modo + Ciudad/Buepp', 'Modo + Hipotecario Crédito', 'NaranjaN Debito desde app YPF',
        # AXION
        'BNA+', 'Reba (crédito American Express)', 'Modo + BBVA crédito',
        'Galicia Mas Mastercard premier (1) Premier', 'Modo + Supervielle (Clientes Identité/cuenta)',
        'Modo + Comafi', 'Modo + Buepp/Ciudad', 'Banco del Sol Debito',
        # SHELL
        'tarjeta NIU', 'Modo + BNA Crédito'
    ],
    'Descuento (%)': [
        # YPF
        15, 10, 15, 30, 30, 20, 10, 15, 30,
        # AXION
        10, 20, 30, 10, 20, 10, 15, 20,
        # SHELL
        30, 25
    ],
    'Tope de Gasto': [
        # YPF
        100000, 100000, 100000, 33333, 84000, 75000, 100000, 60700, 34000,
        # AXION
        150000, 25000, 15000, 100000, 25000, 40000, 67000, 25000,
        # SHELL
        20000, 80000
    ],
    'Tope Devolución': [
        # YPF
        15000, 10000, 15000, 10000, 25000, 15000, 10000, 15000, 10000,
        # AXION
        15000, 5000, 4500, 10000, 5000, 4000, 10000, 5000,
        # SHELL
        6000, 20000
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Agregar filtros en la barra lateral
st.sidebar.header("Filtros")
estacion_filter = st.sidebar.multiselect(
    "Seleccionar Estación",
    options=sorted(df['Estación'].unique()),
    default=sorted(df['Estación'].unique())
)

dia_filter = st.sidebar.multiselect(
    "Seleccionar Día",
    options=sorted(df['Día'].unique()),
    default=sorted(df['Día'].unique())
)

# Aplicar filtros
df_filtered = df[
    (df['Estación'].isin(estacion_filter)) &
    (df['Día'].isin(dia_filter))
]

# Mostrar la tabla con estilo
st.dataframe(
    df_filtered,
    use_container_width=True,
    hide_index=True,
    column_config={
        'Descuento (%)': st.column_config.NumberColumn(
            format="%d%%"
        ),
        'Tope de Gasto': st.column_config.NumberColumn(
            format="$%d"
        ),
        'Tope Devolución': st.column_config.NumberColumn(
            format="$%d"
        )
    }
)

# Información adicional
st.markdown("---")
st.markdown("""
    ### ℹ️ Información
    * Las promociones están sujetas a cambios sin previo aviso
    * Consulte términos y condiciones en cada estación de servicio
    * Algunas promociones requieren uso de aplicaciones específicas
    * Los topes de devolución pueden ser mensuales o por transacción
""") 