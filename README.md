# Description

The **EurekaQuery** project aims to enhance the accessibility and analysis of scientific literature. By integrating Flask as the web framework and leveraging the OpenAI API, the platform specializes in transforming research questions, stated in natural language, into structured PubMed queries. **EurekaQuery** is designed to make scientific discoveries more accessible, catering to a wide audience, from seasoned researchers to those new to medical research.

The core functionality of **EurekaQuery** revolves around the use of natural language processing (NLP) to dissect and understand research questions. However, its application is specifically tailored to analyze the structure of these questions based on the PICO (Population, Intervention, Comparison, Outcome) framework, a method commonly used in evidence-based practice to formulate clinical and health-related questions. This focused application of NLP ensures that queries are generated with precision, directly reflecting the user's intent and the specific elements of their research inquiry.

Once a query is crafted and executed on PubMed, **EurekaQuery** adopts a deterministic approach to analyze the search results and systematically organize the data into a dashboard. This dashboard provides an at-a-glance view of the research landscape related to the query, including key metrics, trends, and insights drawn from the retrieved literature. It is designed to give users a clear and concise overview of the available evidence.

# Getting Started
These instructions will guide you through setting up and running EurekaQuery on your local machine for development, testing, and deployment.

## Prerequisites

- Docker
- GNU Make

## Installation and Running

1. **Build the Development Environment:**

This command builds the Docker image for the development environment, ensuring live code updates via volume mounting.

```sh
make docker
```

2. **Access the Development Environment Console:**

For debugging or executing commands within the development environment, use:

```sh
make docker-bash
```

3. **Additional Commands:**

- **Stop Development Environment:** Stops and removes the development environment container.

```sh
make docker-stop-dev
```

- **Production Environment Setup:** Builds and runs the Docker image for the production environment using Gunicorn.

```sh
make docker-prod
```

- **Stop Production Environment:** Stops and removes the production environment container.

```sh
make docker-stop-prod
```

# Deployment
For deploying EurekaQuery in a production environment, follow the steps outlined in the Production Environment Setup. Ensure to configure your environment securely and review Docker and Gunicorn documentation for best practices in deployment.

# Contributing
Contributions to EurekaQuery are welcome! Please read through our contribution guidelines for details on our code of conduct and the process for submitting pull requests.