cmake_minimum_required(VERSION 3.8)
project(set_speed_manager)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_library(set_speed_manager
  src/set_speed_manager.cpp
)

target_include_directories(set_speed_manager PUBLIC
  include
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)

  find_package(ament_cmake_gtest REQUIRED)

  ament_add_gtest(test_set_speed_manager
    test/test_set_speed_manager.cpp
  )

  target_link_libraries(test_set_speed_manager
    set_speed_manager
  )
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
