# Changes to ecs-workshop

Someone asked me for help with the https://ecsworkshop.com/ so I made made a few changes to help him

## Prerequitsites

- Install python, venv, npm, typescript ...
- Configure the AWS CLI, bootstrap the AWS CDK.
- git clone https://github.com/PbVrCt/ecs_workshop_test

## Deploying the microservices

```
cd cdk
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cdk deploy ecsworkshop-base --require-approval never
cdk deploy ecsworkshop-nodejs --require-approval never
cdk deploy ecsworkshop-crystal --require-approval never
cdk deploy ecsworkshop-frontend --require-approval never
```

## Doing the blue/green deployment

```
cd ecs-workshop-blue-green-deployments
npm install
npm run build
npm run test
./bin/scripts/deploy-container-image-stack.sh
cd nginx-sample
git init
export AWS_DEFAULT_REGION=$(aws configure get region)
git remote add origin https://git-codecommit.$AWS_DEFAULT_REGION.amazonaws.com/v1/repos/nginx-sample
git checkout -b main
git remote -v
git add .
git commit -m "First commit"
```

Geneterate https (or ssh) git credentials for codecommit in the iam console

```
git push --set-upstream origin main
cd ..
./bin/scripts/deploy-pipeline-stack.sh
export ALB_DNS=$(aws cloudformation describe-stacks --stack-name BlueGreenPipelineStack --query 'Stacks[*].Outputs[?ExportName==`ecsBlueGreenLBDns`].OutputValue' --output text)
```