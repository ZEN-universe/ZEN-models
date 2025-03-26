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
# Dataset Name (please change)

![Static Badge](https://img.shields.io/badge/ZEN--garden_version-CHANGE_THE_VERSION-%23627313?labelColor=%23215CAF) (<-- please change the ZEN-garden version in the badge)

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ZEN-universe/ZEN-models/data_structure_check.yml?branch=CHANGE_THE_BRANCH_NAME) (<-- please change branch name)

## 1. Description

### Purpose
<-- Provide a brief description of the dataset and its intended use.

### Associated publication (if applicable)
<-- Link to any associated publications or reports.

### Date
Creation date: YYYY-MM-DD (<-- please change)

## 2. Dataset Summary
A structured summary of key dataset attributes.

| Attribute                      | Description                   |
|--------------------------------|-------------------------------|
| **Spatial Scope**              | e.g., EU28                    |
| **Number of Nodes**            | e.g., 10                      |
| **Temporal Scope**             | e.g., 2020-2050               |
| **Number of Investment Years** | e.g., 4 (every 10 years)      |
| **Number of Time Steps**       | e.g., 8760 (aggregated to 100) |
| **Number of Technologies**     | e.g., 15                      |
| **Number of Energy Carriers**  | e.g., 10                      |

## 3. Framework Compatibility

- [x] This model runs with the main branch of ZEN-garden for the specified version.

<-- If the model does not run with the main branch of ZEN-garden, please specify the fork and branch that is compatible.

## 4. Comments
<-- Include any relevant notes, limitations, or recommendations for using this dataset.

## 5. Contributors
<-- List the contributors to this dataset.

- Erika Bünzli, ebuenzli@example.ch