
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMidi(initial_tempo=160)

# Define the time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key signature (F major)
pm.key_signature_changes = [pretty_midi.KeySignature(0, 0)]  # F major

# Define the time in seconds for 4 bars at 160 BPM (4/4)
# 160 BPM = 60 / 160 = 0.375 seconds per beat
# 4 bars = 16 beats = 6 seconds
BAR_DURATION = 1.5  # seconds per bar
TOTAL_DURATION = 6.0  # seconds total for 4 bars

# Helper function to convert beat to seconds
def beat_to_time(beat):
    return beat * 0.375

# Helper to add a note
def add_note(instrument, note_number, start_time, duration, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start_time, end=start_time + duration)
    instrument.notes.append(note)

# Create instruments
sax_instrument = pretty_midi.Instrument(program=64)  # Tenor Sax
bass_instrument = pretty_midi.Instrument(program=33)  # Acoustic Bass
piano_instrument = pretty_midi.Instrument(program=0)  # Acoustic Piano
drums_instrument = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

pm.instruments = [sax_instrument, bass_instrument, piano_instrument, drums_instrument]

# --- BAR 1: Little Ray (Drums) - Mysterious, sparse, sets the mood ---
# Kick on 1 and 3, snare on 2 and 4
# Hihat on every 8th, with variation in velocity

# Bar 1: 0.0 - 1.5 sec
kick_notes = [pretty_midi.PrettyMIDI.note_number_to_name(36, is_cents=False),  # F2
              pretty_midi.PrettyMIDI.note_number_to_name(36, is_cents=False)]  # F2
snare_notes = [pretty_midi.PrettyMIDI.note_number_to_name(64, is_cents=False),  # Snare
               pretty_midi.PrettyMIDI.note_number_to_name(64, is_cents=False)]  # Snare
hihat_notes = [pretty_midi.PrettyMIDI.note_number_to_name(42, is_cents=False) for _ in range(8)]  # Hihat

# Drums: Kick on 1 & 3 (0.0, 0.75)
add_note(drums_instrument, 36, 0.0, 0.1, 90)
add_note(drums_instrument, 36, 0.75, 0.1, 90)

# Snare on 2 & 4 (0.375, 1.125)
add_note(drums_instrument, 64, 0.375, 0.1, 85)
add_note(drums_instrument, 64, 1.125, 0.1, 85)

# Hihat on every 8th
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
for i, time in enumerate(hihat_times):
    # Some variation in velocity
    vel = 90 if i % 2 == 0 else 80
    add_note(drums_instrument, 42, time, 0.05, vel)

# --- BAR 2: Everyone enters, sax begins melodic motif ---

# Bass: Walking line in F major (F, G, A, Bb)
bass_notes = [71, 72, 73, 74]  # F, G, A, Bb
for i, note in enumerate(bass_notes):
    add_note(bass_instrument, note, beat_to_time(i + 4), 0.375, 95)

# Piano: 7th chords on 2 and 4
# F7: F, A, C, E
# Bb7: Bb, D, F, Ab
# Chord on beat 2 (0.75)
add_note(piano_instrument, 71, 0.75, 0.25, 90)
add_note(piano_instrument, 74, 0.75, 0.25, 90)
add_note(piano_instrument, 76, 0.75, 0.25, 90)
add_note(piano_instrument, 79, 0.75, 0.25, 90)

# Chord on beat 4 (1.125)
add_note(piano_instrument, 70, 1.125, 0.25, 90)
add_note(piano_instrument, 73, 1.125, 0.25, 90)
add_note(piano_instrument, 76, 1.125, 0.25, 90)
add_note(piano_instrument, 78, 1.125, 0.25, 90)

# Saxophone: Melodic motif (sparse, yearning)
# F (71) on beat 1, rest on beat 2, E (72) on beat 3, rest on beat 4
add_note(sax_instrument, 71, 0.0, 0.375, 92)
add_note(sax_instrument, 72, 0.75, 0.375, 92)

# --- BAR 3: Tension builds, sax motif returns with slight variation ---

# Bass: Chromatic walk (F, G, G#, A)
add_note(bass_instrument, 71, 1.5, 0.375, 95)
add_note(bass_instrument, 72, 1.875, 0.375, 95)
add_note(bass_instrument, 73, 2.25, 0.375, 95)
add_note(bass_instrument, 74, 2.625, 0.375, 95)

# Piano: 7th chords on 2 and 4 (A7, D7)
# A7: A, C#, E, G
# D7: D, F#, A, C
add_note(piano_instrument, 74, 1.875, 0.25, 90)
add_note(piano_instrument, 77, 1.875, 0.25, 90)
add_note(piano_instrument, 79, 1.875, 0.25, 90)
add_note(piano_instrument, 81, 1.875, 0.25, 90)

add_note(piano_instrument, 72, 2.625, 0.25, 90)
add_note(piano_instrument, 76, 2.625, 0.25, 90)
add_note(piano_instrument, 74, 2.625, 0.25, 90)
add_note(piano_instrument, 77, 2.625, 0.25, 90)

# Saxophone: Repeat motif, but with more tension
add_note(sax_instrument, 71, 1.5, 0.375, 92)
add_note(sax_instrument, 72, 1.875, 0.375, 92)

# --- BAR 4: Lingering question, sax resolves slightly, but not fully ---

# Bass: Walking in G minor (chromatic)
add_note(bass_instrument, 72, 3.0, 0.375, 95)
add_note(bass_instrument, 73, 3.375, 0.375, 95)
add_note(bass_instrument, 74, 3.75, 0.375, 95)
add_note(bass_instrument, 75, 4.125, 0.375, 95)

# Piano: Dissonant 7th chord on 4 (Gm7: G, Bb, D, F)
add_note(piano_instrument, 76, 4.125, 0.25, 90)
add_note(piano_instrument, 78, 4.125, 0.25, 90)
add_note(piano_instrument, 71, 4.125, 0.25, 90)
add_note(piano_instrument, 73, 4.125, 0.25, 90)

# Saxophone: Resolves to E (72) on beat 4, hanging on
add_note(sax_instrument, 72, 3.75, 0.375, 92)

# Drums: Final bar, kick on 1 and 3, snare on 2 and 4, hihat on every 8th
add_note(drums_instrument, 36, 3.0, 0.1, 90)
add_note(drums_instrument, 36, 3.75, 0.1, 90)
add_note(drums_instrument, 64, 3.375, 0.1, 85)
add_note(drums_instrument, 64, 4.125, 0.1, 85)

hihat_times = [3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]
for i, time in enumerate(hihat_times):
    vel = 90 if i % 2 == 0 else 80
    add_note(drums_instrument, 42, time, 0.05, vel)

# Save the MIDI file
pm.write("dante_intro.mid")
