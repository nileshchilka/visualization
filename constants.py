apmt_theme = """
        <style>
            body{
                background-color: transparent;
            }
            
            #root{
                background-color: white !important;
            }
            
            /* section color to white*/
            section[data-testid="stSidebar"] {background-color:white;}
            
            /* when selected change color*/
            .css-pkbazv {
            color: #ff6441;
            overflow: hidden;
            white-space: nowrap;
            text-overflow: ellipsis;
            display: table-cell;
            }
            
            /* by default all color in section to black*/
            .css-17lntkn {
            color: black;
            overflow: hidden;
            white-space: nowrap;
            text-overflow: ellipsis;
            display: table-cell;
            }
            
            .css-j7qwjs {
            display: flex;
            }
            
            span:hover {
            color: #ff6441;
            background-color: transparent;
            }
            
            a:hover {
            color: #ff6441;
            }
            
            /* For Title*/
            .css-10trblm {
            color: #ff6441;
            position: relative;
            flex: 1 1 0%;
            margin-left: calc(3rem);
            }
            
            /* To remove hamberger and made with streamlit*/
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            /* To remove top space*/
            div.block-container{padding-top:0rem;}
            
        </style>
    """

apmt_logo_small = 'images/apm-terminals-logo-small.png'

colors_list = ["#ff6441","#3c3c46","#5a6e7d","#e6ebf2","#0a6e82","#f0be78","#42B0D5","#aab4c3"]

colors_teu = {
        "APMT": {
            '0-250': '#ff6441',
            '250-1000': '#3c3c46',
            '1000-4000': '#5a6e7d',
            '4000-8000': '#e6ebf2',
            '8000-12000': '#0a6e82',
            '12000-16000': '#f0be78',
            '16000-30000': '#42B0D5',
        },
        "Non APMT": {
            '0-250': '#ff6441',
            '250-1000': '#3c3c46',
            '1000-4000': '#5a6e7d',
            '4000-8000': '#e6ebf2',
            '8000-12000': '#0a6e82',
            '12000-16000': '#f0be78',
            '16000-30000': '#42B0D5',
        }
    }

colors_dur = {
        "APMT": {
            '0-10': '#ff6441',
            '10-20': '#3c3c46',
            '20-30': '#5a6e7d',
            '30-40': '#e6ebf2',
            '40-50': '#0a6e82',
            '50-60': '#f0be78',
            '60-70': '#42B0D5',
            '70+': '#aab4c3'
        },
        "Non APMT": {
            '0-10': '#ff6441',
            '10-20': '#3c3c46',
            '20-30': '#5a6e7d',
            '30-40': '#e6ebf2',
            '40-50': '#0a6e82',
            '50-60': '#f0be78',
            '60-70': '#42B0D5',
            '70+': '#aab4c3'
        }
    }
