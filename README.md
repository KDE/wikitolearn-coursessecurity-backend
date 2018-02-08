# wikitolearn-coursessecurity-backend

## Synopsis
WikiToLearn ChaptersSecurity Backend is backend service of the WikiToLearn architecture.
Its aim is to serve a RESTful HATEOAS API thanks to Python Eve.

## Development
We use Docker to speed-up development and setup the environment without any dependency issues.

### Minimum requirements
* Docker Engine 17.09.0+

### How to run
It is advisable to run using the `docker-compose.yml` file provided.

Run instructions:

* Build all docker containers with: `docker-compose -f docker-compose.yml  -f docker-compose-dev-deps.yml build`
* Run all docker containers with: `docker-compose -f docker-compose.yml  -f docker-compose-dev-deps.yml up`

## Versioning
We use [SemVer](http://semver.org/) for versioning.

## License
This project is licensed under the AGPLv3+. See the [LICENSE.md](LICENSE.md) file for details.