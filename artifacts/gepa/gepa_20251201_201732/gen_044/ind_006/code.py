
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root) with chromatic approach on 2
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.125),  # E (chromatic)
    pretty_midi.Note(velocity=90, pitch=71, start=2.125, end=2.5),  # F# (fifth)
    pretty_midi.Note(velocity=90, pitch=70, start=2.5, end=2.875),  # F (root)
]

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # E
]

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # B
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # B
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 3: Gm7 (root G, fifth D) with chromatic approach on 2
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.625),  # F# (chromatic)
    pretty_midi.Note(velocity=90, pitch=73, start=3.625, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.375),  # G
]

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: Gm7
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.5),  # D#
]

# Sax: Continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=72, start=3.25, end=3.5),  # D#
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),  # D#
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 4: C7 (root C, fifth G) with chromatic approach on 2
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.125),  # B (chromatic)
    pretty_midi.Note(velocity=90, pitch=77, start=5.125, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=5.5, end=5.875),  # C
]

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: C7
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=5.0),  # B
]

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=110, pitch=75, start=4.75, end=5.0),  # C#
    pretty_midi.Note(velocity=110, pitch=74, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=75, start=5.25, end=5.5),  # C#
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
