
import pretty_midi

# Create the MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Assign drum note numbers
kick = 36  # Kick drum
snare = 38  # Snare drum
hihat = 42  # Hi-hat

# BAR 1: Little Ray on drums (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth note

# Bar 1 length in seconds: 1.5s
bar_length = 1.5

# 160 BPM = 160 beats per minute => 2.5 beats per second
# 1 beat = 0.375 seconds
beat = 0.375

# Eighth note = 0.1875 seconds

# Drums in bar 1
# Kick on beats 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125))

# Snare on beats 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5))

# Hihat on every eighth note
for i in range(8):
    start = i * 0.1875
    end = start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start, end=end))

# BAR 2: Full group in (1.5 - 3.0s)
# Diane (piano) plays open voicings, different chord each bar
# Let's use F7, Bb7, Cm7, and D7 (simple but harmonically rich, Wayne would notice)

# Bar 2: F7 (F, A, C, E)
# Diane plays an F7 chord with open voicings, on beat 2 and 4

diane_chord_1 = [pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.5 + beat/2),  # F (E4)
                 pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.5 + beat/2),  # A (A4)
                 pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.5 + beat/2),  # C (C5)
                 pretty_midi.Note(velocity=100, pitch=91, start=1.5, end=1.5 + beat/2)]  # E (E5)
piano.notes.extend(diane_chord_1)

# Bar 2: Cm7 chord (C, Eb, G, Bb) on beat 2 and 4
diane_chord_2 = [pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.25 + beat/2),  # C (C4)
                 pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.25 + beat/2),  # Eb (Eb4)
                 pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.25 + beat/2),  # G (G4)
                 pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.25 + beat/2)]  # Bb (Bb4)
piano.notes.extend(diane_chord_2)

# Marcus (bass) plays a walking line: F, G, A, Bb, C, D, Eb, F (roots and fifths, chromatic approaches)
# Bar 2: F, G, A, Bb
bass_notes = [78, 80, 82, 81]  # F (F3), G (G3), A (A3), Bb (Bb3)
for i, note in enumerate(bass_notes):
    start = 1.5 + i * beat / 2
    end = start + beat / 2
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# BAR 3: Full group in (3.0 - 4.5s)
# Diane: Bb7 chord (Bb, D, F, Ab) on beat 2 and 4
diane_chord_3 = [pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + beat/2),  # Bb (Bb4)
                 pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.0 + beat/2),  # D (D4)
                 pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.0 + beat/2),  # F (F4)
                 pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.0 + beat/2)]  # Ab (Ab3)
piano.notes.extend(diane_chord_3)

# Bar 3: D7 chord (D, F#, A, C) on beat 2 and 4
diane_chord_4 = [pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.75 + beat/2),  # D (D4)
                 pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.75 + beat/2),  # F# (F#4)
                 pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.75 + beat/2),  # A (A4)
                 pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.75 + beat/2)]  # C (C4)
piano.notes.extend(diane_chord_4)

# Marcus: A, Bb, C, D (walking line)
bass_notes = [82, 81, 78, 80]  # A (A3), Bb (Bb3), C (C3), D (D3)
for i, note in enumerate(bass_notes):
    start = 3.0 + i * beat / 2
    end = start + beat / 2
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# BAR 4: Full group in (4.5 - 6.0s)
# Diane: Cm7 chord (C, Eb, G, Bb) on beat 2 and 4

diane_chord_5 = [pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.5 + beat/2),  # C (C4)
                 pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.5 + beat/2),  # Eb (Eb4)
                 pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.5 + beat/2),  # G (G4)
                 pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.5 + beat/2)]  # Bb (Bb4)
piano.notes.extend(diane_chord_5)

# Marcus: D, Eb, F, G (walking line)
bass_notes = [80, 79, 78, 81]  # D (D3), Eb (Eb3), F (F3), G (G3)
for i, note in enumerate(bass_notes):
    start = 4.5 + i * beat / 2
    end = start + beat / 2
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Dante (sax): 4-bar motif — open, melodic, haunting, in F
# F, G, A, Bb, C, D, Eb, F — but not scales, just a motif with space

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=81, start=1.5, end=1.5 + beat),  # Bb (Bb4)
    pretty_midi.Note(velocity=110, pitch=82, start=1.5 + beat, end=1.5 + 2*beat),  # A (A4) — wait
    pretty_midi.Note(velocity=110, pitch=84, start=1.5 + 2*beat, end=1.5 + 3*beat),  # C (C5)
    pretty_midi.Note(velocity=110, pitch=86, start=1.5 + 3*beat, end=1.5 + 4*beat),  # D (D5)
    pretty_midi.Note(velocity=110, pitch=81, start=1.5 + 4*beat, end=1.5 + 5*beat),  # Bb (Bb4)
    pretty_midi.Note(velocity=110, pitch=82, start=1.5 + 5*beat, end=1.5 + 6*beat),  # A (A4)
    pretty_midi.Note(velocity=110, pitch=84, start=1.5 + 6*beat, end=1.5 + 7*beat),  # C (C5)
    pretty_midi.Note(velocity=110, pitch=86, start=1.5 + 7*beat, end=6.0)             # D (D5)
]

sax.notes.extend(sax_notes)

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
