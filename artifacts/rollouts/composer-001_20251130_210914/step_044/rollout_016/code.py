
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
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0), # Ab
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5), # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875), # C#
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0), # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2
    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.625), # F7: F, A, C, Eb
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=69, start=2.25, end=2.625),
    # Bar 2, beat 4
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.375),
    # Bar 3, beat 2
    pretty_midi.Note(velocity=85, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.125),
    # Bar 3, beat 4
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.875),
    # Bar 4, beat 2
    pretty_midi.Note(velocity=85, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=85, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=85, pitch=69, start=5.25, end=5.625),
    # Bar 4, beat 4
    pretty_midi.Note(velocity=85, pitch=62, start=6.0, end=6.375),
    pretty_midi.Note(velocity=85, pitch=64, start=6.0, end=6.375),
    pretty_midi.Note(velocity=85, pitch=67, start=6.0, end=6.375),
    pretty_midi.Note(velocity=85, pitch=69, start=6.0, end=6.375),
]
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2, beat 1: Fm7 (F, Ab, C, Eb) - motif starts on Eb
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75), # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0), # C
    # Bar 2, beat 2: leave it hanging on C
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25), # C
    # Bar 3, beat 1: come back with Fm7 again
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25), # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5), # C
    # Bar 3, beat 2: move to Ab
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75), # Ab
    # Bar 3, beat 3: move up to Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0), # Bb
    # Bar 4, beat 1: resolve back to F
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0), # C
    # Bar 4, beat 2: move to Ab
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25), # Ab
    # Bar 4, beat 3: move to Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5), # Bb
    # Bar 4, beat 4: resolve to F
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75), # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0), # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    pretty_midi.Note(velocity=100, pitch=36, start=5.875, end=6.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
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
