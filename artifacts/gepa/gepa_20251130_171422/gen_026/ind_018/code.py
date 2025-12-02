
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Drums alone (0.0 - 1.5s)
# Build tension with subtle dynamics, space, and texture.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (KICK, 0.0, 0.5, 0.8),   # Kick on 1
    (HIHAT, 0.0, 0.5, 0.4),  # Hihat on 1
    (HIHAT, 0.25, 0.25, 0.4), # Hihat on &1
    (SNARE, 0.5, 0.5, 0.8),  # Snare on 2
    (HIHAT, 0.5, 0.5, 0.4),  # Hihat on 2
    (HIHAT, 0.75, 0.25, 0.4), # Hihat on &2
    (KICK, 1.0, 0.5, 0.8),   # Kick on 3
    (HIHAT, 1.0, 0.5, 0.4),  # Hihat on 3
    (HIHAT, 1.25, 0.25, 0.4), # Hihat on &3
    (SNARE, 1.5, 0.5, 0.8),  # Snare on 4
    (HIHAT, 1.5, 0.5, 0.4),  # Hihat on 4
    (HIHAT, 1.75, 0.25, 0.4) # Hihat on &4
]

for note_number, start, duration, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 2-4: Full Quartet (1.5 - 6.0s)
# Dm key, 4/4 time

# Saxophone motif: concise, emotional, memorable
# Dm7 -> Bb -> G -> C -> A -> Dm7 (approximate, in D minor)
# Notes in Dm (D, F, Ab, Bb, C, Eb, G, etc.)
# This motif is 6 notes, with a slight resolution back to Dm7
sax_notes = [
    (62, 1.5, 0.375, 100),    # D (Dm7 root)
    (60, 1.875, 0.375, 90),   # Bb (tension)
    (65, 2.25, 0.375, 95),    # G (melodic line)
    (67, 2.625, 0.375, 100),  # C (strong note, resolution)
    (64, 2.999, 0.375, 90),   # A (sigh)
    (62, 3.375, 0.375, 100),  # D (back to Dm7)
    (62, 3.75, 0.375, 100),   # D (hold, emotional)
    (60, 4.125, 0.375, 90),   # Bb (tension again)
    (65, 4.5, 0.375, 95),     # G (melodic line)
    (67, 4.875, 0.375, 100),  # C (end with resolution)
    (64, 5.25, 0.375, 90),    # A (sigh)
    (62, 5.625, 0.375, 100)   # D (final resolution)
]

for pitch, start, duration, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Bass line: chromatic approaches, active and melodic
# Dm in bass, walking line with chromatic approach
bass_notes = [
    (62, 1.5, 0.375, 70),     # D (Dm7 root)
    (63, 1.875, 0.375, 70),   # Eb (chromatic approach)
    (60, 2.25, 0.375, 75),    # Bb (tension)
    (62, 2.625, 0.375, 75),   # D
    (67, 2.999, 0.375, 80),   # C (resolution)
    (64, 3.375, 0.375, 75),   # A (melodic)
    (62, 3.75, 0.375, 75),    # D
    (60, 4.125, 0.375, 75),   # Bb
    (67, 4.5, 0.375, 80),     # C
    (64, 4.875, 0.375, 75),   # A
    (62, 5.25, 0.375, 75),    # D
    (60, 5.625, 0.375, 75)    # Bb
]

for pitch, start, duration, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4, emotional
# Dm7 (D, F, Ab, C) on 1 and 3
# Bb7 (Bb, D, F, Ab) on 2 and 4
piano_notes = [
    (62, 1.5, 0.375, 80),     # D (Dm7)
    (65, 1.5, 0.375, 80),     # F
    (69, 1.5, 0.375, 80),     # Ab
    (67, 1.5, 0.375, 80),     # C
    (60, 2.25, 0.375, 80),    # Bb (Bb7)
    (65, 2.25, 0.375, 80),    # D
    (69, 2.25, 0.375, 80),    # F
    (67, 2.25, 0.375, 80),    # Ab
    (62, 3.0, 0.375, 80),     # D (Dm7)
    (65, 3.0, 0.375, 80),     # F
    (69, 3.0, 0.375, 80),     # Ab
    (67, 3.0, 0.375, 80),     # C
    (60, 3.75, 0.375, 80),    # Bb (Bb7)
    (65, 3.75, 0.375, 80),    # D
    (69, 3.75, 0.375, 80),    # F
    (67, 3.75, 0.375, 80)     # Ab
]

for pitch, start, duration, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
