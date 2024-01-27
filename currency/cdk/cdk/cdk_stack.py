from aws_cdk import (
    Stack,
    aws_glue_alpha as glue,
    aws_glue as glue_cfn,
    aws_s3 as s3
)
import aws_cdk as core
from constructs import Construct


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        currency_bucket: s3.Bucket = s3.Bucket(
            self,
            'CurrencyBucket',
            bucket_name='currency-data-bucket-medium-article1',
            auto_delete_objects=True,
            removal_policy=core.RemovalPolicy.DESTROY
        )

        # this bucket will be used to store results of athena queries
        athena_queries_bucket: s3.Bucket = s3.Bucket(
            self,
            'AthenaQueriesBucket',
            bucket_name='athena-queries-bucket-currency-data-medium-article1',
            auto_delete_objects=True,
            removal_policy=core.RemovalPolicy.DESTROY
        )

        glue_database = glue.Database(self, 'GlueDb', database_name='currency')

        table = glue.Table(
            self,
            'GlueTable',
            table_name='currency_data',
            database=glue_database,
            data_format=glue.DataFormat.JSON,
            bucket=currency_bucket,
            columns=[
                glue.Column(name='target_currency', type=glue.Schema.STRING),
                glue.Column(name='USD', type=glue.Schema.DOUBLE),
                glue.Column(name='EUR', type=glue.Schema.DOUBLE),
                glue.Column(name='GBP', type=glue.Schema.DOUBLE)
            ],
            partition_keys=[
                glue.Column(name="year", type=glue.Schema.SMALL_INT),
                glue.Column(name="month", type=glue.Schema.SMALL_INT),
                glue.Column(name="day", type=glue.Schema.SMALL_INT)
            ],
        )

        cfn_table: glue_cfn.CfnTable = table.node.default_child
        cfn_table.add_property_override('TableInput.Parameters.projection\\.enabled', 'true')
        cfn_table.add_property_override('TableInput.Parameters.projection\\.year\\.type', 'injected')
        cfn_table.add_property_override('TableInput.Parameters.projection\\.month\\.type', 'injected')
        cfn_table.add_property_override('TableInput.Parameters.projection\\.day\\.type', 'injected')