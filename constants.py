apmt_theme = """
        <style>
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
