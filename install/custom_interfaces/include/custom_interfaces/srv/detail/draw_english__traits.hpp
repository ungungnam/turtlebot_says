// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_interfaces:srv/DrawEnglish.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__DRAW_ENGLISH__TRAITS_HPP_
#define CUSTOM_INTERFACES__SRV__DETAIL__DRAW_ENGLISH__TRAITS_HPP_

#include "custom_interfaces/srv/detail/draw_english__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<custom_interfaces::srv::DrawEnglish_Request>()
{
  return "custom_interfaces::srv::DrawEnglish_Request";
}

template<>
inline const char * name<custom_interfaces::srv::DrawEnglish_Request>()
{
  return "custom_interfaces/srv/DrawEnglish_Request";
}

template<>
struct has_fixed_size<custom_interfaces::srv::DrawEnglish_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<custom_interfaces::srv::DrawEnglish_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<custom_interfaces::srv::DrawEnglish_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<custom_interfaces::srv::DrawEnglish_Response>()
{
  return "custom_interfaces::srv::DrawEnglish_Response";
}

template<>
inline const char * name<custom_interfaces::srv::DrawEnglish_Response>()
{
  return "custom_interfaces/srv/DrawEnglish_Response";
}

template<>
struct has_fixed_size<custom_interfaces::srv::DrawEnglish_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<custom_interfaces::srv::DrawEnglish_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<custom_interfaces::srv::DrawEnglish_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<custom_interfaces::srv::DrawEnglish>()
{
  return "custom_interfaces::srv::DrawEnglish";
}

template<>
inline const char * name<custom_interfaces::srv::DrawEnglish>()
{
  return "custom_interfaces/srv/DrawEnglish";
}

template<>
struct has_fixed_size<custom_interfaces::srv::DrawEnglish>
  : std::integral_constant<
    bool,
    has_fixed_size<custom_interfaces::srv::DrawEnglish_Request>::value &&
    has_fixed_size<custom_interfaces::srv::DrawEnglish_Response>::value
  >
{
};

template<>
struct has_bounded_size<custom_interfaces::srv::DrawEnglish>
  : std::integral_constant<
    bool,
    has_bounded_size<custom_interfaces::srv::DrawEnglish_Request>::value &&
    has_bounded_size<custom_interfaces::srv::DrawEnglish_Response>::value
  >
{
};

template<>
struct is_service<custom_interfaces::srv::DrawEnglish>
  : std::true_type
{
};

template<>
struct is_service_request<custom_interfaces::srv::DrawEnglish_Request>
  : std::true_type
{
};

template<>
struct is_service_response<custom_interfaces::srv::DrawEnglish_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__DRAW_ENGLISH__TRAITS_HPP_
