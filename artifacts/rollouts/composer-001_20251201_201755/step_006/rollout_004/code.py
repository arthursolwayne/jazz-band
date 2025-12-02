
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=110, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=110, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F#5
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # A5
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),   # F#5
]
sax.notes.extend(sax_notes)

# Bass line (D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=43, start=1.5, end=1.75),  # G2
    pretty_midi.Note(velocity=70, pitch=42, start=1.75, end=2.0),   # D2
    pretty_midi.Note(velocity=70, pitch=41, start=2.0, end=2.25),   # C2 (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=43, start=2.25, end=2.5),   # G2
]
bass.notes.extend(bass_notes)

# Piano comp (open voicings, resolve on the last bar)
# Bar 2: Dmaj7
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=2.0),  # D5
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.0),  # A5
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=2.0),  # D6
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=2.0),  # F#5
]
# Bar 3: G7
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.5),  # G5
    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.5),  # C6
    pretty_midi.Note(velocity=80, pitch=76, start=2.0, end=2.5),  # G6
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.5),  # B5
])
# Bar 4: Cmaj7
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=3.0),  # C5
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=3.0),  # F#5
    pretty_midi.Note(velocity=80, pitch=72, start=2.5, end=3.0),  # C6
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=3.0),  # A5
])
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody (repeat and resolve)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),  # F#5
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # A5
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5),   # F#5
]
sax.notes.extend(sax_notes)

# Bass line (D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=43, start=3.0, end=3.25),  # G2
    pretty_midi.Note(velocity=70, pitch=42, start=3.25, end=3.5),   # D2
    pretty_midi.Note(velocity=70, pitch=41, start=3.5, end=3.75),   # C2 (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=43, start=3.75, end=4.0),   # G2
]
bass.notes.extend(bass_notes)

# Piano comp
# Bar 3: G7
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.5),  # G5
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.5),  # C6
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.5),  # G6
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.5),  # B5
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody (resolve)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=4.625, end=4.75),  # F#5
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # A5
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),   # B5 (resolve)
]
sax.notes.extend(sax_notes)

# Bass line (D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=43, start=4.5, end=4.75),  # G2
    pretty_midi.Note(velocity=70, pitch=42, start=4.75, end=5.0),   # D2
]
bass.notes.extend(bass_notes)

# Piano comp
# Bar 4: Cmaj7
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=5.0),  # C5
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=5.0),  # F#5
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=5.0),  # C6
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=5.0),  # A5
]
piano.notes.extend(piano_notes)

# Drums for bar 3 and 4
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=110, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
