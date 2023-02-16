from setuptools import setup
import os
from glob import glob 
package_name = 'py_autoware'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cheq',
    maintainer_email='cheqiang@kernelsoft.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
            'console_scripts': [
                    'initialpose = py_autoware.publisher_member_function_initialpose:main',
                    'initialgoal = py_autoware.publisher_member_function_initialgoal:main',
            ],
    },
)
