#!/bin/bash

echo "Please insert the USB stick and press Enter:"
read

# Find the block device of the USB stick
block_device=$(lsblk | grep -E '^sd.*[^0-9]$' | tail -1 | awk '{print $1}')

echo "The block device of the USB stick is: /dev/$block_device"

