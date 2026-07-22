#ifndef SET_SPEED_MANAGER_HPP
#define SET_SPEED_MANAGER_HPP

class SetSpeedManager
{
public:
  SetSpeedManager();

  int getSpeed() const;
  void setSpeed(int speed);
  void increment();
  void decrement();

private:
  int set_speed_;
  int min_speed_;
  int max_speed_;
};

#endif
