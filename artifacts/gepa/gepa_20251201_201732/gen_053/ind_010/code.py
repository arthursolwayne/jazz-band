
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hi-hat
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # Bb2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # C3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolving each bar
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # E5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody (F, G, Ab, Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25), # G4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # Ab4
    pretty_midi.Note(velocity=110, pitch=68, start=2.625, end=3.0),  # Bb4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hi-hat
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75), # D3
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125), # Eb3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # Bb2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolving each bar
piano_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # F5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # Ab5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody (Bb, C, D, Eb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=110, pitch=70, start=3.375, end=3.75), # C5
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125), # D5
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5),  # Eb5
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hi-hat
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # C3
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.625), # D3
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),  # Eb3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolving each bar
piano_notes = [
    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # C5
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0),  # Eb5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody (F, G, Ab, Bb) — returns to start
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25), # G4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # Ab4
    pretty_midi.Note(velocity=110, pitch=68, start=5.625, end=6.0),  # Bb4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hi-hat
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
