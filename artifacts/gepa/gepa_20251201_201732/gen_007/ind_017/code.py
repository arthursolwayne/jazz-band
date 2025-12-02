
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time in seconds per beat
tempo = 160  # BPM
beat_seconds = 60 / tempo
bar_seconds = beat_seconds * 4  # 4/4 time
bar_duration = bar_seconds

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)    # Bass
piano = pretty_midi.Instrument(program=0)    # Piano
sax = pretty_midi.Instrument(program=64)     # Tenor Sax

pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# --- BAR 1: Drums only (0.0 - 1.5 seconds)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# 1st beat (0.0 - 0.375)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=35, start=0.0, end=0.375))  # Kick
drums.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=0.0, end=0.375))  # Hihat

# 2nd beat (0.375 - 0.75)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75))  # Snare
drums.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=0.375, end=0.75))  # Hihat

# 3rd beat (0.75 - 1.125)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=35, start=0.75, end=1.125))  # Kick
drums.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=0.75, end=1.125))  # Hihat

# 4th beat (1.125 - 1.5)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))  # Snare
drums.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=1.125, end=1.5))  # Hihat

# --- BAR 2: Full ensemble starts
# Bass: Walking line (D2-G2, MIDI 38-43), walking line with chromatic approaches
# Bass notes (D2, F2#, G2, G#2, A2, Bb2, B2, C#3, D3, etc.)
# We'll use a simple Dm7 walking line: D - F - G - Bb

# Bass line starts at bar 2 (1.5s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # G#2
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last.
# Bar 2: Dm7 (D - F - Ab - C)
# Bar 3: Gm7 (G - Bb - D - F)
# Bar 4: C7 (C - E - G - Bb)
# We'll play each chord on 2nd and 4th beat

# Bar 2: Dm7 (D, F, Ab, C)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25))  # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.25))  # C

# Bar 3: Gm7 (G, Bb, D, F)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0))  # F

# Bar 4: C7 (C, E, G, Bb)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75))  # Bb

# Saxophone: Simple motif — D (D4), F (F4), G (G4), Bb (Bb4) — played on 1st and 3rd beats of bar 2
# Note: Play melody on beat 1 and 3 of bar 2 (1.5s and 2.25s)
# Motif: D4 (62), F4 (65), G4 (67), Bb4 (69)

# First note of motif at 1.5s (beat 1 of bar 2)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625))  # F4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375))   # G4

# Resolution on Bb4 at 3.75s (beat 4 of bar 4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125))  # Bb4

# Save the MIDI
pm.write("dante_intro.mid")

print("MIDI file saved as 'dante_intro.mid'")
