var cfg = { _id: 's1rs2',
  members: [
           { _id: 0, host: 'mongodb004:27018', priority:2 },
           { _id: 1, host: 'mongodb005:27018', priority:1 },
           { _id: 2, host: 'mongodb006:27018', arbiterOnly: true} ]};

var error = rs.initiate(cfg);
printjson(error);

