#include "set_speed_manager/set_speed_manager.hpp"
#include <algorithm>

SetSpeedManager::SetSpeedManager()
: set_speed_(0), min_speed_(0), max_speed_(0)
{
}

int SetSpeedManager::getSpeed() const
{
  return set_speed_;
}

void SetSpeedManager::setSpeed(int speed)
{
  set_speed_ = std::clamp(speed, min_speed_, max_speed_);
}

void SetSpeedManager::increment()
{
  setSpeed(set_speed_ + 5);
}

void SetSpeedManager::decrement()
{
  setSpeed(set_speed_ - 5);
}
