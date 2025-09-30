import pandas as pd
import numpy as np
from datetime import date, timedelta

# --- Configuration ---
N_USERS = 150
YEAR = 2024
ANOMALIES_PER_USER = 7
ARCHETYPES = ["Workaholic", "Night Owl", "Early Bird", "Balanced User"]

def generate_truly_clean_dataset():
    """Generates the full 'Routine Rhythms' dataset with built-in consistency, fixing the rounding bug."""
    
    all_data = []
    start_date = date(YEAR, 1, 1)
    end_date = date(YEAR, 12, 31)
    dates = [start_date + timedelta(days=d) for d in range((end_date - start_date).days + 1)]

    for user_id in range(N_USERS):
        user_archetype = np.random.choice(ARCHETYPES)
        anomaly_dates_indices = np.random.choice(len(dates), size=ANOMALIES_PER_USER, replace=False)
        anomaly_dates = [dates[i] for i in anomaly_dates_indices]

        for d in dates:
            is_weekend = d.weekday() >= 5
            is_anomaly = d in anomaly_dates
            
            screen_time, steps, unlocks, work_hrs, social_hrs, ent_hrs = 0, 0, 0, 0, 0, 0

            # --- RULES ENGINE (Same logic) ---
            if is_anomaly:
                if user_archetype == "Workaholic": work_hrs, social_hrs, ent_hrs, screen_time, steps, unlocks = 0.5, 5, 4, 9.5, 3000, 150
                elif user_archetype == "Night Owl": work_hrs, social_hrs, ent_hrs, screen_time, steps, unlocks = 2, 2, 1, 5, 12000, 60
                elif user_archetype == "Early Bird": work_hrs, social_hrs, ent_hrs, screen_time, steps, unlocks = 1, 3, 7, 11, 2000, 120
                else: work_hrs, social_hrs, ent_hrs, screen_time, steps, unlocks = 8, 0, 1, 9, 1000, 40
            else:
                if user_archetype == "Workaholic":
                    if is_weekend: work_hrs, social_hrs, ent_hrs, screen_time, steps, unlocks = 1, 3, 3.5, 7.5, 6000, 90
                    else: work_hrs, social_hrs, ent_hrs, screen_time, steps, unlocks = 6, 1, 1.5, 8.5, 4000, 70
                elif user_archetype == "Night Owl": work_hrs, social_hrs, ent_hrs, screen_time, steps, unlocks = 2, 4, 6, 12, 3000, 130
                elif user_archetype == "Early Bird": work_hrs, social_hrs, ent_hrs, screen_time, steps, unlocks = 3, 2.5, 2, 7.5, 10000, 80
                else:
                    if is_weekend: work_hrs, social_hrs, ent_hrs, screen_time, steps, unlocks = 1, 4, 3, 8, 8000, 110
                    else: work_hrs, social_hrs, ent_hrs, screen_time, steps, unlocks = 4, 2, 2, 8, 7000, 100
            
            final_screen_time = max(0, screen_time + np.random.normal(0, 1.5))
            noisy_work = max(0, work_hrs + np.random.normal(0, 0.8))
            noisy_social = max(0, social_hrs + np.random.normal(0, 0.8))
            noisy_ent = max(0, ent_hrs + np.random.normal(0, 0.8))
            total_app_hrs = noisy_work + noisy_social + noisy_ent
            
            if total_app_hrs > final_screen_time:
                if total_app_hrs > 0:
                    scaling_factor = final_screen_time / total_app_hrs
                    final_work, final_social, final_ent = noisy_work * scaling_factor, noisy_social * scaling_factor, noisy_ent * scaling_factor
                else:
                    final_work, final_social, final_ent = 0, 0, 0
            else:
                final_work, final_social, final_ent = noisy_work, noisy_social, noisy_ent
            
            row = {
                "user_id": user_id, "date": d, "weekday": d.strftime('%A'), "is_weekend": int(is_weekend),
                "screen_time_hrs": final_screen_time,
                "steps": int(max(0, steps + np.random.normal(0, 500))),
                "unlock_count": int(max(0, unlocks + np.random.normal(0, 10))),
                "work_app_hrs": final_work, "social_app_hrs": final_social, "ent_app_hrs": final_ent,
                "archetype_ground_truth": user_archetype, "is_anomaly_ground_truth": int(is_anomaly)
            }
            all_data.append(row)
            
    df = pd.DataFrame(all_data)
    # The rounding is removed to prevent the bug
    return df

# --- Generate and Verify the Truly Clean Dataset ---
df_truly_clean = generate_truly_clean_dataset()

# --- SAVE THE FINAL CSV (The missing line) ---
df_truly_clean.to_csv("routine_rhythms_2024_final_clean.csv", index=False)
print("Dataset saved to routine_rhythms_2024_final_clean.csv")

# --- Verification Step ---
df_truly_clean['total_app_hrs'] = df_truly_clean['work_app_hrs'] + df_truly_clean['social_app_hrs'] + df_truly_clean['ent_app_hrs']
impossible_days_count = df_truly_clean[df_truly_clean['total_app_hrs'] > df_truly_clean['screen_time_hrs'] + 0.0001].shape[0] # Add tolerance for tiny float issues

print(f"Verification: Found {impossible_days_count} impossible days in the final dataset. ✅")