
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625),  # G (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=2.875),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.875, end=3.0),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125),  # D (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif with variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.375),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=4.375, end=4.5),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625),  # G (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: D7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F#
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=5.875),  # G
    pretty_midi.Note(velocity=110, pitch=68, start=5.875, end=6.0),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_shot.mid")
