# https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.core.html
from aws_cdk import core

from stacks.vpc import VpcStack
from stacks.redshift_cluster import RedshiftClusterStack


app = core.App()

RedshiftClusterStack(
    app,
    "RedshiftClusterStack",
    vpc=VpcStack(app, "VpcStack").vpc
)

app.synth()
