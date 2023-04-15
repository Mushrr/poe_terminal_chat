from setuptools import setup

setup(
        name="poe_terminal_chat",
        version="0.0.1",
        descrption="poe(a third part AI assistant) terminal chat, can have accesses of chatgpt and claude",
        url="https://github.com/Mushrr/poe_terminal_chat",
        author="Mushrr",
        author_email="huangxingjiegkd@163.com",
        license="MIT",
        packages=["poe_terminal_chat"],
        entry_points = {
            'console_scripts': ['poechat=poe_terminal_chat.src.entry:main']
            },
        install_requires=[
            "poe-api>=0.2.10",
            "requests>=2.28.2",
            "python-dotenv>=1.0.0"
            ]
        )
