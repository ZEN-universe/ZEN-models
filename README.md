# Crystal Ball 

[![Static Badge](https://img.shields.io/badge/ZEN--garden_version-v2.2.20-%23627313?labelColor=%23215CAF)](https://github.com/ZEN-universe/ZEN-garden) 

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ZEN-universe/ZEN-models/data_structure_check.yml?branch=Crystal_Ball)](https://github.com/ZEN-universe/ZEN-models/actions)

## 1. Description

### Purpose
This dataset models the transition of the sector-coupled European energy system from 2022 to 2050.
It included 12 final energy demands: electricity, heat, passenger and truck transport, shipping, aviation, primary and secondary steel, ammonia, methanol, olefins, and cement.

The dataset contains capacity expansion constraints.

### Date
Creation date: 26-03-2025

## 2. Dataset Summary
A structured summary of key dataset attributes.

| Attribute                      | Description                |
|--------------------------------|----------------------------|
| **Spatial Scope**              | EU27 + NO, CH, UK - MT, CY |
| **Number of Nodes**            | 28                         |
| **Temporal Scope**             | 2022-2050                  |
| **Number of Investment Years** | 15 (every 2 years)         |
| **Number of Time Steps**       | 8760 (aggregated to 10)    |
| **Number of Technologies**     | 82                         |
| **Number of Energy Carriers**  | 30                         |

## 3. Framework Compatibility

- [x] This model runs with the main branch of ZEN-garden for the specified version.

## 4. Comments
It is the same dataset as the Optimism/Pessimism dataset, except for the treatment of carbon management technologies, as described in the paper

## 5. Contributors

- Jacob Mannhardt, jmannhardt@ethz.ch