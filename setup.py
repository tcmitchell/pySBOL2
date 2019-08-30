from setuptools import setup

setup(name='sbol',
      version='2.3.3-beta',
      description='Pure Python implementation of SBOL standard',
      url='https://github.com/llotneb/SBOL.git',
      author='Benjamin Toll',
      author_email='Ben.Toll@raytheon.com',
      license='Apache-2',
      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 4 - Beta',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: Apache Software License',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6'
      ],
      # What does your project relate to?
      keywords='synthetic biology',
      packages=['sbol'],
      install_requires=[
          'rdflib',
          'deprecated',
          'lxml'
      ],
      zip_safe=False)