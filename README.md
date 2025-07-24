# qualgent-appwright-orchestrator
CLI &amp; Backend Service for AppWright Test Orchestration (QualGent Coding Challenge)

# QualGent AppWright Orchestrator

## Overview

This project provides a modular CLI tool and backend service for queuing, grouping, and deploying AppWright tests across devices, emulators, and BrowserStack.  
Built for the QualGent Backend Coding Challenge.

---

## Features

- **Modular REST backend** with Redis
- **CLI (`qgjob_cli.py`)** for job submission and status checks
- **Job grouping** by app version for device install efficiency
- **GitHub Actions** workflow for CI integration

---

## Quickstart

### 1. Prerequisites

- **Python 3.7+**
- **Redis** (local or Docker)

### 2. Install Dependencies

```sh
pip install -r requirements.txt
