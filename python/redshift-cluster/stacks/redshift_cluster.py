# https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.core.html
# https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_redshift.html
from aws_cdk import (
    core,
    aws_ec2,
    aws_redshift
)


class RedshiftClusterStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc: aws_ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.cluster = aws_redshift.Cluster(
            scope=self,
            id="RedshiftCluster",
            # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_redshift/Login.html
            # The Login object creates and stores a Secrets Manager generated password by default,
            # so there's no need to put your secrets in the CDK code directly
            master_user=aws_redshift.Login(
                master_username="admin"
            ),
            publicly_accessible=True,
            cluster_type=aws_redshift.ClusterType.MULTI_NODE,
            number_of_nodes=3,
            vpc=vpc
        )

        core.CfnOutput(
            scope=self,
            id="cluster_name",
            value=self.cluster.cluster_name
        )

        core.CfnOutput(
            scope=self,
            id="cluster_endpoint",
            value=self.cluster.cluster_endpoint.socket_address
        )
