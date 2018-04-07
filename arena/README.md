# ARENA

## Interface

### 1. new_guest(user_id)

A new Player join arena, return room_id(str).

### 2. close_room(room_id)

close room whose id is room_id.

### 3. close()

close arena.

### 4. send_msg(room_id, data, cb)

send a msg to room whose id is room_id, then run function cb(def cb(data))