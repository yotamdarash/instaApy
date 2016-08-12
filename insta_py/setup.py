from setuptools import setup, find_packages

setup(name='insta_py',
      version='0.1',
      description='Unofficial wrapper for Instagram API',
      url='https://github.com/yotamdarash/instaApy',
      author='Yotam Daniel',
      author_email='yotam.darash@gmail.com',
      license='open',
      packages=find_packages(),
      install_requires=[
          'requests',
      ],
      zip_safe=False)
