from setuptools import find_packages, setup

package_name = 'my_first_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Prathmesh Sharma',
    maintainer_email='prathmeshsharma72@gmail.com',
    description='My first ROS2 package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'first_node = my_first_robot.my_first_node:main',
        ],
    },
)
