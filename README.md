# SmartNews

Smart News application developed using Django, including for the moment:

  * ***Authentication:*** *an app that uses the powerful built-in user authentication system that allows you to quickly and easily add login, logout, and registration functionalities to a website.*
  * ***SmartNewsApp:*** *the main app of the project. It hosts the definition of models (Date, Source, Country, Topic, Statistic and News) and templates.*

The project is developed adhering as much as possible the ***12 factor guidelines***.

The source code for this project is available from: https://github.com/GerardGuerrero/SmartNews

[![Build Status](https://travis-ci.org/GerardGuerrero/SmartNews.svg?branch=master)](https://travis-ci.org/GerardGuerrero/SmartNews)

## Prerequisites and important information for the evaluation

In order to allow the evaluation of the project delivery, a new branch has been developed infringing some rules that they could not be breached in *master* branch. This new branch is ***first-assigment-evaluation***.

## How to run or deploy SmartNewsApp application

### Running SmartNewsApp application with Docker

If you want to run the application with Docker, you should execute the following command:

```
docker-compose up --build
```

*(In case of not having the necessary permissions, it would be necessary to put the word* ***sudo*** *before)*

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

* *Linux*
  ```
  $ source venv/bin/activate
  ```

* *Windows*
  ```
  cd venv
  .\Scripts\activate
  cd ..
  ```

Also in this case, in order to evaluate the project, you need to access *fisrt-assigment-evaluation* branch:

```
git checkout first-assigment-evaluation
```

And finally you can run the server using:

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
* [Travis CI](https://docs.travis-ci.com/) - Continuous Integration
* [Heroku](https://devcenter.heroku.com/) - PaaS used to deploy the app

## Version control

We use [GitHub](https://github.com/) for development version control using Git.

## Authors

* **Rafa Cucurull** - [RafaCucurull](https://github.com/RafaCucurull)
* **Ivan Cortés** - [ivancg98](https://github.com/ivancg98)
* **Gerard Guerrero** - [GerardGuerrero](https://github.com/GerardGuerrero)
* **Robert Torres** - [TorresTosquella](https://github.com/TorresTosquella)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
