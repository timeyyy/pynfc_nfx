cmake_minimum_required (VERSION 2.8)
project (some_project)

include_directories (
    #~ "${PROJECT_SOURCE_DIR}/intfs"
    #~ "${PROJECT_SOURCE_DIR}/types"
    #~ "${PROJECT_SOURCE_DIR}/comps/phpalSli15693/src/Sw"
    "${PROJECT_SOURCE_DIR}/NxpRdLib_PublicRelease/intfs"
    "${PROJECT_SOURCE_DIR}/NxpRdLib_PublicRelease/types"
    "${PROJECT_SOURCE_DIR}/NxpRdLib_PublicRelease/comps/phpalSli15693/src/Sw"
)

set(EXT_LIBS  pthread  m)

add_definitions(-g -O0)

#~ list(APPEND SOURCE "${PROJECT_SOURCE_DIR}/../polling.c")	# This is simply main.c from nfc card polling demo
#~ source_group(src "${PROJECT_SOURCE_DIR}/../polling.c")

list(APPEND SOURCE "${PROJECT_SOURCE_DIR}/main.c")
source_group(src "${PROJECT_SOURCE_DIR}/main.c")


#~ file(GLOB_RECURSE SOURCE_TMP "${PROJECT_SOURCE_DIR}/*.c" )

file(GLOB_RECURSE SOURCE_TMP "${PROJECT_SOURCE_DIR}/NxpRdLib_PublicRelease/*.c" )


list(APPEND SOURCE ${SOURCE_TMP})

#add_library(${PROJECT_NAME} ${SOURCE})					#This was added by nxppy dude

	
add_executable(${PROJECT_NAME} ${SOURCE})
target_link_libraries(${PROJECT_NAME} ${EXT_LIBS})
