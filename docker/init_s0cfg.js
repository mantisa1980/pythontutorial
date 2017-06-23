var cfg = { _id: 's0cfg',
  members: [
           { _id: 0, host: 'mongo007:27019', priority:2 },
           { _id: 1, host: 'mongo008:27019', priority:1 },
           { _id: 2, host: 'mongo009:27019', priority:1 } ]};

var error = rs.initiate(cfg);
printjson(error);

