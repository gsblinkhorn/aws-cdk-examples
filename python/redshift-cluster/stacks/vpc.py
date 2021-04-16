from aws_cdk import (
    core,
    aws_ec2 as ec2
)


class VpcStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        _max_azs = 2

        self.vpc = ec2.Vpc(
            self,
            "VPC",
            max_azs=_max_azs,
            cidr="10.10.0.0/16",
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE,
                    name="Private",
                    cidr_mask=24
                )
            ],
            nat_gateways=_max_azs,
        )

        core.CfnOutput(
            scope=self,
            id="vpc_id",
            value=self.vpc.vpc_id
        )
