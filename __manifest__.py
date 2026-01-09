{
    "name": "POS Origin Cashier Receipt",
    "version": "17.0.1.0.0",
    "summary": "Muestra el cajero origen en el ticket del Punto de Venta.",
    "category": "Point of Sale",
    "author": "JDA SOLUTIONS",
    "license": "LGPL-3",
    "website": "https://github.com/julesprog963-stack/pos_origin_cashier_receipt",
    "depends": ["point_of_sale", "pos_hr", "pos_origin_cashier"],
    "data": [],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_origin_cashier_receipt/static/src/js/receipt_origin_cashier_patch.js",
            "pos_origin_cashier_receipt/static/src/xml/receipt_origin_cashier.xml",
        ],
    },
    "images": [
        "pos_origin_cashier_receipt/static/description/icon.png",
    ],
    "application": False,
    "installable": True,
}
