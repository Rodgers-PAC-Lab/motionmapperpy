import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="motionmapperpy",
    version="1.0",
    author="Kanishk Jain",
    author_email="kanishkbjain@gmail.com",
    maintainer="Kanishk Jain",
    maintainer_email="kanishkbjain@gmail.com",
    description="A modified Python implementation of MotionMapper (https://github.com/gordonberman/MotionMapper)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bermanlabemory/motionmapperpy",
    download_url="https://github.com/bermanlabemory/motionmapperpy.git",
    python_requires=">=3.9",
    install_requires=[
        # cupy is a runtime dep but must be installed via conda
        # (PyPI 'cupy' is a source dist requiring nvcc).
        "numpy",
        "scipy",
        "matplotlib",
        "h5py",
        "hdf5storage",
        "scikit-learn",
        "scikit-image",
        "easydict",
        "umap-learn",
        "imageio",
        "moviepy",
        "tensorflow",
        "keras",
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
)