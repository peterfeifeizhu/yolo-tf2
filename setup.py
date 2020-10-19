from setuptools import setup, find_packages

install_requires = [
    'pandas==1.1.2',
    'lxml==4.5.0',
    'opencv_python_headless==4.2.0.34',
    'imagesize==1.2.0',
    'seaborn==0.10.0',
    'tensorflow==2.2.0',
    # 'tensorflow-gpu==2.2.0',
    'numpy~=1.19.2',
    'matplotlib==3.2.1',
    'imgaug==0.4.0',
    'imagecorruptions==1.1.0',
    'tensorflow-addons==0.10.0',
    'configparser~=5.0.0',
    'opencv-python~=4.2.0.34',
]

setup(
    name='yolo_tf2',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/emadboctorx/yolov3-keras-tf2',
    license='MIT',
    author='emadboctor',
    author_email='emad_1989@hotmail.com',
    description='yolo(v3/v4) implementation in keras and tensorflow 2.2',
    install_requires=install_requires,
    python_requires='>=3.7',
)