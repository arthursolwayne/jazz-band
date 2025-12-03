
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Key: F major
pm.key_signature_changes = [pretty_midi.KeySignature(key_number=1, time=0.0)]  # F major

# Define instrument programs
# Tenor Sax = 64
# Acoustic Bass = 33
# Electric Piano = 10
# Drums = 0

# Add instruments
tenor_sax = pretty_midi.Instrument(program=64, is_drum=False)
bass = pretty_midi.Instrument(program=33, is_drum=False)
piano = pretty_midi.Instrument(program=10, is_drum=False)
drums = pretty_midi.Instrument(program=0, is_drum=True)

pm.instruments = [tenor_sax, bass, piano, drums]

# Define tempo: 160 BPM
# 60 seconds = 160 beats => 1 beat = 0.375 seconds
# 1 bar = 4 beats => 1.5 seconds per bar

# Define the time for each bar (in seconds)
bar_duration = 1.5
bar_1_end = bar_duration
bar_2_end = bar_1_end + bar_duration
bar_3_end = bar_2_end + bar_duration
bar_4_end = bar_3_end + bar_duration

# ------------------------------- DRUMS (Little Ray) -------------------------------
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: Start with a subtle groove, not too aggressive

# Define the 8th note positions (0.0, 0.375, 0.75, 1.125, 1.5)
bar_1_kicks = [0.0, 0.75]
bar_1_snare = [0.375, 1.125]
bar_1_hihat = [0.0, 0.375, 0.75, 1.125, 1.5]

for time in bar_1_kicks:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

for time in bar_1_snare:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

for time in bar_1_hihat:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

# Bar 2-4: Full energy, kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    bar_start = (bar - 1) * bar_duration
    bar_kicks = [bar_start + 0.0, bar_start + 0.75]
    bar_snare = [bar_start + 0.375, bar_start + 1.125]
    bar_hihat = [bar_start + t for t in [0.0, 0.375, 0.75, 1.125, 1.5]]

    for time in bar_kicks:
        note = pretty_midi.Note(velocity=110, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)

    for time in bar_snare:
        note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)

    for time in bar_hihat:
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(note)

# ------------------------------- BASS (Marcus) -------------------------------
# Walking bass line (roots and fifths with chromatic approaches)
# F major key: F, Gm, Am, Bb, C, Dm, Em, F
# Bar 1: F -> G -> Ab -> A -> F (chromatic approach up to G)
# Bar 2: Gm -> C -> D -> Eb -> G (chromatic approach down to C)
# Bar 3: Am -> D -> E -> F -> A (chromatic approach up to D)
# Bar 4: Bb -> Eb -> F -> G -> Bb (chromatic approach down to Eb)
# All notes in bass range (D2 to G2, MIDI 38 to 43)

# Bar 1: F (38), G (39), Ab (40), A (41), F (38)
times = [0.0, 0.5, 1.0, 1.5, 2.0]
pitches = [38, 39, 40, 41, 38]
for t, p in zip(times, pitches):
    note = pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.25)
    bass.notes.append(note)

# Bar 2: G (39), C (40), D (42), Eb (43), G (39)
times = [2.5, 3.0, 3.5, 4.0, 4.5]
pitches = [39, 40, 42, 43, 39]
for t, p in zip(times, pitches):
    note = pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.25)
    bass.notes.append(note)

# Bar 3: A (41), D (42), E (44), F (45), A (41)
times = [5.0, 5.5, 6.0, 6.5, 7.0]
pitches = [41, 42, 44, 45, 41]
for t, p in zip(times, pitches):
    note = pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.25)
    bass.notes.append(note)

# Bar 4: Bb (42), Eb (45), F (45), G (47), Bb (42)
times = [7.5, 8.0, 8.5, 9.0, 9.5]
pitches = [42, 45, 45, 47, 42]
for t, p in zip(times, pitches):
    note = pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.25)
    bass.notes.append(note)

# ------------------------------- PIANO (Diane) -------------------------------
# Open voicings, different chord each bar, resolve on the last
# Bar 1: Fmaj7 (F, A, C, E)
# Bar 2: Gm7 (G, Bb, D, F)
# Bar 3: Am7 (A, C, E, G)
# Bar 4: Bb7 (Bb, D, F, Ab)

# Bar 1: Fmaj7 (F, A, C, E) - open voicing, high register
# Play on beats 2 and 4 (0.375 and 1.125)
for t in [0.375, 1.125]:
    note = pretty_midi.Note(velocity=100, pitch=79, start=t, end=t + 0.1)  # E5
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=77, start=t, end=t + 0.1)  # C5
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=74, start=t, end=t + 0.1)  # A4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=72, start=t, end=t + 0.1)  # F4
    piano.notes.append(note)

# Bar 2: Gm7 (G, Bb, D, F) - open voicing, high register
for t in [2.375, 3.125]:
    note = pretty_midi.Note(velocity=100, pitch=80, start=t, end=t + 0.1)  # F5
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=77, start=t, end=t + 0.1)  # D5
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=73, start=t, end=t + 0.1)  # Bb4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=72, start=t, end=t + 0.1)  # G4
    piano.notes.append(note)

# Bar 3: Am7 (A, C, E, G) - open voicing, high register
for t in [4.375, 5.125]:
    note = pretty_midi.Note(velocity=100, pitch=81, start=t, end=t + 0.1)  # G5
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=80, start=t, end=t + 0.1)  # E5
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=77, start=t, end=t + 0.1)  # C5
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=74, start=t, end=t + 0.1)  # A4
    piano.notes.append(note)

# Bar 4: Bb7 (Bb, D, F, Ab) - open voicing, high register
for t in [6.375, 7.125]:
    note = pretty_midi.Note(velocity=100, pitch=82, start=t, end=t + 0.1)  # Ab5
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=80, start=t, end=t + 0.1)  # F5
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=77, start=t, end=t + 0.1)  # D5
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=71, start=t, end=t + 0.1)  # Bb4
    piano.notes.append(note)

# ------------------------------- TENOR SAX (You) -------------------------------
# Melodic idea: short motif, start on F, move to A, C, leave it hanging

# Bar 1: Start the motif at 0.0
note = pretty_midi.Note(velocity=110, pitch=72, start=0.0, end=0.5)  # F5
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=0.5, end=1.0)  # A5
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=79, start=1.0, end=1.5)  # C6
tenor_sax.notes.append(note)

# Bar 2: Resolution of the motif, then leave it hanging
note = pretty_midi.Note(velocity=110, pitch=76, start=2.0, end=2.5)  # A5
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=72, start=2.5, end=3.0)  # F5
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.5)  # A5
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=79, start=3.5, end=4.0)  # C6
tenor_sax.notes.append(note)

# Bar 3: A slight variation, fragmentation
note = pretty_midi.Note(velocity=110, pitch=76, start=4.0, end=4.5)  # A5
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=5.0)  # F5
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=5.0, end=5.5)  # A5
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=79, start=5.5, end=6.0)  # C6
tenor_sax.notes.append(note)

# Bar 4: Resolution, complete the idea but leave space
note = pretty_midi.Note(velocity=110, pitch=76, start=6.0, end=6.5)  # A5
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=72, start=6.5, end=7.0)  # F5
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=76, start=7.0, end=7.5)  # A5
tenor_sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=79, start=7.5, end=8.0)  # C6
tenor_sax.notes.append(note)

# Save the MIDI file
pm.write("dante_russo_intro.mid")
