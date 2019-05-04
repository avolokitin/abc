import os
import struct

LOG_FILE_PATH = os.path.join(os.getcwd(), 'txnlog.dat')
UID = 2456938384156277127


class Header:
  """Transaction Header

  Header format: 
    4 bytes - magic string
    1 byte - version
    4 bytes - number of records
  """
  @classmethod
  def from_file(cls, fd):
    magic_string = fd.read(4)
    version = fd.read(1)
    records = fd.read(4)
    return cls(magic_string, version, records)

  def __init__(self, magic_str, version, num_records):
    self.magic_str = magic_str.decode()
    self.version = ord(version)
    self.num_records = struct.unpack('!I', num_records)[0]
  
  def __repr__(self):
    return '{} {} {}'.format(self.magic_str, self.version, self.num_records)


class Record:
  """Transaction Record

  Record format: 
    1 byte - type
    4 bytes - unix time stamp
    8 bytes - user id
    8 bytes - amount in dollars
  """
  @classmethod
  def from_file(cls, fd):
    rtype = ord(fd.read(1))
    time_stamp = fd.read(4)
    uid = fd.read(8)
    if rtype == 0 or rtype == 1:
      amount = fd.read(8)
    else:
      amount = None
    return cls(rtype, time_stamp, uid, amount)

  def __init__(self, rtype, time_stamp, uid, amount):
    self.rtype = rtype
    self.time_stamp = struct.unpack('!I', time_stamp)[0]
    self.uid = struct.unpack('!Q', uid)[0]
    if amount:
      self.amount = struct.unpack('!d', amount)[0]
    else:
      self.amount = amount
  
  def __repr__(self):
    return '{} {} {} {}'.format(self.rtype, self.time_stamp, self.uid, self.amount)

header = None
records = []
with open(LOG_FILE_PATH, 'rb') as fd:
  header = Header.from_file(fd)
  for _ in range(header.num_records):
    records.append(Record.from_file(fd))


total_debit = 0
total_credit = 0
started_auto_pays = 0
ended_auto_pays = 0
uid_balance = 0

for record in records:
  # debit
  if record.rtype == 0:
    total_debit += record.amount
    if record.uid == UID:
      uid_balance -= record.amount
  # credit 
  elif record.rtype == 1:
    total_credit += record.amount
    if record.uid == UID:
      uid_balance += record.amount
  # autopay
  elif record.rtype == 2:
    started_auto_pays += 1
  # ended autopay 
  elif record.rtype == 3:
    ended_auto_pays += 1

print(uid_balance, total_debit, total_credit, started_auto_pays, ended_auto_pays)

