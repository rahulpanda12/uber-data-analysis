import kagglehub

# Download latest version
path = kagglehub.dataset_download("bhanupratapbiswas/uber-data-analysis")

print("Path to dataset files:", path)