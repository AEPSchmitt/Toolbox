#!/bin/bash

echo "===== 🚀 Boot Performance Stats ====="
echo

echo "⏱️  Overall Boot Time:"
systemd-analyze time
echo

echo "📊 Top 10 Slowest Services:"
systemd-analyze blame | head -10
echo

echo "🪢 Critical Chain (boot order bottlenecks):"
systemd-analyze critical-chain | head -20
echo

echo "📂 Failed Systemd Units (if any):"
systemctl --failed || echo "None"
