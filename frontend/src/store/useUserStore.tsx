import { createContext, useContext, useState, ReactNode } from 'react';

interface UserState {
  name: string;
  ageGroup: '6-9' | '10-14' | '';
  focusArea: 'architecture' | 'logic' | '';
  points: number;
  level: number;
  streakDays: number;
  dailyLimitMinutes: number;
  usedMinutesToday: number;
}

interface UserContextType extends UserState {
  setName: (name: string) => void;
  setAgeGroup: (group: '6-9' | '10-14') => void;
  setFocusArea: (area: 'architecture' | 'logic') => void;
  addPoints: (amount: number) => void;
  incrementStreak: () => void;
  addUsedMinutes: (minutes: number) => void;
}

const defaultState: UserState = {
  name: '',
  ageGroup: '',
  focusArea: '',
  points: 1200,
  level: 5,
  streakDays: 14,
  dailyLimitMinutes: 60,
  usedMinutesToday: 42,
};

const UserContext = createContext<UserContextType | null>(null);

export function UserProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<UserState>(defaultState);

  const setName = (name: string) => setState(s => ({ ...s, name }));
  const setAgeGroup = (group: '6-9' | '10-14') => setState(s => ({ ...s, ageGroup: group }));
  const setFocusArea = (area: 'architecture' | 'logic') => setState(s => ({ ...s, focusArea: area }));
  const addPoints = (amount: number) => setState(s => ({ ...s, points: s.points + amount }));
  const incrementStreak = () => setState(s => ({ ...s, streakDays: s.streakDays + 1 }));
  const addUsedMinutes = (minutes: number) => setState(s => ({ ...s, usedMinutesToday: s.usedMinutesToday + minutes }));

  return (
    <UserContext.Provider value={{ ...state, setName, setAgeGroup, setFocusArea, addPoints, incrementStreak, addUsedMinutes }}>
      {children}
    </UserContext.Provider>
  );
}

export function useUser() {
  const ctx = useContext(UserContext);
  if (!ctx) throw new Error('useUser must be used within UserProvider');
  return ctx;
}