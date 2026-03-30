___
# Beyond pipelines: Multi-modal CO<sub>2</sub> transport enables timely CO<sub>2</sub> capture, transport, and storage deployment

[![Static Badge](https://img.shields.io/badge/ZEN--garden_version-v2.6.14-%23627313?labelColor=%23215CAF)](https://github.com/ZEN-universe/ZEN-garden)

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ZEN-universe/ZEN-models/data_structure_check.yml?branch=Beyond_pipelines_2026)](https://github.com/ZEN-universe/ZEN-models/actions)

## 1. Description

### Purpose
This data set models the expansion of a CO<sub>2</sub> capture, transport, and storage 
infrastructure from emitters in Switzerland to storage sites in the North Sea.


### Associated publication (if applicable)
Submitted to International Journal of Greenhouse Gas Control. 

### Date
Creation date: 12.02.2026

## 2. Dataset Summary
A structured summary of key dataset attributes.

| Attribute                      | Description                        |
|--------------------------------|------------------------------------|
| **Spatial Scope**              | CH plus nodes in DE,BE,NL,DK,NO,UK |
| **Number of Nodes**            | 60                                 |
| **Temporal Scope**             | 2026-2050                          |
| **Number of Investment Years** | 9 (every 3 years)                  |
| **Number of Time Steps**       | 1 per year                         |
| **Number of Technologies**     | 16                                 |
| **Number of Energy Carriers**  | 10                                 |

## 3. Framework Compatibility

This model does not run with the main branch of ZEN-garden for the specified version.
Instead, it can be run with the fork "Beyond_pipelines_2026" of ZEN-garden, which 
includes the specific functionality to model the expansion of CO<sub>2</sub> capture, 
transport, and storage infrastructure.

The respective model can be found at: 
https://github.com/johburger/ZEN-garden/tree/Beyond_pipelines_2026

## 4. Comments
Two datasets are provided: the base dataset (CH_multi_modal) and the scenario with a 
local storage site in Switzerland (CH_multi_modal_local_storage). 

## 5. Contributors
- Johannes Burger, jburger@ethz.ch