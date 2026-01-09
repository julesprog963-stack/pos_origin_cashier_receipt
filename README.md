# pos_origin_cashier_receipt

Muestra el cajero origen en el ticket del POS usando el campo `origin_cashier_id` provisto por `pos_origin_cashier`.

## Instalación / upgrade
- Copiar la carpeta `pos_origin_cashier_receipt` a tus `custom_addons` (ya está en `/mnt/extra-addons` según tu setup).
- Actualizar la lista de Apps y **Instalar/Actualizar** el módulo.
- Abrir POS, realizar una venta y reimprimir el ticket para verificar la línea de “Cashier Origen”.

## Detalles técnicos
- Se hereda la plantilla `point_of_sale.OrderReceipt` para añadir la línea.  
- Se hace patch a `Order.export_for_printing()` para enviar `origin_cashier_name`/`origin_cashier_id` al receipt (usa `employee_by_id` de `pos_hr`; fallback a N/A en el template).
- Assets cargados en `point_of_sale._assets_pos`.

## Checklist rápida
- Sin cambios a core.
- No añade ACLs ni permisos nuevos.
- Si no hay cajero origen, el ticket muestra “N/A” y no rompe el flujo.
