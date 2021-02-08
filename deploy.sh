ssh -o StrictHostKeyChecking=no root@autolib.uz << 'ENDSSH'
 cd /autolib/autolib
 docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
 docker build -t registry.gitlab.com/humofx/autolib .
 docker pull registry.gitlab.com/humofx/autolib/master
 docker-compose up -d
ENDSSH