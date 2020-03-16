A dummy repo for testing drone

To run drone locally:

# Step 1: Install docker and start the drone service.

On Ubuntu:

```bash
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

# Step 2: Install drone 0.8 command line interface tools

You can find more info on this step [here](https://0-8-0.docs.drone.io/cli-installation/).

**IMPORTANT**: WE ARE USING DRONE CI v0.8, NOT 1.x. The documentation and pipeline definition differ drastically between the two versions. When looking for docs, you should go to [this page](https://0-8-0.docs.drone.io/cli-installation/).

# Step 4: Create a drone pipeline

Move to the base directory of your repo and create a `.drone.yml`. This should look similar to the file included in this repo, e.g.:

```yaml
pipeline:
    backend:
        image: python
        commands:
            - sleep 15
            - echo $TEST_SECRET
            - pip install psycopg2
            - pip install pytest
            - python postgres_check.py
            - pytest
        secrets: [test_secret]
services:
    database:
        image: postgres
        environment:
            - POSTGRES_USER=postgres
            - POSTGRES_DB=test
```

This example demonstrates how to test a Python application that relies on a Postgres database. It also defines a secret, `test_secret`, that is passed into the the Python container as an environmental variable.

# Step 5: Run the pipeline

Run the drone pipeline using `drone exec`. For the particular example in this repo, we need to pass in the environment variable we defined in the `.drone.yml` file, like so

```bash
sudo TEST_SECRET=123 drone exec
```
