import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    talker = launch_ros.actions.Node(
            package = 'mypkg2',
            node_executable = 'talker'
            )
    listener = launch_ros.actions.Node(
            package = 'mypkg2',
            node_executable = 'listener',
            output = 'screen'
            )

    return launch.LaunchDescription([talker,listener])
