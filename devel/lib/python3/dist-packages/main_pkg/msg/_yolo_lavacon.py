# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from main_pkg/yolo_lavacon.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class yolo_lavacon(genpy.Message):
  _md5sum = "da269e966072bed82c14a04982ff80e5"
  _type = "main_pkg/yolo_lavacon"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float64 yolo_mid_X
float64 yolo_mid_y
string yolo_con_name
string yolo_con_color
"""
  __slots__ = ['yolo_mid_X','yolo_mid_y','yolo_con_name','yolo_con_color']
  _slot_types = ['float64','float64','string','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       yolo_mid_X,yolo_mid_y,yolo_con_name,yolo_con_color

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(yolo_lavacon, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.yolo_mid_X is None:
        self.yolo_mid_X = 0.
      if self.yolo_mid_y is None:
        self.yolo_mid_y = 0.
      if self.yolo_con_name is None:
        self.yolo_con_name = ''
      if self.yolo_con_color is None:
        self.yolo_con_color = ''
    else:
      self.yolo_mid_X = 0.
      self.yolo_mid_y = 0.
      self.yolo_con_name = ''
      self.yolo_con_color = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2d().pack(_x.yolo_mid_X, _x.yolo_mid_y))
      _x = self.yolo_con_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.yolo_con_color
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.yolo_mid_X, _x.yolo_mid_y,) = _get_struct_2d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.yolo_con_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.yolo_con_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.yolo_con_color = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.yolo_con_color = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2d().pack(_x.yolo_mid_X, _x.yolo_mid_y))
      _x = self.yolo_con_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.yolo_con_color
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.yolo_mid_X, _x.yolo_mid_y,) = _get_struct_2d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.yolo_con_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.yolo_con_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.yolo_con_color = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.yolo_con_color = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2d = None
def _get_struct_2d():
    global _struct_2d
    if _struct_2d is None:
        _struct_2d = struct.Struct("<2d")
    return _struct_2d
