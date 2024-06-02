/** @odoo-module */
import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { useService } from "@web/core/utils/hooks";

export class TreeButtonController extends ListController {
    setup() {
        super.setup();
        this.actionManager = useService("action");
    }

    createFutureLead() {
        this.do_action({
            type: 'ir.actions.act_window',
            res_model: 'crm.lead',
            views: [[false, 'form']],
            target: 'current',
            context: {
                default_name: 'Future Lead',
                default_type: 'opportunity',
            },
        });
    }
}

registry.category("views").add("button_in_tree", {
    ...listView,
    Controller: TreeButtonController,
    buttonTemplate: "button_in_tree",
});
