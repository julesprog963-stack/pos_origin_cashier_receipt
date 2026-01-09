/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Order } from "@point_of_sale/app/store/models";

patch(Order.prototype, {
    export_for_printing() {
        const data = super.export_for_printing(...arguments);
        const originId = this.origin_cashier_id || null;
        const originEmployee =
            originId && this.pos?.employee_by_id ? this.pos.employee_by_id[originId] : null;

        return {
            ...data,
            origin_cashier_id: originId,
            origin_cashier_name: originEmployee?.name || null,
        };
    },
});
