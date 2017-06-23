var cfg = { _id: 's0rs1',
  members: [
           { _id: 0, host: 'mongo004:27018', priority:2 },
           { _id: 1, host: 'mongo005:27018', priority:1 },
           { _id: 2, host: 'mongo006:27018', arbiterOnly: true} ]};

var error = rs.initiate(cfg);
printjson(error);

