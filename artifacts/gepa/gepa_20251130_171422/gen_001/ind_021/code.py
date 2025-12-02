
import pretty_midi

# Create a Pretty MIDI object with 160 BPM (4/4 time)
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for the quartet
tenor_sax = pretty_midi.Instrument(program=64)  # Tenor saxophone
bass = pretty_midi.Instrument(program=33)       # Double bass
piano = pretty_midi.Instrument(program=0)       # Piano
drums = pretty_midi.Instrument(program=11)      # Drums

# Define time in seconds for each bar (160 BPM = 60/160 = 0.375 seconds per beat)
BAR_DURATION = 1.5
BEAT_DURATION = 0.375

# --- DRUMS: Little Ray (Bar 1 only) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0, 36, 100),      # Kick on beat 1
    (0.375, 42, 100),  # Snare on beat 2
    (0.75, 46, 100),   # Hihat on beat 3 (eighth note)
    (1.125, 46, 100),  # Hihat on beat 4 (eighth note)
    (1.5, 36, 100),    # Kick on beat 3 (end of bar)
]

for time, note, velocity in drum_notes:
    drum_note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

pm.instruments.append(drums)

# --- BASS: Marcus (Bars 1-4: walking line, chromatic approaches) ---
# Dm7 chord: D, F, A, C (root, b9, 11, 13)
# Walking bass line in D minor: D, C, Bb, A, G, F, Eb, D
# Slight chromatic approach on A -> G -> F

bass_notes = [
    (0, 62, 100, 0.375),  # D (root)
    (0.375, 60, 100, 0.375),  # C (chromatic)
    (0.75, 61, 100, 0.375),   # Bb (chromatic)
    (1.125, 62, 100, 0.375),  # A (chord tone)
    (1.5, 65, 100, 0.375),    # G (chromatic)
    (1.875, 58, 100, 0.375),  # F (chord tone)
    (2.25, 57, 100, 0.375),   # Eb (chromatic)
    (2.625, 62, 100, 0.375),  # D (root)
]

for time, pitch, velocity, duration in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

pm.instruments.append(bass)

# --- PIANO: Diane (Bars 2-4: comp on 2 and 4, 7th chords) ---
# Dm7: D, F, A, C (root, b9, 11, 13)
# Comp on 2 and 4: 2nd beat and 4th beat of each bar

# Bar 2: Dm7 on beat 2
# Bar 3: Dm7 on beat 2
# Bar 4: Dm7 on beat 2 and 4

# Dm7 = D, F, A, C
# 7th chord: root, minor 3rd, 11th, 13th

piano_notes = [
    # Bar 2 (1.5s) - Dm7 on beat 2 (1.5 + 0.375 = 1.875)
    (1.875, 62, 100, 0.375),  # D
    (1.875, 64, 100, 0.375),  # F
    (1.875, 69, 100, 0.375),  # A
    (1.875, 72, 100, 0.375),  # C

    # Bar 3 (3.0s) - Dm7 on beat 2 (3.0 + 0.375 = 3.375)
    (3.375, 62, 100, 0.375),  # D
    (3.375, 64, 100, 0.375),  # F
    (3.375, 69, 100, 0.375),  # A
    (3.375, 72, 100, 0.375),  # C

    # Bar 4 (4.5s) - Dm7 on beat 2 and 4
    (4.5 + 0.375, 62, 100, 0.375),  # D (beat 2)
    (4.5 + 0.375, 64, 100, 0.375),  # F
    (4.5 + 0.375, 69, 100, 0.375),  # A
    (4.5 + 0.375, 72, 100, 0.375),  # C

    (4.5 + 1.125, 62, 100, 0.375),  # D (beat 4)
    (4.5 + 1.125, 64, 100, 0.375),  # F
    (4.5 + 1.125, 69, 100, 0.375),  # A
    (4.5 + 1.125, 72, 100, 0.375),  # C
]

for time, pitch, velocity, duration in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

pm.instruments.append(piano)

# --- TENOR SAX: Dante (Bars 2-4: melody, concise, memorable, unique twist) ---
# Motif: D (62), A (69), Eb (66), G (67) — then repeat, but hold on the last note
# This is a simple question: D -> A -> Eb -> G — it's blue, it's chromatic, it's a little dark

# Bar 2 (1.5s) - start the motif
# Bar 3 (3.0s) - repeat the motif
# Bar 4 (4.5s) - repeat the motif, but end on the last note (G)

sax_notes = [
    # Bar 2
    (1.5, 62, 100, 0.375),  # D
    (1.875, 69, 100, 0.375),  # A
    (2.25, 66, 100, 0.375),   # Eb
    (2.625, 67, 100, 0.375),  # G

    # Bar 3
    (3.0, 62, 100, 0.375),  # D
    (3.375, 69, 100, 0.375),  # A
    (3.75, 66, 100, 0.375),   # Eb
    (4.125, 67, 100, 0.375),  # G

    # Bar 4
    (4.5, 62, 100, 0.375),  # D
    (4.875, 69, 100, 0.375),  # A
    (5.25, 66, 100, 0.375),   # Eb
    (5.625, 67, 100, 1.0),    # G (hold for 1 second, ending at 6.625)
]

for time, pitch, velocity, duration in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    tenor_sax.notes.append(note)

pm.instruments.append(tenor_sax)

# Save the MIDI file
pm.write("dante_intro.mid")
