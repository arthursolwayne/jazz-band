
import pretty_midi

# Initialize the MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Syncopated, tight, with tension and release

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=95, pitch=snare, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=95, pitch=snare, start=1.875, end=2.0))

# Hihat on every eighth note
for i in range(0, 4):
    hihat_start = i * 0.375
    hihat_end = hihat_start + 0.1
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=hihat_start, end=hihat_end))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line in F minor (F, G, Ab, A, Bb, B, C, Db)
# Chromatic approach on the 3rd beat of bar 2

# Bar 2
bass_notes = [
    (1.5, 70, 57),  # F (C4)
    (1.875, 75, 58),  # G (D4)
    (2.25, 70, 60),  # Ab (Eb4)
    (2.625, 75, 61),  # A (F4)
    (3.0, 70, 62),  # Bb (Gb4)
    (3.375, 75, 64),  # B (G4)
    (3.75, 70, 65),  # C (Ab4)
    (4.125, 75, 66)   # Db (Bb4)
]
for start, vel, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.375))

# Bar 3
bass_notes = [
    (4.5, 70, 66),  # Db (Bb4)
    (4.875, 75, 65),  # C (Ab4)
    (5.25, 70, 64),  # B (G4)
    (5.625, 75, 62),  # Bb (Gb4)
    (6.0, 70, 61),  # A (F4)
    (6.375, 75, 60),  # Ab (Eb4)
    (6.75, 70, 58),  # G (D4)
    (7.125, 75, 57)   # F (C4)
]
for start, vel, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.375))

# Piano: Diane, 7th chords, comp on 2 and 4. Sharp and emotional.

# Bar 2
piano_notes = [
    (1.875, 100, 69),  # A (E4) - F7 (F, A, C, Eb)
    (1.875, 100, 65),  # C (G3)
    (1.875, 100, 62),  # Eb (D3)
    (1.875, 95, 61),   # Bb (Db3)
    (2.625, 100, 69),  # A
    (2.625, 100, 65),  # C
    (2.625, 100, 62),  # Eb
    (2.625, 95, 61)    # Bb
]
for start, vel, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.125))

# Bar 3
piano_notes = [
    (5.25, 100, 69),  # A
    (5.25, 100, 65),  # C
    (5.25, 100, 62),  # Eb
    (5.25, 95, 61),   # Bb
    (6.0, 100, 69),   # A
    (6.0, 100, 65),   # C
    (6.0, 100, 62),   # Eb
    (6.0, 95, 61)     # Bb
]
for start, vel, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.125))

# Saxophone: Dante, haunting, simple motif. Start it, leave it hanging.

# Bar 2: Start the motif
sax_notes = [
    (1.5, 110, 66),  # F# (F#4)
    (1.75, 90, 64),  # E (E4)
    (2.0, 110, 67),  # G (G4)
    (2.25, 90, 65),  # F (F4)
    (2.5, 110, 68),  # A (A4)
]
for start, vel, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25))

# Bar 3: Return to complete the motif
sax_notes = [
    (3.0, 110, 66),  # F#
    (3.25, 90, 64),  # E
    (3.5, 110, 67),  # G
    (3.75, 90, 65),  # F
    (4.0, 110, 68),  # A
]
for start, vel, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25))

# Bar 4: Finish the motif with a resolution
sax_notes = [
    (4.5, 110, 65),  # F (F4) - resolution to F minor
    (4.75, 90, 63),  # D (D4)
    (5.0, 110, 66),  # F#
    (5.25, 90, 64),  # E
    (5.5, 110, 68),  # A
]
for start, vel, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_introduction.mid")
