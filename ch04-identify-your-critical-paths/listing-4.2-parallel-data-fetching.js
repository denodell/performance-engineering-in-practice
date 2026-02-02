const [user, preferences, notifications] = await Promise.all([
  fetchUser(id),
  fetchPreferences(id),
  fetchNotifications(id)
]);
