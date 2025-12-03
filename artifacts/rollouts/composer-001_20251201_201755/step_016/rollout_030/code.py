
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in (1.5 - 3.0s)

# Marcus: Walking line in Fm (F, Ab, D, Gb, etc.)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=80, pitch=56, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=80, pitch=54, start=2.625, end=3.0), # Gb2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, resolve on the last bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25), # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25), # Ab4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.25), # C5
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=2.25), # D5
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=3.0), # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=3.0), # D5
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0), # F4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0), # Ab4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Melody in Fm (G, Ab, F, Eb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875), # G4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # Ab4
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625), # F4
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0), # Eb4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Everyone in (3.0 - 4.5s)

# Marcus: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.375), # Bb2
    pretty_midi.Note(velocity=80, pitch=56, start=3.375, end=3.75), # D2
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=80, pitch=51, start=4.125, end=4.5), # Ab2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, resolve on the last bar
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75), # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.75), # D5
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75), # F4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75), # Ab4
]

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.5), # C5
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.5), # Eb4
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.5), # G5
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.5), # Bb4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Repeat the motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # Ab4
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125), # F4
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5), # Eb4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Everyone in (4.5 - 6.0s)

# Marcus: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875), # C3
    pretty_midi.Note(velocity=80, pitch=61, start=4.875, end=5.25), # Eb3
    pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=5.625), # G3
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0), # C3
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, resolve on the last bar
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=5.25), # C5
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=5.25), # Eb4
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=5.25), # G5
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25), # Bb4
]

# Bar 4: End on Cm7
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=6.0), # C5
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=6.0), # Eb4
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=6.0), # G5
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=6.0), # Bb4
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
