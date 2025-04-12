# RUN
Before you run Docker, you should prepare database on your machine.

```
$ flask db init
$ flask db migrate
$ flask db upgrade
```

## exex
```
docker-compose up
```

# error
## case 1
if you face build error you update permission like this.
```
 > [frontend build-stage 6/6] RUN npm run build:
0.146
0.146 > front-sample@0.0.0 build
0.146 > vue-tsc -b && vite build
0.146
0.148 sh: 1: vue-tsc: Permission denied
------
failed to solve: process "/bin/sh -c npm run build" did not complete successfully: exit code: 127
```

## how to fix of case 1
```
$ chmod 755 frontend/node_modules/vue-tsc/bin/vue-tsc.js
chmod: Invalid file mode: 755
```

