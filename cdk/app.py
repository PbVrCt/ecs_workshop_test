#!/usr/bin/env python3
import os

import aws_cdk as cdk

from src.platform_stack import BaseVPCStack
from src.frontend_stack import FrontendService
from src.nodejs_stack import NodejsService
from src.crystal_stack import CrystalService

app = cdk.App()

_env = cdk.Environment(
    account=os.getenv("AWS_ACCOUNT_ID"), region=os.getenv("AWS_DEFAULT_REGION")
)

base_platform = BaseVPCStack(app, "ecsworkshop-base", env=_env)
nodejs_service = NodejsService(
    app,
    "ecsworkshop-nodejs",
    base_platform.ecs_cluster,
    base_platform.services_security_group,
    base_platform.service_discovery_namespace,
    env=_env,
)
crystal_service = CrystalService(
    app,
    "ecsworkshop-crystal",
    base_platform.ecs_cluster,
    base_platform.services_security_group,
    base_platform.service_discovery_namespace,
    env=_env,
)
FrontendService(
    app,
    "ecsworkshop-frontend",
    base_platform.ecs_cluster,
    base_platform.services_security_group,
    base_platform.service_discovery_namespace,
    env=_env,
)

app.synth()
