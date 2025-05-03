#!/bin/bash
# Set Java headless mode environment variable
export JAVA_TOOL_OPTIONS="-Djava.awt.headless=true"

# Run PlantUML using xvfb-run to simulate a display and generate the diagram.
xvfb-run plantuml docs/project_flow.plantuml
