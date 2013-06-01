#!/bin/bash
SAMPLES=$(ls .samples)
WC=$(wc .samples/* | tail -1 | awk '{print $1}')
args=$SAMPLES" "$WC
bin/PCAPlot $args

