cd docker

docker build --progress=plain -f Dockerfile-llama3-8b -t rick-morty-llama3-8b .

docker run --log-driver json-file --log-opt max-size=10m rick-morty-llama3-8b --network none

docker login

update dockerfile from docker/start.sh to start.sh and same for build.sh 

bash ../scripts/build.sh

docker run mavericb/ollama:llama3-8b-lilypad-v20240829062256 --network none

./stack run --network dev github.com/mavericb/lilypad-module-test:main
