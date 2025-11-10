version: 0.2

phases:
  pre_build:
    commands:
      - echo Logging in to Amazon ECR...
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $ECR_REPO_URI
  build:
    commands:
      - echo Building Docker image...
      - docker build -t lambda-container .
      - docker tag lambda-container:latest $ECR_REPO_URI:latest
  post_build:
    commands:
      - echo Pushing image to ECR...
      - docker push $ECR_REPO_URI:latest
      - echo Writing image URI to imagedefinitions.json...
      - printf '[{"name":"LambdaContainerFunction","imageUri":"%s"}]' $ECR_REPO_URI:latest > imagedefinitions.json

artifacts:
  files:
    - imagedefinitions.json