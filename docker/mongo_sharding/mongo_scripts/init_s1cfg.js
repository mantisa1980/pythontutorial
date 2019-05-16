var cfg = { _id: 's1cfg',
  members: [
           { _id: 0, host: 'mongocfg001:27019', priority:2 },
           { _id: 1, host: 'mongocfg002:27019', priority:1 },
           { _id: 2, host: 'mongocfg003:27019', priority:1 } ]};

var error = rs.initiate(cfg);
printjson(error);

