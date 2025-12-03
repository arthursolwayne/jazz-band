
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth, with a syncopated fill
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

# Add the drum notes to the drums instrument
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass (walking line with chromatic approaches)
bass_notes = [
    # Bar 2: Root (F2), chromatic approach above (G#2)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25), # G#2
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # F2
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),  # E2 (fifth of F7)
]

# Diane on piano (open voicings, each bar a different chord)
# Bar 2: F7 (C, E, F, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # C (C3)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # E (E3)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # A (A3)
]

# Dante on sax (motif, start it, leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=3.0),  # G
]

# Add the notes to their respective instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus on bass (walking line with chromatic approaches)
bass_notes = [
    # Bar 3: Root (F2), chromatic approach below (E#2)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # E#2
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),  # E2 (fifth of F7)
]

# Diane on piano (open voicings, each bar a different chord)
# Bar 3: Bb7 (F, A, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # Bb (Bb3)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # F (F3)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # A (A3)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D (D4)
]

# Dante on sax (motif, return and finish it)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),  # G
]

# Add the notes to their respective instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus on bass (walking line with chromatic approaches)
bass_notes = [
    # Bar 4: Root (F2), chromatic approach above (G#2)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=73, start=4.875, end=5.25), # G#2
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),  # E2 (fifth of F7)
]

# Diane on piano (open voicings, each bar a different chord)
# Bar 4: D7 (F, A, D, F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # D (D3)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # F (F3)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # A (A3)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F# (F#4)
]

# Dante on sax (motif variation, leave it unfinished)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0),  # G
]

# Add the notes to their respective instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
