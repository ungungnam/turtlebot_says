// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:srv/DrawEnglish.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__DRAW_ENGLISH__BUILDER_HPP_
#define CUSTOM_INTERFACES__SRV__DETAIL__DRAW_ENGLISH__BUILDER_HPP_

#include "custom_interfaces/srv/detail/draw_english__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_DrawEnglish_Request_line
{
public:
  Init_DrawEnglish_Request_line()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::srv::DrawEnglish_Request line(::custom_interfaces::srv::DrawEnglish_Request::_line_type arg)
  {
    msg_.line = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::DrawEnglish_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::DrawEnglish_Request>()
{
  return custom_interfaces::srv::builder::Init_DrawEnglish_Request_line();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_DrawEnglish_Response_success
{
public:
  Init_DrawEnglish_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::srv::DrawEnglish_Response success(::custom_interfaces::srv::DrawEnglish_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::DrawEnglish_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::DrawEnglish_Response>()
{
  return custom_interfaces::srv::builder::Init_DrawEnglish_Response_success();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__DRAW_ENGLISH__BUILDER_HPP_
