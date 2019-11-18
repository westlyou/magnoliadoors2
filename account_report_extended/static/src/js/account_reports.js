odoo.define('account_report_extended.account_report', function (require) {
    'use strict';

    var AccountReport = require('account_reports.account_report');

    AccountReport.include({
        render_searchview_buttons: function () {
            var self = this;
            this.$searchview_buttons.find('.js_account_salesperson_auto_complete').select2();
            if (this.report_options.users) {
                this.$searchview_buttons.find('[data-filter="salesperson"]').select2("val", this.report_options.user_ids);
            }
            this.$searchview_buttons.find('.js_account_salesperson_auto_complete').on('change', function () {
                self.report_options.user_ids = self.$searchview_buttons.find('[data-filter="salesperson"]').val();
                return self.reload().then(function () {
                    self.$searchview_buttons.find('.account_salesperson_filter').click();
                })
            });
            return this._super.apply(this, arguments);
        }
    })
});