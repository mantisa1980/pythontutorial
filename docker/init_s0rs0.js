var cfg = { _id: 's0rs0',
  members: [
           { _id: 0, host: 'mongo001:27018', priority:2 },
           { _id: 1, host: 'mongo002:27018', priority:1 },
           { _id: 2, host: 'mongo003:27018', arbiterOnly: true} ]};

var error = rs.initiate(cfg);
printjson(error);

