import sys

from setuptools import setup, find_packages

# version = sys.argv[-1].split('=')[1]
# sys.argv = sys.argv[0:len(sys.argv) - 1]

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name="WeTextProcessing-fix-2",
    version="0.0.1",
    author="Lyming",
    author_email="331661029@qq.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="WeTextProcessing, including TN & ITN",
    url="https://github.com/lym331461029/WeTextProcessing",
    packages=find_packages(),
    package_data={
        "tn": [
            "*.fst", "chinese/data/*/*.tsv", "english/data/*/*.tsv",
            "english/data/*.tsv", "english/data/*/*.far"
        ],
        "itn": ["*.fst", "chinese/data/*/*.tsv"],
    },
    install_requires=['pynini==2.1.6', 'importlib_resources'],
    entry_points={
        "console_scripts": [
            "wetn = tn.main:main",
            "weitn = itn.main:main",
        ]
    },
    tests_require=['pytest'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
