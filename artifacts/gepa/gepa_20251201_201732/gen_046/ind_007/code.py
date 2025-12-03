
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F minor (F2, C2, G2, D2, etc.)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=75, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # C2
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # Eb2 (chromatic approach to D2)
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),  # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=83, start=1.5, end=1.875),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # C2
    pretty_midi.Note(velocity=90, pitch=73, start=3.75, end=4.125),  # Db2 (chromatic approach to D2)
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),  # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Bbm7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625),  # G2 (chromatic approach to Ab2)
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=6.0),  # Ab2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=4.875),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Complete the motif, resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=76, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=78, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=5.625, end=6.0),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
