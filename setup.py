from setuptools import setup

setup(name='engformat',
      version='0.0.3',
      description='A series for tools for displaying engineering calculations according to the Engineering Standard Format',
      url='',
      author='Maxim Millen',
      author_email='millen@fe.up.pt',
      license='MIT',
      packages=[
        'engformat',
    ],
    install_requires=[
        "numpy",
        "bwplot"
    ],
      zip_safe=False)