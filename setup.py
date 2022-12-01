from setuptools import setup

package_name = 'settei'

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
            'settei = settei.settei:main',
            'service = settei.service_member_function:main',
            'client = settei.client_member_function:main',
            'talker = settei.publisher_member_function:main',
            'listener = settei.subscriber_member_function:main',
        ],
    },
)
