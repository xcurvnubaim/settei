from setuptools import setup

package_name = 'settei2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zharif',
    maintainer_email='zhariffmarzuqi@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'settei2 = settei2.settei2:main',
            'service = settei2.service_member_function:main',
            'client = settei2.client_member_function:main',
        ],
    },
)
