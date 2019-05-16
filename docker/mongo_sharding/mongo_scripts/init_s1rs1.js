var cfg = { _id: 's1rs1',
  members: [
           { _id: 0, host: 'mongodb001:27018', priority:2 },
           { _id: 1, host: 'mongodb002:27018', priority:1 },
           { _id: 2, host: 'mongodb003:27018', arbiterOnly: true} ]};

var error = rs.initiate(cfg);
printjson(error);

