#!/bin/bash

echo "🧹 Cleaning old temporary results..."
rm -rf allure-results

# IMPORTANT: we keep history folder
mkdir -p allure-history

echo "🧪 Running pytest..."
pytest -s --alluredir=allure-results

# Check results exist
if [ ! -d "allure-results" ] || [ -z "$(ls -A allure-results)" ]; then
    echo "No test results found (tests may be skipped by Excel)."
    exit 1
fi

echo "📊 Generating Allure report with history..."

allure generate allure-results \
  --clean \
  -o allure-report \
  --history-dir allure-history

echo "💾 Saving history for next run..."
cp -r allure-report/history allure-history

echo "Opening report..."
allure open allure-report