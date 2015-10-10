from distutils.core import setup
setup(
  name = 'apfft',
  packages = ['apfft'], # this must be the same as the name above
  version = '0.3',
  description = 'Provides arbitrary precision FFTs using the mpmath package',
  author = 'David Stein',
  author_email = 'dbstein@math.ucdavis.edu',
  url = 'https://github.com/dbstein/apfft', # use the URL to the github repo
  download_url = 'https://github.com/dbstein/apfft/tarball/0.3', # I'll explain this in a second
  keywords = ['arbitrary precision', 'fft', 'fourier'], # arbitrary keywords
  classifiers = [],
)
