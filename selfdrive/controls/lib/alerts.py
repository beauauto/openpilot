from cereal import car, log

# Priority
class Priority:
  LOWEST = 0
  LOW_LOWEST = 1
  LOW = 2
  MID = 3
  HIGH = 4
  HIGHEST = 5

AlertSize = log.Live100Data.AlertSize
AlertStatus = log.Live100Data.AlertStatus
AudibleAlert = car.CarControl.HUDControl.AudibleAlert
VisualAlert = car.CarControl.HUDControl.VisualAlert

class Alert(object):
  def __init__(self,
               alert_type,
               alert_text_1,
               alert_text_2,
               alert_status,
               alert_size,
               alert_priority,
               visual_alert,
               audible_alert,
               duration_sound,
               duration_hud_alert,
               duration_text,
               alert_rate=0.):

    self.alert_type = alert_type
    self.alert_text_1 = alert_text_1
    self.alert_text_2 = alert_text_2
    self.alert_status = alert_status
    self.alert_size = alert_size
    self.alert_priority = alert_priority
    self.visual_alert = visual_alert
    self.audible_alert = audible_alert

    self.duration_sound = duration_sound
    self.duration_hud_alert = duration_hud_alert
    self.duration_text = duration_text

    self.start_time = 0.
    self.alert_rate = alert_rate

    # typecheck that enums are valid on startup
    tst = car.CarControl.new_message()
    tst.hudControl.visualAlert = self.visual_alert

  def __str__(self):
    return self.alert_text_1 + "/" + self.alert_text_2 + " " + str(self.alert_priority) + "  " + str(
      self.visual_alert) + " " + str(self.audible_alert)

  def __gt__(self, alert2):
    return self.alert_priority > alert2.alert_priority


ALERTS = [
  # Miscellaneous alerts
  Alert(
      "enable",
      "",
      "",
      AlertStatus.normal, AlertSize.none,
      Priority.MID, VisualAlert.none, AudibleAlert.chimeEngage, .2, 0., 0.),

  Alert(
      "disable",
      "",
      "",
      AlertStatus.normal, AlertSize.none,
      Priority.MID, VisualAlert.none, AudibleAlert.chimeDisengage, .2, 0., 0.),

  Alert(
      "fcw",
      "刹车!",
      "有撞车危险",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.fcw, AudibleAlert.chimeWarningRepeat, 1., 2., 2.),

  Alert(
      "steerSaturated",
      "需要人工控制",
      "转向扭矩超过限制",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.chimePrompt, 1., 2., 3.),

  Alert(
      "steerTempUnavailable",
      "需要人工控制",
      "转向暂时不可用",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.chimeWarning1, .4, 2., 3.),

  Alert(
      "steerTempUnavailableMute",
      "需要人工控制",
      "转向暂时不可用",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .2, .2, .2),

  Alert(
      "preDriverDistracted",
      "请看着前方道路：您看起来分心了",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.none, .0, .1, .1, alert_rate=0.75),

  Alert(
      "promptDriverDistracted",
      "请看着前方道路",
      "您看起来分心了",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, .1, .1),

  Alert(
      "driverDistracted",
      "立即解除自动驾驶",
      "用户分心了",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGH, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, .1, .1),

  Alert(
      "preDriverUnresponsive",
      "触摸方向盘：无驾驶员监控",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.none, .0, .1, .1, alert_rate=0.75),

  Alert(
      "promptDriverUnresponsive",
      "触摸方向盘",
      "用户没反应",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, .1, .1),

  Alert(
      "driverUnresponsive",
      "立即解除自动驾驶",
      "用户没反应",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGH, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, .1, .1),

  Alert(
      "driverMonitorOff",
      "驾驶员监控器无法使用",
      "准确度低",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .4, 0., 4.),

  Alert(
      "driverMonitorOn",
      "驾驶员监控器可以使用",
      "准确度高",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .4, 0., 4.),

  Alert(
      "geofence",
      "需要解除自动驾驶",
      "不在地理围栏区域",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.HIGH, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, .1, .1),

  Alert(
      "startup",
      "随时准备好接管驾驶",
      "始终把手放在方向盘上，眼睛注视前方道路",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., 15.),

  Alert(
      "ethicalDilemma",
      "立即恢复人工驾驶",
      "发现道德难题",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 3.),

  Alert(
      "steerTempUnavailableNoEntry",
      "自动驾驶不可用",
      "暂时无法控制方向盘",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "manualRestart",
      "恢复人工驾驶",
      "恢复人工驾驶",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "resumeRequired",
      "车停了",
      "按继续键启动",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "belowSteerSpeed",
      "立即恢复人工驾驶",
      "速度太低方向控制不可用 ",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning1, 0., 0., .1),

  Alert(
      "debugAlert",
      "调试警报",
      "",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .1, .1, .1),

  # Non-entry only alerts
  Alert(
      "wrongCarModeNoEntry",
      "自动驾驶不可用",
      "主开关关闭",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "dataNeededNoEntry",
      "自动驾驶不可用",
      "校准需要数据。上传驾驶记录，再试一次",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "outOfSpaceNoEntry",
      "自动驾驶不可用",
      "存储空间用尽",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "pedalPressedNoEntry",
      "自动驾驶不可用",
      "在尝试期间踩了油门",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, "brakePressed", AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "speedTooLowNoEntry",
      "自动驾驶不可用",
      "速度太低",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "brakeHoldNoEntry",
      "自动驾驶不可用",
      "还在使用刹车",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "parkBrakeNoEntry",
      "自动驾驶不可用",
      "还在使用手刹",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "lowSpeedLockoutNoEntry",
      "自动驾驶不可用",
      "巡航出错：从新启动",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "lowBatteryNoEntry",
      "自动驾驶不可用",
      "电池快耗尽",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  # Cancellation alerts causing soft disabling
  Alert(
      "overheat",
      "立即恢复人工驾驶",
      "系统过热",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "wrongGear",
      "立即恢复人工驾驶",
      "不是D挡",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "calibrationInvalid",
      "立即恢复人工驾驶",
      "校对无效: 调整EON位置并从新校对",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "calibrationIncomplete",
      "立即恢复人工驾驶",
      "校对在进行中",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "doorOpen",
      "立即恢复人工驾驶",
      "车门打开了",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "seatbeltNotLatched",
      "立即恢复人工驾驶",
      "没系安全带",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "espDisabled",
      "立即恢复人工驾驶",
      "ESP关闭",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "lowBattery",
      "立即恢复人工驾驶",
      "电池快耗尽",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  # Cancellation alerts causing immediate disabling
  Alert(
      "radarCommIssue",
      "立即恢复人工驾驶",
      "雷达出错：从新启动汽车",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "radarFault",
      "立即恢复人工驾驶",
      "雷达出错：从新启动汽车",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "modelCommIssue",
      "立即恢复人工驾驶",
      "模型出错：检查互联网链接",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "controlsFailed",
      "立即恢复人工驾驶",
      "控制失败",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "controlsMismatch",
      "立即恢复人工驾驶",
      "控制不匹配",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "commIssue",
      "立即恢复人工驾驶",
      "CAN总线出错：检查连接",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "steerUnavailable",
      "立即恢复人工驾驶",
      "车道保持出错：从新启动汽车",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "brakeUnavailable",
      "立即恢复人工驾驶",
      "巡航出错：从新启动汽车",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "gasUnavailable",
      "立即恢复人工驾驶",
      "油门出错：从新启动汽车",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "reverseGear",
      "立即恢复人工驾驶",
      "倒车挡",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "cruiseDisabled",
      "立即恢复人工驾驶",
      "巡航关闭",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "plannerError",
      "立即恢复人工驾驶",
      "计划解决方案错误",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  # not loud cancellations (user is in control)
  Alert(
      "noTarget",
      "自动驾驶取消了",
      "没有先导车",
      AlertStatus.normal, AlertSize.mid,
      Priority.HIGH, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "speedTooLow",
      "自动驾驶取消了",
      "速度太低",
      AlertStatus.normal, AlertSize.mid,
      Priority.HIGH, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "invalidGiraffeHonda",
      "无效线束连接器配置",
      "博奥控制用0111，原车控制用1011",
      AlertStatus.normal, AlertSize.mid,
      Priority.HIGH, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  # Cancellation alerts causing non-entry
  Alert(
      "overheatNoEntry",
      "自动驾驶不可用",
      "系统过热",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "wrongGearNoEntry",
      "自动驾驶不可用",
      "不在D挡",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "calibrationInvalidNoEntry",
      "自动驾驶不可用",
      "校对无效: 调整EON位置并从新校对",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "calibrationIncompleteNoEntry",
      "自动驾驶不可用",
      "校对正在进行中",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "doorOpenNoEntry",
      "自动驾驶不可用",
      "车门打开了",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "seatbeltNotLatchedNoEntry",
      "自动驾驶不可用",
      "没系安全带",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "espDisabledNoEntry",
      "自动驾驶不可用",
      "ESP关闭了",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "geofenceNoEntry",
      "自动驾驶不可用",
      "不在地理围栏区域",
      AlertStatus.normal, AlertSize.mid,
      Priority.MID, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "radarCommIssueNoEntry",
      "自动驾驶不可用",
      "雷达出错：从新启动汽车",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "radarFaultNoEntry",
      "自动驾驶不可用",
      "雷达出错：从新启动汽车",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "modelCommIssueNoEntry",
      "自动驾驶不可用",
      "模型出错：检查互联网链接",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "controlsFailedNoEntry",
      "自动驾驶不可用",
      "控制失败",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "commIssueNoEntry",
      "自动驾驶不可用",
      "CAN总线出错：检查连接",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "steerUnavailableNoEntry",
      "自动驾驶不可用",
      "车道保持出错：从新启动汽车",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "brakeUnavailableNoEntry",
      "自动驾驶不可用",
      "巡航出错：从新启动汽车",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "gasUnavailableNoEntry",
      "自动驾驶不可用",
      "油门出错：从新启动汽车",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "reverseGearNoEntry",
      "自动驾驶不可用",
      "在倒车挡",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "cruiseDisabledNoEntry",
      "自动驾驶不可用",
      "巡航已关闭",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "noTargetNoEntry",
      "自动驾驶不可用",
      "无先导车",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "plannerErrorNoEntry",
      "自动驾驶不可用",
      "计划解决方案出错",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "invalidGiraffeHondaNoEntry",
      "无效线束连接器配置",
      "博奥控制用0111，原车控制用1011",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  # permanent alerts
  Alert(
      "steerUnavailablePermanent",
      "车道保持出错：从新启动汽车",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "brakeUnavailablePermanent",
      "巡航出错：从新启动汽车",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "lowSpeedLockoutPermanent",
      "巡航出错：从新启动汽车",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "calibrationIncompletePermanent",
      "正在校准: ",
      "提速到 ",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "invalidGiraffeHondaPermanent",
      "无效线束连接器配置",
      "博奥控制用0111，原车控制用1011",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),
]
