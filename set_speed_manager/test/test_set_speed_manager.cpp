#include <gtest/gtest.h>
#include "set_speed_manager/set_speed_manager.hpp"

TEST(SetSpeedManagerTest, InitialSpeedIsZero)
{
    SetSpeedManager manager;
    EXPECT_EQ(manager.getSpeed(), 0);
}
