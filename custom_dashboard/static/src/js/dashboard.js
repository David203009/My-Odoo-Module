/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

class CustomDashboardComponent extends Component {
    static template = "custom_dashboard.DashboardComponent";

    setup() {
        this.state = useState({ message: "¡Hola desde Owl!" });
    }

    updateMessage() {
        this.state.message = "¡Mensaje actualizado!";
    }
}

CustomDashboardComponent.template = "custom_dashboard.DashboardComponent";

// Registra el componente en el sistema
registry.category("actions").add("custom_dashboard.component", CustomDashboardComponent);