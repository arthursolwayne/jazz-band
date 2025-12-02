
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Sax enters with motif
# F7 - G7 - A7 - Bb7 (F7, G7, A7, Bb7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.6875),  # F7
    pretty_midi.Note(velocity=100, pitch=89, start=1.6875, end=1.875), # G7
    pretty_midi.Note(velocity=100, pitch=91, start=1.875, end=2.0625), # A7
    pretty_midi.Note(velocity=100, pitch=90, start=2.0625, end=2.25), # Bb7
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.6875),   # F
    pretty_midi.Note(velocity=80, pitch=54, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=52, start=1.875, end=2.0625), # E
    pretty_midi.Note(velocity=80, pitch=55, start=2.0625, end=2.25),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=80, pitch=58, start=1.875, end=2.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.0),   # F
    # Bar 3: G7 on beat 2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.5625), # B
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5625), # F
    # Bar 4: A7 on beat 2
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.0625), # E
    pretty_midi.Note(velocity=80, pitch=66, start=4.875, end=5.0625), # G
]
piano.notes.extend(piano_notes)

# Bar 2: Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Sax repeats motif, transposed up a 3rd
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=92, start=3.0, end=3.1875),  # G7
    pretty_midi.Note(velocity=100, pitch=94, start=3.1875, end=3.375), # A7
    pretty_midi.Note(velocity=100, pitch=96, start=3.375, end=3.5625), # Bb7
    pretty_midi.Note(velocity=100, pitch=95, start=3.5625, end=3.75), # C7
]
sax.notes.extend(sax_notes)

# Bass: Walking line in G
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.1875),   # G
    pretty_midi.Note(velocity=80, pitch=56, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=80, pitch=54, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=80, pitch=57, start=3.5625, end=3.75),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: G7 on beat 2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.5625), # B
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5625), # F
    # Bar 4: A7 on beat 2
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.0625), # E
    pretty_midi.Note(velocity=80, pitch=66, start=4.875, end=5.0625), # G
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.3125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Sax finishes motif, transposed up a 3rd
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=95, start=4.5, end=4.6875),  # A7
    pretty_midi.Note(velocity=100, pitch=97, start=4.6875, end=4.875), # Bb7
    pretty_midi.Note(velocity=100, pitch=99, start=4.875, end=5.0625), # C7
    pretty_midi.Note(velocity=100, pitch=98, start=5.0625, end=5.25), # B7
]
sax.notes.extend(sax_notes)

# Bass: Walking line in A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.6875),   # A
    pretty_midi.Note(velocity=80, pitch=58, start=4.6875, end=4.875), # B
    pretty_midi.Note(velocity=80, pitch=56, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=80, pitch=59, start=5.0625, end=5.25),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: A7 on beat 2
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.0625), # E
    pretty_midi.Note(velocity=80, pitch=66, start=4.875, end=5.0625), # G
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.8125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
