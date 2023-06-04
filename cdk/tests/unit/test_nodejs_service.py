# TODO: Use mocks? Now the Nodejs stack is explicitly dependent on the Base stack

# import os

# import aws_cdk as core
# import aws_cdk.assertions as assertions

# from cdk.src.nodejs_stack import NodejsService

# env = core.Environment(
#     account=os.getenv("AWS_ACCOUNT_ID"), region=os.getenv("AWS_DEFAULT_REGION")
# )

# def test_task_created():
#     app = core.App()
#     stack = NodejsService(app, "baseplatform", env=env)
#     template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::ECS::TaskDefinition", {
#         "Cpu": "256"
#     })
