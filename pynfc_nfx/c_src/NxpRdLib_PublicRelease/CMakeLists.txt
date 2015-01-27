cmake_minimum_required (VERSION 2.8)
project (nxprd)

include_directories (
    "${PROJECT_SOURCE_DIR}/intfs"
    "${PROJECT_SOURCE_DIR}/types"
    "${PROJECT_SOURCE_DIR}/comps/phpalSli15693/src/Sw"
)

set(EXT_LIBS  pthread  m)

add_definitions(-g -O0)

list(APPEND SOURCE "${PROJECT_SOURCE_DIR}/../polling.c")	# This is simply main.c from nfc card polling demo
source_group(src "${PROJECT_SOURCE_DIR}/../polling.c")

file(GLOB_RECURSE SOURCE_TMP "${PROJECT_SOURCE_DIR}/*.c" )
list(APPEND SOURCE ${SOURCE_TMP})

#~ add_library(${PROJECT_NAME} ${SOURCE})					This was added by nxppy dude


add_executable(${PROJECT_NAME} ${SOURCE})
target_link_libraries(${PROJECT_NAME} ${EXT_LIBS})
