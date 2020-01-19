cmake_minimum_required(VERSION 3.7)
project(calibration)

set(CMAKE_CXX_STANDARD 11)
set(SOURCE_FILES calibration.cpp)

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

set(BOOST_REQUIRED_MODULES system filesystem thread date_time iostreams)
find_package(Boost 1.30.1 REQUIRED COMPONENTS ${BOOST_REQUIRED_MODULES})
include_directories(SYSTEM ${Boost_INCLUDE_DIRS})

add_executable( calibration calibration.cpp )
target_link_libraries( calibration 
                       ${OpenCV_LIBS} 
                       Boost::system 
                       Boost::filesystem
                       Boost::thread
                       Boost::date_time
                       Boost::iostreams)
