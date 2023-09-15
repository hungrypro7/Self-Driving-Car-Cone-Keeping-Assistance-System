// Generated by gencpp from file ublox_msgs/UpdSOS.msg
// DO NOT EDIT!


#ifndef UBLOX_MSGS_MESSAGE_UPDSOS_H
#define UBLOX_MSGS_MESSAGE_UPDSOS_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ublox_msgs
{
template <class ContainerAllocator>
struct UpdSOS_
{
  typedef UpdSOS_<ContainerAllocator> Type;

  UpdSOS_()
    : cmd(0)
    , reserved1()  {
      reserved1.assign(0);
  }
  UpdSOS_(const ContainerAllocator& _alloc)
    : cmd(0)
    , reserved1()  {
  (void)_alloc;
      reserved1.assign(0);
  }



   typedef uint8_t _cmd_type;
  _cmd_type cmd;

   typedef boost::array<uint8_t, 3>  _reserved1_type;
  _reserved1_type reserved1;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(CLASS_ID)
  #undef CLASS_ID
#endif
#if defined(_WIN32) && defined(MESSAGE_ID)
  #undef MESSAGE_ID
#endif
#if defined(_WIN32) && defined(CMD_FLASH_BACKUP_CREATE)
  #undef CMD_FLASH_BACKUP_CREATE
#endif
#if defined(_WIN32) && defined(CMD_FLASH_BACKUP_CLEAR)
  #undef CMD_FLASH_BACKUP_CLEAR
#endif

  enum {
    CLASS_ID = 9u,
    MESSAGE_ID = 20u,
    CMD_FLASH_BACKUP_CREATE = 0u,
    CMD_FLASH_BACKUP_CLEAR = 1u,
  };


  typedef boost::shared_ptr< ::ublox_msgs::UpdSOS_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ublox_msgs::UpdSOS_<ContainerAllocator> const> ConstPtr;

}; // struct UpdSOS_

typedef ::ublox_msgs::UpdSOS_<std::allocator<void> > UpdSOS;

typedef boost::shared_ptr< ::ublox_msgs::UpdSOS > UpdSOSPtr;
typedef boost::shared_ptr< ::ublox_msgs::UpdSOS const> UpdSOSConstPtr;

// constants requiring out of line definition

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ublox_msgs::UpdSOS_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ublox_msgs::UpdSOS_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ublox_msgs::UpdSOS_<ContainerAllocator1> & lhs, const ::ublox_msgs::UpdSOS_<ContainerAllocator2> & rhs)
{
  return lhs.cmd == rhs.cmd &&
    lhs.reserved1 == rhs.reserved1;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ublox_msgs::UpdSOS_<ContainerAllocator1> & lhs, const ::ublox_msgs::UpdSOS_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ublox_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ublox_msgs::UpdSOS_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ublox_msgs::UpdSOS_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ublox_msgs::UpdSOS_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ublox_msgs::UpdSOS_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ublox_msgs::UpdSOS_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ublox_msgs::UpdSOS_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ublox_msgs::UpdSOS_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fdc2e32dbb00126a932ae76a6222eec4";
  }

  static const char* value(const ::ublox_msgs::UpdSOS_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xfdc2e32dbb00126aULL;
  static const uint64_t static_value2 = 0x932ae76a6222eec4ULL;
};

template<class ContainerAllocator>
struct DataType< ::ublox_msgs::UpdSOS_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ublox_msgs/UpdSOS";
  }

  static const char* value(const ::ublox_msgs::UpdSOS_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ublox_msgs::UpdSOS_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# UPD-SOS (0x09 0x14)\n"
"#\n"
"# Firmware Supported on:\n"
"# u-blox 8 / u-blox M8 from protocol version 15 up to version 23.01\n"
"#\n"
"\n"
"uint8 CLASS_ID = 9\n"
"uint8 MESSAGE_ID = 20\n"
"\n"
"uint8 cmd                   # Command\n"
"# The host can send this message in order to save part of the BBR memory in a \n"
"# file in flash file system. The feature is designed in order to emulate the \n"
"# presence of the backup battery even if it is not present; the host can issue \n"
"# the save on shutdown command before switching off the device supply. It is \n"
"# recommended to issue a GNSS stop command before, in order to keep the BBR \n"
"# memory content consistent.\n"
"uint8 CMD_FLASH_BACKUP_CREATE = 0    # Create Backup File in Flash\n"
"# The host can send this message in order to erase the backup file present in \n"
"# flash. It is recommended that the clear operation is issued after the host has \n"
"# received the notification that the memory has been restored after a reset. \n"
"# Alternatively the host can parse the startup string 'Restored data saved on \n"
"# shutdown' or poll the UBX-UPD-SOS message for getting the status.\n"
"uint8 CMD_FLASH_BACKUP_CLEAR = 1     # Clear Backup File in Flash\n"
"\n"
"uint8[3] reserved1          # Reserved\n"
;
  }

  static const char* value(const ::ublox_msgs::UpdSOS_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ublox_msgs::UpdSOS_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.cmd);
      stream.next(m.reserved1);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct UpdSOS_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ublox_msgs::UpdSOS_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ublox_msgs::UpdSOS_<ContainerAllocator>& v)
  {
    s << indent << "cmd: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.cmd);
    s << indent << "reserved1[]" << std::endl;
    for (size_t i = 0; i < v.reserved1.size(); ++i)
    {
      s << indent << "  reserved1[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.reserved1[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // UBLOX_MSGS_MESSAGE_UPDSOS_H
