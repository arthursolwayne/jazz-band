
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass - walking line in Fm (F, Ab, D, C, F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=3.0),  # C2
]

# Piano - open voicings, resolve on last chord
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25),  # C4
    pretty_midi.Note(velocity=100, pitch=83, start=1.5, end=2.25),  # E4
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=3.0),  # Ab4
]

# Sax - motif: F, Ab, G, C (hanging on C)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=80, start=1.875, end=2.25), # Ab4
    pretty_midi.Note(velocity=110, pitch=81, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=110, pitch=83, start=2.625, end=3.0),  # C4
]

# Add to their instruments
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass - walking line in Fm (F, Ab, D, C, F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=90, pitch=68, start=4.125, end=4.5),  # C2
]

# Piano - open voicings, resolve on last chord
piano_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab) (repeating from bar 2)
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=3.75),  # Ab4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=83, start=3.75, end=4.5),  # C4
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.5),  # Eb4
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.5),  # Bb4
]

# Sax - motif: F, Ab, G, C (finish it)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=80, start=3.375, end=3.75), # Ab4
    pretty_midi.Note(velocity=110, pitch=81, start=3.75, end=4.125), # G4
    pretty_midi.Note(velocity=110, pitch=83, start=4.125, end=4.5),  # C4
]

# Add to their instruments
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bass - walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0),  # C2
]

# Piano - open voicings, resolve on last chord
piano_notes = [
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=6.0),  # Bb4
]

# Sax - motif: F, Ab, G, C (rest on C)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=83, start=4.5, end=6.0),  # C4
]

# Add to their instruments
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_intro.mid")
