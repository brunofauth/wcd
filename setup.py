from setuptools import setup


if __name__ == "__main__":
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()

    setup(
        name="wcd",
        version="0.0.1",
        license="MIT",

        author="Bruno Fauth",
        author_email="bvfauth@hotmail.com",

        description="A daemon which manages your desktop wallpapers. Sort of the 'mpd' of wallpapers.",
        long_description=long_description,
        long_description_content_type="text/markdown",

        packages=["wcd"],

        url="http://github.com/brunofauth/wcd",
        project_urls={"Bug Tracker": "https://github.com/brunofauth/wcd/issues"},

        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License"
        ],
        python_requires=">=3.7"
    )

