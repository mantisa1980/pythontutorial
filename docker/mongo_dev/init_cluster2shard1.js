var cfg = { _id: 'cluster2:shard1',
  members: [
           { _id: 0, host: 'mongo-004:27018', priority:2 },
           { _id: 1, host: 'mongo-005:27018', priority:1 },
           { _id: 2, host: 'mongo-006:27018', arbiterOnly: true} ]};

var error = rs.initiate(cfg);
printjson(error);

