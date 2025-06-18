cmake_minimum_required(VERSION 3.8)
project(pubsub)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(pubsub REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Num.msg"
  "msg/Sphere.msg"
  "srv/Addthreeints.srv"
  "action/Fib.action"
  DEPENDENCIES geometry_msgs
)

ament_export_dependencies(rosidl_default_runtime)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

install(PROGRAMS
  nodes/pub_python.py
  nodes/sub_python.py
  nodes/serv_python.py
  nodes/client_python.py
  nodes/msg_nodes/num_pub.py
  nodes/msg_nodes/num_sub.py
  nodes/msg_nodes/sphere_pub.py
  nodes/msg_nodes/sphere_sub.py
  nodes/srv_nodes/addthree_server.py
  nodes/srv_nodes/addthree_client.py
  nodes/action_nodes/action_server.py
  nodes/action_nodes/action_client.py
  
  DESTINATION lib/${PROJECT_NAME}
)


ament_package()
