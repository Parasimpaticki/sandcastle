from distutils.core import setup
setup(
  name = 'sandcastle',
  version = '1.2.2',
  description = 'A Python script for AWS S3 bucket enumeration.',
  author = 'Yasin Soliman',
  author_email = 'ysx.public@icloud.com',
  scripts=['sandcastle.py'],
  url = 'https://github.com/yasinS/sandcastle',
  download_url = 'https://github.com/yasinS/sandcastle/archive/1.2.2.tar.gz',
  keywords = ['amazons3', 'infosec', 'bucket'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Security",
    ],

)
