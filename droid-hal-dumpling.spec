# Reference: dhd/droid-hal-device.inc

%define vendor oneplus
%define device dumpling

%define vendor_pretty OnePlus
%define device_pretty OnePlus 5T (A5010)

%define droid_target_aarch64 1
%define enable_kernel_update 1

%define android_config \
  #define WANT_ADRENO_QUIRKS 1 \
%{nil}

%define straggler_files \
  /bt_firmware \
  /dsp \
  /firmware \
  /persist \
  /d \
  /product \
  /verity_key \
%{nil}

# Ignore unpackaged (and broken) /bugreports & /sdcard symlinks
%define _unpackaged_files_terminate_build 0

# Don't create systemd mount units for these
%define makefstab_skip_entries /dev/cpuctl /dev/stune /sys/fs/pstore /mnt/vendor/persist

%include rpm/dhd/droid-hal-device.inc
