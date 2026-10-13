# DYMO LabelWriter 4XL macOS driver

A small installer containing the three printer files extracted from DYMO Connect 1.6.3.9 for macOS: the LabelWriter raster filter, the 4XL printer definition, and the 4XL icon. The extracted payload is approximately 340 KB. The files retain their original vendor bytes.

The raster filter contains both Apple Silicon and Intel code and links to libraries supplied by macOS. The printer definition defaults to DYMO 1744907 4-inch-by-6-inch shipping labels.

## Install

Download the `.pkg` from this repository's Releases page, open it, and complete the macOS administrator prompt. The installer places the driver files in `/Library/Printers`, attempts to restart the standard macOS print scheduler, and registers a USB-connected LabelWriter 4XL when it can discover one.

If the printer is unplugged or the print scheduler is unavailable, the driver files are still installed. Connect the printer and use System Settings → Printers & Scanners → Add Printer. Select the 4XL and choose **Use → Select Software → DYMO LabelWriter 4XL**.

If the software list is empty, choose **Use → Other…**. In the file chooser, press Command-Shift-G and enter `/Library/Printers/PPDs/Contents/Resources/lw4xl.ppd.gz`. Open that file, confirm that **Use** reads **DYMO LabelWriter 4XL**, and click **Add**.

The development Mac completed the driver installation successfully. Manual selection of the installed printer definition was accepted. Adding the printer then failed with **Bad file descriptor** because the macOS print scheduler could not open its listener socket. The installer's scheduler restart did not resolve that service failure. Restart the Mac if this occurs; physical printing remains unverified.

Existing DYMO applications and other printer queues are preserved. This installer does not install DYMO Connect, its web service, its support application, or a DYMO background daemon.

## Build

Run `./scripts/build-installer.sh` on macOS. The package is written to `dist/`. The package is a locally built, unsigned installer. Vendor ownership of the extracted files is retained; this repository does not apply a new license to them.

## Source and verification

The source is [DYMO's official Mac installer](https://dymoreleasecontent.blob.core.windows.net/dymo-release/DCDMAC/DCDMac1.6.3.9-Arm64.pkg), linked from the [DYMO download page](https://www.dymo.com/support?cfid=user-guide). Source and extracted-file checksums are recorded in `provenance.json`.

On the development Mac running macOS 27.0.1, the original vendor filter executed and printed its expected command-line usage. `codesign --verify --strict` reported an invalid signature for its ARM64 slice. The local source installer matched the content length and Content-MD5 served by DYMO's official download. The archive preserves the vendor filter without changing its signature.

Physical printing must be checked after installation. The first release records the verification completed on the development Mac; it does not claim compatibility testing on other Macs.
