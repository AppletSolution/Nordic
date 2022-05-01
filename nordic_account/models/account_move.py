# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"

    client_booking_no = fields.Char("Client's Booking No")
    nordic_booking_no = fields.Char("Nordic's Booking No")
    cargo_out_date = fields.Date("Cargo Out Date")
    cargo_volume = fields.Float("Cargo Volume")
    commodity = fields.Char("Commodity")
    consignee_name = fields.Char("Consignee Name")
    container_no = fields.Char("Container No")
    departure_location = fields.Char("Departure Location")
    file_upper_run_date = fields.Date("File Upper Run Date")
    final_destination = fields.Char("Final Destination")
    id_ed_no = fields.Char("ID / ED No")
    job_no = fields.Char("Job No")
    no_of_id_ed= fields.Char("No of ED / ID")
    pickup_location = fields.Char("Pick Up Location")
    port_exam_date = fields.Date("Port Exam Date")
    service_type= fields.Many2one('sale.order.template')
    shipment_date = fields.Date("Shipment Date")
    shipment_name = fields.Char("Shipment Name")
    shipment_line_name = fields.Char("Shipment Line Name")
    track_no_mm = fields.Char("Myanmar Track No")
    track_no_th = fields.Char("Thailand Track No")
    track_type= fields.Char("Track Type")
    vessel_no = fields.Char("Vessel No")
    warehouse_id = fields.Many2one('stock.warehouse')
    eta_ygn_date = fields.Date("ETA YGN ")
    etd_ygn_date = fields.Date("ETD YGN ")
    eta_mwd_date = fields.Date("ETA MWD ")
    etd_mwd_date = fields.Date("ETD MWD ")
    eta_lcb_date = fields.Date("ETA LCB ")
    etd_lcb_date = fields.Date("ETD LCB ")
    eta_sva_date = fields.Date("ETA SVA ")
    etd_sva_date = fields.Date("ETD SVA ")
