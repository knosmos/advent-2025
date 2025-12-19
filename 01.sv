`default_nettype none
`timescale 1ns/1ps
module solve_01 (
    input  wire         clk,
    input  wire         rst,
    input  wire         dir,    // 0: L, 1: R
    input  wire  [7:0]  data,
    input  wire         valid,
    output logic [15:0] res
);
    logic [7:0] cur;
    always_ff @(posedge clk) begin
        if (rst) begin
            res <= 16'd0;
            cur <= 7'd50;
        end else if (valid) begin
            if (dir == 0) begin
                res <= res + (cur - data % 100 <= 0 ? 1 : 0) + data / 100;
                cur <= (cur - data) % 100;
            end else begin
                res <= res + (cur + data % 100 >= 100 ? 1 : 0) + data / 100;
                cur <= (cur + data) % 100;
            end
        end
    end
endmodule
`default_nettype wire