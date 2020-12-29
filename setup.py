import setuptools
import sys
from file_sync_tool import info

if sys.version_info < (3, 5):
    sys.exit('file_sync_tool requires Python 3.5+ to run')

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='file_sync_tool-kmi',
    version=info.__version__,
    author='Konrad Michalik',
    author_email='support@konradmichalik.eu',
    description='Synchronize files from and to host systems.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=info.__homepage__,
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Intended Audience :: Developers'
    ],
    python_requires='>=3.5',
    install_requires=[
        "future-fstrings>=1.2"
        "db-sync-tool-kmi>=2.2.5",
    ],
    entry_points={
        'console_scripts': [
            'file_sync_tool = file_sync_tool.__main__:main'
        ]
    },
)
