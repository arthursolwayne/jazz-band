
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
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.25),
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
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: Different chord each bar, resolve on the last
# Bar 3: Cm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # A
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: Different chord each bar, resolve on the last
# Bar 4: G7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, bring it back to F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=95, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=95, pitch=38, start=4.125, end=4.5),   # Snare on 4
]
# Hihat on every eighth
for i in range(3.0, 4.5, 0.375):
    pretty_midi.Note(velocity=80, pitch=42, start=i, end=i + 0.375)
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=95, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=95, pitch=38, start=5.625, end=6.0),   # Snare on 4
]
# Hihat on every eighth
for i in range(4.5, 6.0, 0.375):
    pretty_midi.Note(velocity=80, pitch=42, start=i, end=i + 0.375)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
