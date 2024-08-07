dag_name = "test_ex1"
dag_config = {
    "default_args": {"owner": "custom_owner", "start_date": "2019-09-01"},
    "description": "this is an example dag",
    "schedule_interval": "0 3 * * *",
    "tasks": {
        "task_1": {
            "operator": "airflow.operators.bash_operator.BashOperator",
            "bash_command": "echo 1",
        },
        "task_2": {
            "operator": "airflow.operators.bash_operator.BashOperator",
            "bash_command": "echo 2",
            "dependencies": ["task_1"],
        },
        "task_3": {
            "operator": "airflow.operators.bash_operator.BashOperator",
            "bash_command": "echo 3",
            "dependencies": ["task_1"],
        },
    },
}
