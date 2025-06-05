___
___
# DELETE THIS SECTION AFTER COMPLETING THE TEMPLATE

## Workflow to add a new dataset
1. Create a new branch with the name of the dataset on Github.
2. Clone the new branch to your local machine: `git clone -b <branch-name> git@github.com:ZEN-universe/ZEN-models.git`
3. Add your dataset to the `data` folder. The first level of `data` should contain the dataset and `config.json` file.
4. Fill out the template below, follow the "<--" instructions
5. Delete this section and all the extra comments below
6. Commit and push your changes to the new branch.

___
___
# Climate-resilience

[![Static Badge](https://img.shields.io/badge/ZEN--garden_version-CHANGE_THE_VERSION-%23627313?labelColor=%23215CAF)](https://github.com/ZEN-universe/ZEN-garden) (<-- please change the ZEN-garden version in the badge)

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ZEN-universe/ZEN-models/data_structure_check.yml?branch=CHANGE_THE_BRANCH_NAME)](https://github.com/ZEN-universe/ZEN-models/actions) (<-- please change branch name)

## 1. Description

### Purpose
This dataset descibe the European energy system model utilized in the work "Climate-resilient panning of energy systems via system-informed identification of stressful events". The model includes climate-related time series for all the 60 climate scenarios considered. 

### Associated publication (if applicable)
Publication currently under review. 

### Date
Creation date: 25-11-2024

## 2. Dataset Summary
A structured summary of key dataset attributes.

| Attribute                      | Description                   |
|--------------------------------|-------------------------------|
| **Spatial Scope**              | EU28                    |
| **Number of Nodes**            |  28                      |
| **Temporal Scope**             | 2050, fully hourly resolved               |
| **Number of Investment Years** | 1      |
| **Number of Time Steps**       | 8760 |
| **Number of Technologies**     | 30                      |
| **Number of Energy Carriers**  | 9                     |

## 3. Framework Compatibility

- [x] This model runs with the main branch of ZEN-garden for the specified version.


## 4. Comments
This model produces 60 single-climate system, via the scenario analysis feature of ZEN-garden. 

## 5. Contributors
- Francesco De Marco, fdemarco@ethz.ch
- Jacob Mannhardt, jmannhardt@ethz.ch

- Erika Bünzli, ebuenzli@example.ch
