import dash
import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
app = dash.Dash(__name__)
# --- Déclaration des éléments
# ___ Noeuds = tables

noeuds = [
    {
        'data': {'id': short, 'label': label},
        'position': {'x': 20*lat, 'y': -20*long}
    }
    for short, label, long, lat in (
        ('code_client', 'TClients', 34.03, -118.25),
        ('no_employe', 'Temploye', 40.71, -74),
        ('no_commande', 'Tcommandes', 43.65, -79.38),
        ('no_commande_ref_produit', 'Tdetails_commandes', 45.50, -73.57),
        ('ref_produits', 'Tproduits', 49.28, -123.12),
        ('code_categorie', 'Tcategories', 41.88, -87.63),
        ('no_fournisseurs', 'Tfournisseurs', 42.36, -71.06)
    )
]

relations = [
    {'data': {'source': source, 'target': target}}
    for source, target in (
        ('no_commande', 'no_commande_ref_produit'),
        ('no_commande', 'code_client'),
        ('no_commande', 'no_employe'),
        ('ref_produits', 'no_commande_ref_produit'),
        ('ref_produits', 'code_categorie'),
        ('ref_produits', 'no_fournisseurs')
    )
]

elements = noeuds + relations

#   cyto.Cytoscape(
#   id='cytoscape-callbacks-1',
#        elements=elements,
#        style={'width': '100%', 'height': '400px'},
#       layout={
#            'name': 'grid'
#        }
#)
app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown-update-layout',
        value='grid',
        clearable=False,
        options=[
            {'label': name.capitalize(), 'value': name}
            for name in ['grid', 'random', 'circle', 'cose', 'concentric']
        ]
    ),
    cyto.Cytoscape(
        id='cytoscape-update-layout',
        layout={'name': 'circle'},
        style={'width': '100%', 'height': '450px'},
        elements=elements
    )
])


@app.callback(Output('cytoscape-update-layout', 'layout'),
              [Input('dropdown-update-layout', 'value')])
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }


if __name__ == '__main__':
    app.run_server(debug=True)
