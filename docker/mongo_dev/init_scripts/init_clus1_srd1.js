var cfg = { _id: 'clus1:srd1',
  members: [
           { _id: 0, host: 'pig-mongo-001-test:27018', priority:2 },
           { _id: 1, host: 'pig-mongo-002-test:27018', priority:1 },
           { _id: 2, host: 'pig-mongo-003-test:27018', arbiterOnly: true} ]};

var error = rs.initiate(cfg);
printjson(error);

