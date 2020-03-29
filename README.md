# SmartNews

Smart News application developed using Django, including for the moment:

  * ***Authentication***
  * ***SmartNewsApp***

The project is developed adhering as much as possible the 12 factor guidelines.

The source code for this project is available from: https://github.com/GerardGuerrero/SmartNews

## Getting Started ???

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites and important information for the evaluation

In order to allow the evaluation of the project delivery, a new branch has been developed infringing some rules that they could not be breached in *master* branch. This new branch is ***first-assigment-evaluation***.

## How to run or deploy SmartNewsApp application

### Running SmartNewsApp application with Docker

Explain how to run the automated tests for this system

```
docker-compose up --build
```

In order to evaluate the project, you need to access *fisrt-assigment-evaluation* branch:

```
git checkout first-assigment-evaluation
```

### Running SmartNewsApp application on local host

First of all, you need to go to the project main directory (e.g. *SmartNews*):

```
$ cd SmartNews
```

Then, you have to activate de virtual environment:

* Linux
  ```
  $ source venv/bin/activate
  ```

* Windows
  ```
  cd venv
  .\Scripts\activate
  cd ..
  ```

Also in this case, in order to evaluate the project, you need to access *fisrt-assigment-evaluation* branch:

```
git checkout first-assigment-evaluation
```

And finaly you can run the server using:

```
python manage.py runserver
```

### Deploying SmartNewsApp application on Heroku

In order to deploy the app on Heroky, you just have to follow this link:
https://smart-news-application.herokuapp.com


## How to check authentication required functions

In all cases, to test how superuser works, the access credentials are:


* *user*: ***admin***
* *password*: ***admin***


And in order to try how a simple user interact, you can login with these others:


* *user*: ***ferran***
* *password*: ***12345verdes***


You can also create new users in all cases.

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Rafa Cucurull** - [RafaCucurull](https://github.com/RafaCucurull)
* **Ivan Cortés** - [ivancg98](https://github.com/ivancg98)
* **Gerard Guerrero** - [GerardGuerrero](https://github.com/GerardGuerrero)
* **Robert Torres** - [TorresTosquella](https://github.com/TorresTosquella)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
