{
    "name": "customer_sales_order_history",
    "version": "1.2",
    "category": "",
    "summary": "customer_sales_order_history",
    "description": "This module is customer_sales_order_history",
    "depends": ["base", "sale"],
    "data": [
        # views
        "security/ir.model.access.csv",
        "data/stage_data.xml",
        "wizard/custom_setting_view.xml",
        "views/history_view.xml",
    ],
    "installable": True,
    "application": True,
}
