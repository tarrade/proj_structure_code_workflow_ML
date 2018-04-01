# proj_structure_code_workflow_ML
How to structure python code some some generic ML project. The idea is to have a generic template with an automatic worksflow.


# structure

├── Makefile                <- tasks
├── config.yml              <- config file in YAML, can be exported as env vars if needed
├── config-private.yml      <- config file with private config (password, api keys, etc.)
├── data
│   └── raw
│   ├── intermediate
│   ├── processed
│   ├── temp
├── results
│   ├── outputs
│   ├── models
├── documents
│   ├── docs
│   ├── images
│   └── references
├── notebooks               <- notebooks for explorations / prototyping
└── src                     <- all source code, internal org as needed
