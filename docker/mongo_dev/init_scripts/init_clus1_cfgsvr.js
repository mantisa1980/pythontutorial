var cfg = { _id: 'clus1cfg', // this should match the --replSet parameter
            configsvr: true,
            members: [
              { _id: 0, host: 'mongo-clus1-cfgsvr1:27019', priority:2 },
              { _id: 1, host: 'mongo-clus1-cfgsvr2:27019', priority:1 },
              { _id: 2, host: 'mongo-clus1-cfgsvr3:27019', priority:1 } ]};

var error = rs.initiate(cfg);
printjson(error);

