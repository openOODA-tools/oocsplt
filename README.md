# oocsplt: Sovereign Context Splitter & Stream Partitioner

<div align="center">

```
================================================================================
                                oocsplt
              Sovereign openOODA Context Splitter
================================================================================
```

**Sovereign Context Splitter & Stream Partitioner**  
*POSIX-compliant csplit alternative splitting streams into context-determined sections matched by regex patterns or line markers.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Streaming MCP stdio for AI agents  
Written in 100% pure native [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oocsplt/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oocsplt-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oocsplt/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oocsplt/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oocsplt-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oocsplt/uninstall.sh | bash
```

---

## 2. CLI Usage

```
Usage: oocsplt [OPTIONS] FILE PATTERN...

Splits files into context-determined sections matched by regex patterns or line numbers.

Options:
  -f, --prefix <PREFIX>    Use PREFIX instead of 'xx' for chunk filenames (default: 'xx')
  -n, --digits <DIGITS>    Use DIGITS digits instead of 2 for chunk suffixes (default: 2)
  -s, -q, --quiet          Do not print counts of output file sizes
  -z, --elide-empty-files  Remove empty output files
  -k, --keep-files         Do not remove output files on errors
      --dry-run            Simulate split operations without writing files to disk
  -d, --demo               Showcase context splitting on synthetic multi-chapter document
  -j, --json               Output structured JSON summary and chunk metadata
      --theme <THEME>      Select terminal color theme (ember, ocean, matrix, cyber, monochrome)
      --mcp                Run streaming MCP JSON-RPC 2.0 server on stdio
  -h, --help               Show this help message and exit
  -v, --version            Show version information and exit

Pattern Syntax:
  INTEGER                  Split up to, but not including, line number INTEGER
  /REGEXP/[OFFSET]         Split up to matching line, with optional +/- line offset
  %REGEXP%[OFFSET]         Skip up to matching line without outputting section
  {INTEGER}                Repeat previous pattern specified number of times
  {*}                      Repeat previous pattern as many times as possible
```

---

## 3. Pattern Matching & Section Slicing

* **Line Index Markers**: `oocsplt input.txt 10 20 30` partitions lines `1..9`, `10..19`, and `20..29`.
* **Context Delimiters**: `oocsplt doc.md '/^# Chapter/' '{*}'` splits at each chapter heading repeatedly until end of file.
* **Skip Delimiters**: `%SKIP%` discards preceding text sections while preserving subsequent matching slices.
* **Zero Ambient Authority**: File writing is bounded strictly through `&FsWriteCap` with dry-run verification mode.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oocsplt` runs a JSON-RPC 2.0 stdio server providing five sovereign splitting tools:

* `csplt_split`: Split input file or string content by pattern list or line numbers.
* `csplt_preview`: Preview split boundaries without writing to disk.
* `csplt_by_lines`: Split text into sections at specified line numbers.
* `csplt_by_pattern`: Split text into sections matching a delimiter pattern.
* `csplt_demo`: Return synthetic multi-chapter context splitting showcase.

```bash
oocsplt --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded**: Operates strictly with explicit tokens (`&FsReadCap`, `&FsWriteCap`, `&ProcessCap`, `&EnvCap`). Physical absence of ambient disk or network authority.
* **Negative-Trust Architecture**: Complete pattern grammar validation, bounds clamping, and memory-safe line slicing.
* **Hermetic Binary**: Standalone zero-dependency executable compiled via `oodac`.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
