 #!/bin/bash
mv docker-compose-only-test-purposes.yml docker-compose.yml
docker-compose down
mv docker-compose.yml docker-compose-only-test-purposes.yml
