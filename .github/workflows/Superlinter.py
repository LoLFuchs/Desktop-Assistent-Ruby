---
#################################
#################################
## Super Linter GitHub Actions ##
#################################
#################################
name: Lint Code Base

#############################
# Start the job on all push #
#############################
on:
  push:
    branches-ignore: [master, main]
    # Remove the line above to run when pushing to master
  pull_request:
    branches: [master, main]

###############
# Set the Job #
###############
jobs:
  build:
    # Name the Job
    name: Lint Code Base
    # Set the agent to run on
    runs-on: ubuntu-latest

    ############################################
    # Grant status permission for MULTI_STATUS #
    ############################################
    permissions:
      contents: read
      packages: read
      statuses: write

    ##################
    # Load all steps #
    ##################
    steps:
      ##########################
      # Checkout the code base #
      ##########################
      - name: Checkout Code
        uses: actions/checkout@v3
        with:
          # Full git history is needed to get a proper
          # list of changed files within `super-linter`
          fetch-depth: 0

      ################################
      # Run Linter against code base #
      ################################
      - name: Lint Code Base
        uses: super-linter/super-linter@v5
        env:
          VALIDATE_ALL_CODEBASE: false
          DEFAULT_BRANCH: main
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
