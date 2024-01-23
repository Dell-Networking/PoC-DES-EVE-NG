# PoC DES EVE-NG


[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](#-how-to-contribute)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Dell-Networking/PoC-SONiC-template/blob/main/LICENSE.md)
[![GitHub issues](https://img.shields.io/github/issues/Dell-Networking/PoC-SONiC-template)](https://github.com/Dell-Networking/PoC-SONiC-template/issues)

Built and maintained by [Ben Goldstone](https://github.com/benjamingoldstone/) and [Contributors](https://github.com/Dell-Networking/PoC-SONiC-template/graphs/contributors)

------------------

This repo contains step-by-step instructions on how to deploy Dell Enterprise SONiC on EVE-NG.


## Contents

- [Description and Objective](#-description-and-objective)
- [Requirements](#-requirements)
- [Procedure](#-procedure)
- [How to Contribute](#-how-to-contribute)


## 🚀 Description and Objective
Welcome to the Dell Enterprise SONiC on EVE-NG project! This repository provides comprehensive instructions, configurations, and resources to seamlessly deploy Dell Enterprise SONiC (Software for Open Networking in the Cloud) within the EVE-NG virtual environment. SONiC offers a modern, open-source network operating system that brings the power of cloud principles to the network.

## 📋 Requirements

**Prerequisites:**    
EVE-NG server  
Dell Enterprise SONiC virtual switch image   

**Code versions used:**    
EVE-NG: EVE-COM-5.0.1-19  
DES: Enterprise_SONiC_OS_4.1.1.img

## 👏 Procedure
**Modifying Config File & Adding SONiC Image**  
- Under the SRC folder open the "config.json" file and your EVE-NG server credentials 
- Change the filename and extension of your Dell Enterprise SONiC image from Enterprise_SONiC_OS_4.1.1.img to virtioa.qcow2 
- Move the virtioa.qcow2 file to the SRC folder
  
**Uploading DES Image & Template to EVE-NG Server**  
- Run the "scp-files-to-server.py" script 

**Adding DES Virtual Switch to EVE-NG Lab**  
- Run the "spin-up-des-switch.py" script


## 👏 How to Contribute
We welcome contributions to the project. Please reference the [CONTRIBUTING](https://github.com/Dell-Networking/PoC-Index/blob/main/CONTRIBUTING.md) guide in the PoC-Index repo for more details (this guide is common across Dell Networking PoC projects).



