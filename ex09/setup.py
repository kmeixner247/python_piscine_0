import setuptools


def main():
    """main function of setup.py"""
    setuptools.setup(
        name='ft_package',
        version='0.0.1',
        description='A sample test package',
        url='https://github.com/kmeixner247',
        author='kmeixner',
        author_email='kmeixner@student.42wolfsburg.de',
        packages=['ft_package'],
        license='MIT'
    )


if __name__ == "__main__":
    main()
