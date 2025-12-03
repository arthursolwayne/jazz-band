
import pretty_midi

# Initialize the MIDI file with the specified tempo
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

# Time signature: 4/4, 160 BPM => 0.375 seconds per beat
# 1 bar = 1.5 seconds

# Bar 1: Little Ray alone (0.0 - 1.5 seconds)
# Drums only
drum_notes = [
    (0.0, KICK),
    (0.375, HIHAT),
    (0.75, SNARE),
    (1.125, HIHAT),
    (1.5, KICK),
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(drum_note)

# Bar 2: Full ensemble (1.5 - 3.0 seconds)

# Bass line (Marcus): Walking line in Fm
# Root (F), 7th (Eb), 5th (C), b9 (Ab), etc. with chromatic approaches
bass_notes = [
    (1.5, 39),  # F2 (MIDI 39)
    (1.875, 41),  # Ab2 (chromatic approach)
    (2.25, 40),  # G2 (fifth)
    (2.625, 38),  # Eb2 (7th)
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano (Diane): Open voicings, each bar a different chord
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (1.5, 53),  # F4 (root)
    (1.5, 61),  # Ab4 (b3)
    (1.5, 60),  # C4 (5)
    (1.5, 62),  # Eb4 (7)
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    (2.25, 57),  # Bb4
    (2.25, 59),  # D4
    (2.25, 53),  # F4
    (2.25, 61),  # Ab4
])

# Bar 4: C7 (C, E, G, Bb)
piano_notes.extend([
    (3.0, 60),  # C4
    (3.0, 64),  # E4
    (3.0, 62),  # G4
    (3.0, 61),  # Bb4
])

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax (Dante): One short motif, haunting, sparse
# Motif: F4 - G4 - Eb4 - rest
sax_notes = [
    (1.5, 53),  # F4
    (1.875, 55),  # G4
    (2.25, 50),  # Eb4
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Bar 3: Drums continue (3.0 - 4.5 seconds)
drum_notes = [
    (3.0, KICK),
    (3.375, HIHAT),
    (3.75, SNARE),
    (4.125, HIHAT),
    (4.5, KICK),
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(drum_note)

# Bar 4: Drums continue (4.5 - 6.0 seconds)
drum_notes = [
    (4.5, KICK),
    (4.875, HIHAT),
    (5.25, SNARE),
    (5.625, HIHAT),
    (6.0, KICK),
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(drum_note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
