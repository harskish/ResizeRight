from setuptools import setup, find_packages

setup(
  name = 'resize-right',
  packages = find_packages(exclude=[]),
  version = '0.0.2',
  license = 'MIT',
  description = 'Resize Right',
  author = 'Assaf Shocher',
  author_email = 'assafshocher@gmail.com',
  url = 'https://github.com/assafshocher/ResizeRight',
  keywords = [
    'deep learning',
    'image resize'
  ],
  install_requires=[
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
