# --- STYLE CSS ---
st.markdown(f"""
    <link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">
    <style>
    /* UKRYCIE MENU STREAMLIT I STOPKI (Z zachowaniem przycisku panelu bocznego) */
    [data-testid="stToolbar"] {{visibility: hidden !important; display: none !important;}}
    footer {{visibility: hidden !important; display: none !important;}}
    #MainMenu {{visibility: hidden !important; display: none !important;}}
    .stDeployButton {{display: none !important;}}
    
    .stApp {{ background: linear-gradient(180deg, #FFFFFF 0%, #FFEBEE 100%) !important; }}
    
    /* Bezpieczne wymuszenie czcionki na całej aplikacji */
    * {{ font-family: 'Anton', sans-serif !important; }}
    html, body, [class*="st-"], .stMarkdown, label, p, span {{ color: {COLOR_TEXT}; }}
    
    /* NAPRAWA: Zabezpieczenie ikon systemowych Streamlit przed nadpisaniem czcionki Anton */
    [data-testid="stIconMaterial"], [data-testid="stExpander"] summary span, .material-symbols-rounded, .streamlit-expander-icon {{ 
        font-family: 'Material Symbols Rounded', sans-serif !important; 
    }}
    
    h1, h2, h3, h4 {{ color: {COLOR_PRIMARY} !important; text-transform: uppercase; text-align: center; }}
    
    [data-testid="stMetric"] {{
        background-color: white; padding: 15px; border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 1px solid #e0e0e0;
    }}
    .template-box {{
        background-color: #FFEBEE; padding: 15px; border-radius: 10px; border: 1px solid #FFCDD2; margin-bottom: 20px;
    }}
    .metric-card-red {{ background: linear-gradient(135deg, #FFEBEE 0%, #FFCDD2 100%); border-left: 5px solid #D32F2F; }}
    .metric-card-orange {{ background: linear-gradient(135deg, #FFF3E0 0%, #FFE0B2 100%); border-left: 5px solid #F57C00; }}
    .metric-card-green {{ background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%); border-left: 5px solid #388E3C; }}
    
    /* Kalendarz Sztabu */
    .calendar-grid {{ display: grid; grid-template-columns: repeat(7, 1fr); gap: 8px; width: 100%; margin-bottom: 20px; }}
    @media (max-width: 1200px) {{ .calendar-grid {{ grid-template-columns: repeat(4, 1fr); }} }}
    @media (max-width: 800px) {{ .calendar-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    .calendar-cell {{ background: #FFFFFF; border: 1px solid #E0E0E0; border-radius: 12px; padding: 10px; min-height: 150px; display: flex; flex-direction: column; }}
    .calendar-cell.today {{ border: 2px solid #D32F2F !important; background-color: #FFFDE7 !important; }}
    .calendar-cell-header {{ font-size: 0.85rem; font-weight: bold; color: {COLOR_PRIMARY}; text-transform: uppercase; margin-bottom: 2px; }}
    .calendar-cell-header.today-text {{ color: #D32F2F !important; }}
    .calendar-cell-date {{ font-size: 0.72rem; color: #666; margin-bottom: 8px; border-bottom: 1px solid #eee; padding-bottom: 5px; }}
    .staff-plan-tag {{ background: #FFEBEE; border: 1px solid #FFCDD2; border-left: 4px solid {COLOR_PRIMARY}; padding: 6px; margin-bottom: 6px; border-radius: 6px; font-size: 0.75rem; line-height: 1.3; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }}
    .staff-plan-group {{ font-weight: bold; color: {COLOR_TEXT}; display: block; font-size: 0.65rem; text-transform: uppercase; margin-bottom: 2px; }}
    </style>
    """, unsafe_allow_html=True)
